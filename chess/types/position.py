class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return isinstance(other, Position) and self.row == other.row and self.col == other.col

    def __repr__(self):
        return f"({self.row}, {self.col})"

    def isWithinBounds(self) -> bool:
        return 0 <= self.row < 8 and 0 <= self.col < 8

    def add(self, dr: int, dc: int):
        return Position(self.row + dr, self.col + dc)
