from abc import ABC, abstractmethod
from chess.types.position import Position

class Piece(ABC):
    def __init__(self, isWhite: bool, position: Position):
        self.isWhite = isWhite
        self.position = position
        self.hasMoved = False
        self.captured = False

    @abstractmethod
    def getValidMoves(self, board):
        pass

    def move(self, board, newPosition: Position):
        pass

    def isCaptured(self):
        return self.captured

    def __repr__(self):
        return f"{self.__class__.__name__}({self.isWhite}, {self.position})"
