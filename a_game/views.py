from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

@login_required
def create_game(request):
    game = Game.objects.create()
    game.players.add(request.user)
    game.save()
    return redirect('a_game:game_detail', game_id=game.id)

@login_required
def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    initial_board = [
        ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
        ["♙"] * 8,
        [""] * 8,
        [""] * 8,
        [""] * 8,
        [""] * 8,
        ["♟"] * 8,
        ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ]
    return render(request, 'a_game/game_detail.html', {
        'game': game,
        'board': initial_board
    })

@login_required
def update_board(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    # Exemple d'un plateau mis à jour
    updated_board = [
    ]

    # Retourner le plateau mis à jour
    return JsonResponse({'board': updated_board})

@login_required
def move_piece(request, game_id):
    """
    Gère le déplacement d'une pièce et met à jour le plateau.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        from_row, from_col = data['from']
        to_row, to_col = data['to']

        # Récupérer le jeu et l'échiquier
        game = get_object_or_404(Game, id=game_id)
        board = game.board

        # Effectuer le mouvement de la pièce
        piece = board[from_row][from_col]
        board[from_row][from_col] = ''
        board[to_row][to_col] = piece

        # Sauvegarder les modifications du jeu
        game.save()

        # Retourner le plateau mis à jour via WebSocket
        return JsonResponse({'board': board})
