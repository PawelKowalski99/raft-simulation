from abc import ABC, abstractmethod


class EmptyObjectAbstract(ABC):

    @abstractmethod
    def __init__(self, position):
        self.position = position
        self.type = None
        self.symbol = None
