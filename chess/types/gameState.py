from enum import Enum

class GameState(Enum):
    WHITE_WIN = 1
    BLACK_WIN = 2
    DRAW = 3
    STALEMATE = 4
    IN_PROGRESS = 5
