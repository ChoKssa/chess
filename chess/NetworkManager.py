from .Game import Game
from .Player import Player

class NetworkManager():
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.isGameReady = False
        self.game = None

    def setPlayer(self, player: Player):
        print(self.p1)
        print(self.p2)
        if self.p1 is None:
            self.p1 = player
            print(self.p1)
            print("Player 1 set")
        else:
            self.p2 = player
            print("Player 2 set")
            self.isGameReady = True
            self.game = Game(self.p1, self.p2)

    def getGameBoard(self):
        pass
