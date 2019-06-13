from abc import ABC, abstractmethod


class EntityAbstract(ABC):
    """"
    The abstract parent for objects on board
    """
    type = None
    symbol = None

    @abstractmethod
    def __init__(self, position):
        self.position = position
