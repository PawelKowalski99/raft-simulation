import random

from classes.entities.effect_entity_abstract_class import EffectEntityAbstract


class Food(EffectEntityAbstract):
    """
    Representation of food on ocean.
    Instance of class is used by human so as not to die from hunger.
    """
    type = 'food'
    symbol = 'F'
    def __init__(self, position):
        """
        Initialization of Food
        :param (int, int) position: x and y position where Stick should be put
        """
        super(Food, self).__init__(position)

        self.effect_value = random.randint(30, 45)
        self.__durability = random.randint(80, 101)

    def decomposition(self):
        """
        Simulates decomposition of food
        """
        self.__durability -= 5
        if self.__durability <= 0:
            del self
