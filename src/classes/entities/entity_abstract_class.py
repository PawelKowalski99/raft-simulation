from abc import ABC, abstractmethod


class EntityAbstract(ABC):
    """"
    The abstract parent for objects on board
    """
    type = None
    symbol = None

    @abstractmethod
    def __init__(self, position):
        """
        Initialization
        :param (int, int) position: x and y position where Stick should be put
        """
        self.position = position
