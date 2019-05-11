from abc import ABC, abstractmethod
import random
from effect_object_abstract_class import EffectObjectAbstract


class Food(EffectObjectAbstract):
    """
    Instance of class is used by human so as not to die from hunger.
    """
    def __init__(self, position):
        super(Food, self).__init__(position)
        self.type = 'food'
        self.symbol = 'F'
        self.wholesomeness = random.randint(40, 61)
        self.__durability = random.randint(80, 101)

    def food_simulation(self, board):
        self.decomposition()

        if self.__durability <= 0:
            board.remove_object_from_map(self)
