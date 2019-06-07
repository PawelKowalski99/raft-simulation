from abc import ABC, abstractmethod


class EntityAbstract(ABC):
    type = None
    symbol = None


    @abstractmethod
    def __init__(self, position):
        self.position = position
