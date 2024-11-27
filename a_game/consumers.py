from channels.generic.websocket import AsyncWebsocketConsumer
import json
from chess.NetworkManager import NetworkManager

class GameConsumer(AsyncWebsocketConsumer):
    games = {}

    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_group_name = f'game_{self.game_id}'
        self.games[self.game_id] = NetworkManager()

        await self.channel_layer.group_add(
            self.game_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Quitter un groupe
        await self.channel_layer.group_discard(
            self.game_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        move = text_data_json['move']
        id = text_data_json['id']

        # Envoyer un événement à un groupe
        await self.channel_layer.group_send(
            self.game_group_name,
            {
                'type': 'game_move',
                'move': move
            }
        )

    async def game_move(self, event):
        move = event['move']

        # Envoyer le mouvement aux WebSocket clients
        await self.send(text_data=json.dumps({
            'move': move
        }))
