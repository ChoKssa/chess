from .Piece import Piece
from ..types.position import Position

class King(Piece):
    def __init__(self, isWhite: bool, position):
        super().__init__(isWhite, position)

    def getValidMoves(self, board):
        validMoves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            nextRow = self.position.row + dr
            nextCol = self.position.col + dc
            nextPos = Position(nextRow, nextCol)

            if not nextPos.isWithinBounds():
                continue

            piece = board.getPieceAtPosition(nextPos)

            if piece is None or piece.isWhite != self.isWhite:
                validMoves.append(nextPos)

        return validMoves
