from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from django.contrib.auth.decorators import login_required

@login_required
def create_game(request):
    game = Game.objects.create()
    game.players.add(request.user)
    game.save()
    return redirect('a_game:game_detail', game_id=game.id)

@login_required
def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'a_game/game_detail.html', {'game': game})
