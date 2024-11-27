from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    players = models.ManyToManyField(User, related_name="games")
    white_player = models.ForeignKey(User, related_name="white_games", on_delete=models.SET_NULL, null=True, blank=True)
    black_player = models.ForeignKey(User, related_name="black_games", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('ongoing', 'Ongoing'), ('finished', 'Finished')], default='pending')
    board_state = models.TextField(null=True, blank=True)  # JSON-encoded board state
    current_turn = models.CharField(max_length=5, choices=[('WHITE', 'White'), ('BLACK', 'Black')], default='WHITE')

    def __str__(self):
        return f"Game {self.id} - Status: {self.status}"

    def add_player(self, user):
        if self.players.count() < 2:
            self.players.add(user)
            if self.white_player is None:
                self.white_player = user
            elif self.black_player is None:
                self.black_player = user
            self.save()
            return True
        return False
