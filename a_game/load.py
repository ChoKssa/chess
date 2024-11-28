import json
from asgiref.sync import sync_to_async
from .models import Game as GameModel
from chess.Game import Game
from chess.Player import Player
from chess.Board import Board
from chess.types.position import Position
from chess.pieces import Pawn, Rook, Knight, Bishop, Queen, King

def load_game_from_model(game_model: GameModel) -> Game:
    """
    Convertit un objet Django Game en une instance de la classe Python Game.

    Args:
        game_model (GameModel): L'instance du modèle Django Game.

    Returns:
        Game: Une instance de la classe Python Game.
    """
    # Créer les joueurs
    white_player = Player(game_model.white_player.username, True) if game_model.white_player else None
    black_player = Player(game_model.black_player.username, False) if game_model.black_player else None

    # Initialiser la classe Game
    python_game = Game(whitePlayer=white_player, blackPlayer=black_player)

    # Charger le plateau
    if game_model.board_state:
        board_state = json.loads(game_model.board_state)
        python_game.board = load_board_from_state(board_state)

    # Définir le joueur actuel
    python_game.currentPlayer = white_player if game_model.current_turn == 'WHITE' else black_player

    # Mettre à jour l'état du jeu
    python_game.isGameOver = game_model.status == 'finished'

    return python_game

def load_board_from_state(board_state) -> Board:
    """
    Charge une instance de Board à partir de son état JSON.

    Args:
        board_state (dict): L'état du plateau sous forme de JSON.

    Returns:
        Board: Une instance de Board.
    """
    board = Board()
    for row_idx, row in enumerate(board_state):
        for col_idx, cell in enumerate(row):
            if cell is not None:
                # Exemple : Charger les pièces selon leur type
                piece_class = get_piece_class_from_name(cell['type'])
                is_white = cell['is_white']
                position = Position(row=row_idx, col=col_idx)
                piece = piece_class(isWhite=is_white, position=position)
                board.board[row_idx][col_idx].setPiece(piece)
    return board

def get_piece_class_from_name(name: str):
    """
    Récupère la classe de pièce correspondant à un nom donné.

    Args:
        name (str): Le nom de la pièce (e.g., 'Pawn', 'Rook').

    Returns:
        type: La classe correspondante.
    """
    piece_classes = {
        'Pawn': Pawn,
        'Rook': Rook,
        'Knight': Knight,
        'Bishop': Bishop,
        'Queen': Queen,
        'King': King
    }
    return piece_classes.get(name)


def update_model_from_game(python_game: Game, game_model: GameModel) -> GameModel:
    """
    Met à jour le modèle Django Game à partir de la classe Python Game.

    Args:
        python_game (Game): L'instance de la classe Python Game.
        game_model (GameModel): L'instance du modèle Django Game à mettre à jour.

    Returns:
        GameModel: L'instance du modèle mise à jour.
    """
    # Mettre à jour le statut
    game_model.status = 'finished' if python_game.isGameOver else 'ongoing'

    # Mettre à jour le joueur actuel
    if python_game.currentPlayer:
        game_model.current_turn = 'WHITE' if python_game.currentPlayer.isWhite else 'BLACK'

    # Sauvegarder l'état du plateau en JSON
    game_model.board_state = json.dumps(dump_board_to_state(python_game.board))

    return game_model


def dump_board_to_state(board) -> list:
    """
    Convertit l'état d'une instance de Board en un format sérialisable JSON.

    Args:
        board (Board): L'instance de Board.

    Returns:
        list: L'état du plateau sous forme de liste de listes.
    """
    board_state = []
    for row in board.board:
        board_row = []
        for cell in row:
            if cell.isEmpty():
                board_row.append(None)
            else:
                piece = cell.getPiece()
                board_row.append({
                    'type': type(piece).__name__,  # Nom de la classe de la pièce
                    'is_white': piece.isWhite,
                })
        board_state.append(board_row)
    return board_state
