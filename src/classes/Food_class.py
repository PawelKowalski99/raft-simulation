import random

from classes.effect_object_abstract_class import EffectObjectAbstract


class Food(EffectObjectAbstract):
    """
    Instance of class is used by human so as not to die from hunger.
    """
    def __init__(self, position):
        super(Food, self).__init__(position)
        self.type = 'food'
        self.symbol = 'F'
        self.wholesomeness = random.randint(30, 45)
        self.__durability = random.randint(80, 101)

    def simulation(self):
        self.__durability -= 5
        if self.__durability <= 0:
            del self
