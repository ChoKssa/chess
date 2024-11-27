class Player():
    def __init__(self, name: str, isWhite: bool):
        super().__init__()
        self.name = name
        self.isWhite = isWhite
        self.isCurrentPlayer = False
        self.isInCheck = False


    def makeMove(self, move):
        pass

    def __eq__(self, value):
        return self.name == value.name and self.isWhite == value.isWhite
