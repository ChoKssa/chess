class MoveHistory:
    def __init__(self):
        self.history = []

    def addMove(self, move):
        self.history.append(move)

    def getMove(self, index):
        return self.history[index]

    def getLatestMove(self):
        return self.history[-1]
