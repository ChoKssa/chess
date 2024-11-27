from .Player import Player
from .Board import Board
from .NetworkManager import NetworkManager
from .types.gameState import GameState
from .types.position import Position

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
        pass

    def resetGame(self):
        self.board = Board()
        self.startGame()

    def makeMove(self, initialPos: Position, finalPos: Position):
        self.board.makeMove(initialPos, finalPos)
        self.switchPlayer()
