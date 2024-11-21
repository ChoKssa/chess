from .Player import Player
from .Board import Board
from .NetworkManager import NetworkManager
from .types.gameState import GameState

class Game:
    def __init__(self, whitePlayer: Player, blackPlayer: Player):
        self.whitePlayer = whitePlayer
        self.blackPlayer = blackPlayer
        self.currentPlayer = None
        self.board = Board()
        # self.networkManager = NetworkManager()
        self.isGameOver = False
        self.state: GameState = GameState.IN_PROGRESS

    def startGame(self):
        """Setup the board and assign the current player."""
        self.board.setupBoard()
        self.currentPlayer = self.whitePlayer
        self.isGameOver = False
        self.state = GameState.IN_PROGRESS

    def endGame(self, winner: Player = None):
        """Mark the game as over and set the winner."""
        self.isGameOver = True
        if winner:
            self.state = GameState.WHITE_WIN if winner == self.whitePlayer else GameState.BLACK_WIN
        else:
            self.state = GameState.DRAW


    def switchPlayer(self):
        """Switch the current player."""
        self.currentPlayer = self.blackPlayer if self.currentPlayer == self.whitePlayer else self.whitePlayer


    def getBoard(self):
        """Return the current state of the board."""
        return self.board

    def getCurrentPlayer(self):
        """Return the player whose turn it is."""
        return self.currentPlayer


    def checkEndConditions(self):
        """Check for game-ending conditions."""
        if Rules.is_checkmate(self.board, self.currentPlayer.color):
            self.endGame(winner=self.currentPlayer.opponent)
        elif Rules.is_stalemate(self.board, self.currentPlayer.color):
            self.endGame()  # Stalemate results in a draw
        elif len(self.board.getMoveHistory()) >= 50:  # Optional: 50-move rule
            self.endGame()


    def resetGame(self):
        """Reset the game to its initial state."""
        self.board.setupBoard()
        self.currentPlayer = self.whitePlayer
        self.isGameOver = False
        self.state = GameState.IN_PROGRESS


    from .rules import Rules

    def validateMove(self, player: Player, start: Position, end: Position):
        """Validate a player's move."""
        if player != self.currentPlayer:
            raise ValueError("It's not this player's turn.")
        piece = self.board.getPieceAtPosition(start)
        if not piece or piece.isWhite != player.isWhite:
            raise ValueError("Invalid piece selection.")
        return Rules.validate_move(piece, start, end, self.board)


    def handlePlayerMove(self, player: Player, start: Position, end: Position):
        """Handle a player's move."""
        if not self.validateMove(player, start, end):
            raise ValueError("Invalid move.")
        self.board.movePiece(start, end)  # Move the piece on the board
        self.checkEndConditions()  # Check for game-ending conditions
        self.switchPlayer()  # Switch to the next player

