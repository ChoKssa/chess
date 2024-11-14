from typing import List
from .MoveHistory import MoveHistory
from .pieces import Pawn, Rook, Knight, Bishop, Queen, King, Piece

class BoardCell:
    def __init__(self, piece=None):
        self.piece: Piece = piece

    def isEmpty(self):
        return self.piece is None

    def getPiece(self):
        return self.piece

    def setPiece(self, piece: Piece):
        self.piece = piece


class Board:
    def __init__(self):
        self.gridSize = 8
        self.board: List[List[BoardCell]] = [[BoardCell() for _ in range(self.gridSize)] for _ in range(self.gridSize)]
        self.history = MoveHistory()
        self.captureHistory = []

    def setupBoard(self):
        piece_order: List[Piece] = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for col in range(self.gridSize):
            self.board[1][col].setPiece(Pawn(isWhite=False, position=(1, col)))
            self.board[6][col].setPiece(Pawn(isWhite=True, position=(6, col)))

        for col, piece_class in enumerate(piece_order):
            self.board[0][col].setPiece(piece_class(isWhite=False, position=(0, col)))

        for col, piece_class in enumerate(piece_order):
            self.board[7][col].setPiece(piece_class(isWhite=True, position=(7, col)))

    def validateMove(self, move):
        pass

    def getPieceAtPosition(self, position):
        pass

    def isCheck(self):
        pass

    def isCheckmate(self):
        pass

    def isDraw(self):
        pass

    def isStalemate(self):
        pass

    def debugPrintBoard(self):
        piece_symbols = {
            "Pawn": "P",
            "Rook": "R",
            "Knight": "N",
            "Bishop": "B",
            "Queen": "Q",
            "King": "K"
        }

        for row in range(self.gridSize):
            row_str = ""
            for col in range(self.gridSize):
                cell = self.board[row][col]
                if cell.piece is None:
                    row_str += ". "
                else:
                    piece_type = type(cell.piece).__name__
                    symbol = piece_symbols.get(piece_type, "?")
                    row_str += (symbol.upper() if cell.piece.isWhite else symbol.lower()) + " "
            print(row_str.strip())
