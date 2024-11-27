from chess.Player import Player
from chess.Game import Game
from chess.types.position import Position

def main():
    p1 = Player("Player 1", True)
    p2 = Player("Player 2", False)
    game = Game(p1, p2)

    game.startGame()

    game.makeMove(Position(6, 5), Position(5, 5))
    game.makeMove(Position(1, 4), Position(2, 4))
    game.makeMove(Position(6, 6), Position(4, 6))
    game.makeMove(Position(0, 3), Position(4, 7))

    game.board.debugPrintBoard()
    game.checkEndConditions()

if __name__ == "__main__":
    main()
