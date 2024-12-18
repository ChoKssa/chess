from .Player import Player
from .Board import Board
from .types.gameState import GameState
from .types.position import Position

class Game:
    def __init__(self, whitePlayer: Player, blackPlayer: Player):
        self.whitePlayer = whitePlayer
        self.blackPlayer = blackPlayer
        self.currentPlayer = None
        self.board = Board()
        self.isGameOver = False
        self.state: GameState = GameState.IN_PROGRESS

    def startGame(self):
        self.board.setupBoard()
        self.currentPlayer = self.whitePlayer

    # def endGame(self, winner):
    #     pass

    def switchPlayer(self):
        if self.currentPlayer == self.whitePlayer:
            self.currentPlayer = self.blackPlayer
        else:
            self.currentPlayer = self.whitePlayer

    def getBoard(self):
        return self.board

    def getCurrentPlayer(self):
        return self.currentPlayer

    def checkEndConditions(self):
        status = self.board.getStatus()

        if status == "Checkmate":
            self.state = GameState.WHITE_WIN if self.currentPlayer == self.whitePlayer else GameState.BLACK_WIN
            self.isGameOver = True

        return self.state

    def resetGame(self):
        self.board = Board()
        self.startGame()

    def makeMove(self, initialPos: Position, finalPos: Position):
        self.board.makeMove(initialPos, finalPos)
        self.switchPlayer()

    def __repr__(self):
        return f"Game(whitePlayer={self.whitePlayer}, blackPlayer={self.blackPlayer}, currentPlayer={self.currentPlayer}, board={self.board}, isGameOver={self.isGameOver}, state={self.state})"
