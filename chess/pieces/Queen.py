from .Piece import Piece

class Queen(Piece):
    def __init__(self, isWhite: bool, position):
        super().__init__(isWhite, position)

    def getValidMoves(self, board):
        pass
