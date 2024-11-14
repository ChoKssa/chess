class Player():
    def __init__(self, name: str, isWhite: bool):
        super().__init__()
        self.name = name
        self.isWhite = isWhite
        self.isCurrentPlayer = False
        self.isInCheck = False


    def makeMove(self, move):
        pass
