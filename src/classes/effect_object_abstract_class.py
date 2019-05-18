import random
from abc import ABC, abstractmethod

from empty_object_class import EmptyObjectAbstract


class EffectObjectAbstract(EmptyObjectAbstract, ABC):
    """
    Abstract class for items with some effect
    """
    @abstractmethod
    def __init__(self, position):
        super(EffectObjectAbstract, self).__init__(position)
        self.effect_object_value = random.randint(20, 40)
