import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404
from .models import Game

class GameConsumer(AsyncWebsocketConsumer):
    games = {}

    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.room_group_name = f'game_{self.game_id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        move = data.get('move', None)
        if move:
            game = get_object_or_404(Game, id=self.game_id)
            board = game.board
            from_row, from_col = move['from']
            to_row, to_col = move['to']
            piece = board[from_row][from_col]
            board[from_row][from_col] = ''
            board[to_row][to_col] = piece
            game.board = board
            game.save()
            await self.send_move_update()

    async def send_move_update(self):
        game = get_object_or_404(Game, id=self.game_id)
        updated_board = game.board
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
