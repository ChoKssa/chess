from .Piece import Piece
from ..types.position import Position

class Rook(Piece):
    def __init__(self, isWhite: bool, position):
        super().__init__(isWhite, position)

    def getValidMoves(self, board):
        validMoves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                nextRow = self.position.row + dr * i
                nextCol = self.position.col + dc * i
                nextPos = Position(nextRow, nextCol)

                if not nextPos.isWithinBounds():
                    break

                piece = board.getPieceAtPosition(nextPos)

                if piece is None:
                    validMoves.append(nextPos)
                elif piece.isWhite != self.isWhite:
                    validMoves.append(nextPos)
                    break
                else:
                    break

        return validMoves
