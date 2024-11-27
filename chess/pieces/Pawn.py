from .Piece import Piece
from ..types.position import Position

class Pawn(Piece):
    def __init__(self, isWhite: bool, position):
        super().__init__(isWhite, position)


    def getValidMoves(self, board):
        validMoves = []
        directions = []

        if self.isWhite:
            directions = [(-1, 0), (-1, 1), (-1, -1)]
            if not self.hasMoved:
                directions.append((2, 0))
        else:
            directions = [(1, 0), (1, 1), (1, -1)]
            if not self.hasMoved:
                directions.append((-2, 0))

        nextPos = Position(self.position.row + directions[0][0], self.position.col + directions[0][1])
        if nextPos.isWithinBounds():
            piece = board.getPieceAtPosition(nextPos)
            if piece is None:
                validMoves.append(nextPos)

        for i in range(1, len(directions)):
            nextPos = Position(self.position.row + directions[i][0], self.position.col + directions[i][1])
            if nextPos.isWithinBounds():
                piece = board.getPieceAtPosition(nextPos)
                if piece is not None and piece.isWhite != self.isWhite:
                    validMoves.append(nextPos)

        return validMoves

    def move(self, board, newPosition):
        pass

    def promote(self, newPiece):
        pass

    def canEnPassant(self):
        pass
