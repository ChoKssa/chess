class Position:
    def __init__(self, file: str, rank: int):
        if file not in 'abcdefgh' or not (1 <= rank <= 8):
            raise ValueError("Invalid position on the chess board")
        self.file = file
        self.rank = rank

    def __repr__(self):
        return f"Position({self.file!r}, {self.rank!r})"

    def __str__(self):
        return f"{self.file}{self.rank}"

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.file == other.file and self.rank == other.rank
        return False

    def __hash__(self):
        return hash((self.file, self.rank))
