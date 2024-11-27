from .Piece import Piece
from ..types.position import Position

class Pawn(Piece):
    def __init__(self, isWhite: bool, position):
        super().__init__(isWhite, position)


    def getValidMoves(self, board):
        validMoves = []
        directions = [(1, 0), (1, 1), (1, -1)]

        if not self.hasMoved:
            directions.append((2, 0))

        if self.isWhite:
            directions = [(-1, 0), (-1, 1), (-1, -1)]

        if not self.hasMoved:
            directions.append((-2, 0))

        for dr, dc in directions:
            nextRow = self.position.row + dr
            nextCol = self.position.col + dc
            nextPos = Position(nextRow, nextCol)

            if not nextPos.isWithinBounds():
                continue

            piece = board.getPieceAtPosition(nextPos)

            if piece is None:
                validMoves.append(nextPos)

        return validMoves

    def move(self, board, newPosition):
        pass

    def promote(self, newPiece):
        pass

    def canEnPassant(self):
        pass
