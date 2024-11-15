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
        self.board.setupBoard()
        self.currentPlayer = self.whitePlayer

    def endGame(self, winner):
        pass

    def switchPlayer(self):
        pass

    def getBoard(self):
        pass

    def getCurrentPlayer(self):
        pass

    def checkEndConditions(self):
        pass

    def resetGame(self):
        pass

    def validateMove(self, player, move):
        pass

    def handlePlayerMove(self, player, move):
        pass
