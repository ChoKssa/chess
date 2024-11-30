from typing import List
from .MoveHistory import MoveHistory
from .pieces import Pawn, Rook, Knight, Bishop, Queen, King, Piece
from .types.position import Position
from .types.gameState import GameState
from .Player import Player
import copy

class BoardCell:
    def __init__(self, piece=None):
        self.piece: Piece = piece

    def isEmpty(self):
        return self.piece is None

    def getPiece(self):
        return self.piece

    def setPiece(self, piece: Piece):
        self.piece = piece

    def __repr__(self):
        return f"BoardCell(piece={self.piece})"


class Board:
    def __init__(self):
        self.gridSize = 8
        self.board: List[List[BoardCell]] = [[BoardCell() for _ in range(self.gridSize)] for _ in range(self.gridSize)]
        self.history = MoveHistory()
        self.captureHistory = []

    def setupBoard(self):
        piece_order: List[Piece] = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for col in range(self.gridSize):
            self.board[1][col].setPiece(Pawn(isWhite=False, position=Position(1, col)))
            self.board[6][col].setPiece(Pawn(isWhite=True, position=Position(6, col)))

        for col, piece_class in enumerate(piece_order):
            self.board[0][col].setPiece(piece_class(isWhite=False, position=Position(0, col)))

        for col, piece_class in enumerate(piece_order):
            self.board[7][col].setPiece(piece_class(isWhite=True, position=Position(7, col)))

    def validateMove(self, move):
        pass

    def getPieceAtPosition(self, position: Position):
        return self.board[position.row][position.col].getPiece()

    def makeMove(self, initialPos: Position, finalPos: Position):
        piece = self.getPieceAtPosition(initialPos)
        captured_piece = self.getPieceAtPosition(finalPos)

        if piece is None:
            return False

        if captured_piece is not None:
            self.captureHistory.append(captured_piece)


        self.board[finalPos.row][finalPos.col].setPiece(piece)
        self.board[initialPos.row][initialPos.col].setPiece(None)
        piece.position = finalPos
        piece.hasMoved = True
        return True

    def getKingPosition(self, isWhite: bool) -> Position:
        for row in range(self.gridSize):
            for col in range(self.gridSize):
                piece = self.board[row][col].getPiece()
                if isinstance(piece, King) and piece.isWhite == isWhite:
                    return Position(row, col)
        return None


    def isCheck(self, isWhite: bool):
        king_position = self.getKingPosition(isWhite=isWhite)

        for row in range(self.gridSize):
            for col in range(self.gridSize):
                piece = self.board[row][col].getPiece()
                if piece is None:
                    continue
                if piece.isWhite == isWhite:
                    continue
                if king_position in piece.getValidMoves(self):
                    return True
        return False


    def simulateMove(self, initialPos: Position, finalPos: Position):
        fake_board = Board()
        fake_board.board = copy.deepcopy(self.board)
        piece = fake_board.getPieceAtPosition(initialPos)

        if piece is None:
            return False

        fake_board.board[finalPos.row][finalPos.col].setPiece(piece)
        fake_board.board[initialPos.row][initialPos.col].setPiece(None)

        isCheck = fake_board.isCheck(piece.isWhite)
        return isCheck

    def isCheckmate(self, isWhite: bool):
        # isCheck = self.isCheck(isWhite)

        # if not isCheck:
        #     return False

        for row in range(self.gridSize):
            for col in range(self.gridSize):
                piece = self.board[row][col].getPiece()
                if piece is None:
                    continue
                if piece.isWhite != isWhite:
                    continue

                valid_moves = piece.getValidMoves(self)
                for move in valid_moves:
                    if not self.simulateMove(piece.position, move):
                        return False
        return True

    def isDraw(self):
        pass

    def isStalemate(self):
        pass

    def getStatus(self):
        if self.isCheckmate(True):
            return "Checkmate"
        if self.isCheckmate(False):
            return "Checkmate"
        elif self.isDraw():
            return "Draw"
        elif self.isStalemate():
            return "Stalemate"
        elif self.isCheck(True):
            return "Check"
        elif self.isCheck(False):
            return "Check"
        else:
            return

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

    def __repr__(self):
        return f"Board(gridSize={self.gridSize}, board={self.board}, history={self.history}, captureHistory={self.captureHistory})"
