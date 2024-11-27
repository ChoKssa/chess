from .Game import Game

class NetworkManager():
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.isGameReady = False
        self.game = None

    def setPlayer(self, player):
        if self.p1 is None:
            self.p1 = player
        else:
            self.p2 = player
        self.isGameReady = True
        self.game = Game(self.p1, self.p2)

    def getGameBoard(self):
        pass
