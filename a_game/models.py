from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    players = models.ManyToManyField(User, related_name="games")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Game {self.id} - Status: {self.status}"
