from .Piece import Piece

class Rook(Piece):
    def __init__(self, isWhite: bool, position):
        super().__init__(isWhite, position)

    def getValidMoves(self, board):
        pass