from .Piece import Piece

class Pawn(Piece):
    def __init__(self, isWhite: bool, position):
        super().__init__(isWhite, position)


    def getValidMoves(self, board):
        pass

    def move(self, board, newPosition):
        pass

    def promote(self, newPiece):
        pass

    def canEnPassant(self):
        pass
