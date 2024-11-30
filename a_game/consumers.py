from typing import Dict
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404
from a_game.models import Game
from chess.Game import Game as GameLogic
from asgiref.sync import sync_to_async
from .load import load_game_from_model, update_model_from_game, dump_board_to_state
from chess.types.position import Position
from django.contrib.auth.models import User


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.room_group_name = f'game_{self.game_id}'
        self.player_id = self.scope['user'].id
        game = None
        self.game = await sync_to_async(get_object_or_404)(
           Game.objects.select_related('white_player', 'black_player'),
           id=self.game_id
        )
        self.user = await sync_to_async(get_object_or_404)(User, id=self.player_id)

        if self.game.status == "not_started":
            if self.game.white_player is None:
                if not await sync_to_async(self.game.add_player)((self.user)):
                    await self.close()
                    return
            elif self.game.black_player is None and self.game.white_player != self.user:
                if not await sync_to_async(self.game.add_player)((self.user)):
                    await self.close()
                    return
                self.game.status = "ongoing"
                await sync_to_async(self.game.save)()
            elif self.user not in [self.game.white_player, self.game.black_player]:
                await self.close()
                return

        if self.game.status == "ongoing" and self.game.board_state is None:
            game = load_game_from_model(self.game)
            game.startGame()
            self.game = update_model_from_game(game, self.game)
            await sync_to_async(self.game.save)()


        await sync_to_async(self.game.refresh_from_db)()
        white_player = await sync_to_async(lambda: self.game.white_player)()
        black_player = await sync_to_async(lambda: self.game.black_player)()
        board_state = []
        if self.game.board_state:
            board_state = self.generate_board(self.game.board_state)
        else:
            new_game = GameLogic(None, None)
            new_game.startGame()
            board_state = self.generate_board(json.dumps(dump_board_to_state(new_game.board)))
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({
            'board': board_state,
            'current_turn': self.game.current_turn,
            'status': self.game.status,
        }))

    def generate_board(self, board: str) -> Dict:
        board = json.loads(board)
        board_dict = []

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                board_dict.append({
                    "row": i,
                    "col": j,
                    "piece": cell
                })
        return board_dict



    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        move = data.get('move', None)
        game = await sync_to_async(get_object_or_404)(Game, id=self.game_id)
        game = load_game_from_model(self.game)

        if move:
            initPos = Position(move['from']["row"], move['from']['col'])
            finalPos = Position(move['to']["row"], move['to']["col"])
            game.makeMove(initPos, finalPos)
            game.board.debugPrintBoard()
            game = update_model_from_game(game, self.game)

            await sync_to_async(game.save)()
            await self.send_game_update()

    async def send_game_update(self):
        game = await sync_to_async(get_object_or_404)(Game, id=self.game_id)
        updated_board =self.generate_board(game.board_state)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'game_update',
                'board': updated_board,
                'current_turn': game.current_turn,
            }
        )

    async def game_update(self, event):
        await self.send(text_data=json.dumps({
            'board': event['board'],
            'current_turn': event['current_turn'],
        }))
