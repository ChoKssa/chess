from abc import ABC, abstractmethod

class NetworkManager(ABC):
    def __init__(self):
        super().__init__()

    # @abstractmethod
    def send(self, message):
        pass

    # @abstractmethod
    def receiveMove(self, move):
        pass

    # @abstractmethod
    def disconnectPlayer(self):
        pass

    def broadcastGameState(self, gameState):
        pass
