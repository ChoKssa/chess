from typing import Dict
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404
from a_game.models import Game
from asgiref.sync import sync_to_async
from .load import load_game_from_model, update_model_from_game
from chess.types.position import Position


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.room_group_name = f'game_{self.game_id}'

        self.game = await sync_to_async(get_object_or_404)(Game, id=self.game_id)
        game = load_game_from_model(self.game)
        game.startGame()
        game = update_model_from_game(game, self.game)

        await sync_to_async(game.save)()

        game = await sync_to_async(get_object_or_404)(Game, id=self.game_id)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        board =self.generate_board(game.board_state)
        await self.accept()
        await self.send(text_data=json.dumps({
            'board': board,
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
            print(move)
            initPos = Position(move['from']["row"], move['from']['col'])
            finalPos = Position(move['to']["row"], move['to']["col"])
            print(initPos, finalPos)
            game.makeMove(initPos, finalPos)
            game.board.debugPrintBoard()
            game = update_model_from_game(game, self.game)

            await sync_to_async(game.save)()
            await self.send_move_update()

    async def send_move_update(self):
        game = await sync_to_async(get_object_or_404)(Game, id=self.game_id)
        updated_board =self.generate_board(game.board_state)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'game_board_update',
                'board': updated_board,
            }
        )

    async def game_board_update(self, event):
        updated_board = event['board']
        await self.send(text_data=json.dumps({
            'board': updated_board,
        }))
