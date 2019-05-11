from empty_object_class import EmptyObjectAbstract
from abc import ABC, abstractmethod
import random


class EffectObjectAbstract(EmptyObjectAbstract, ABC):
    """
    Abstract class for items with some effect
    """
    @abstractmethod
    def __init__(self, position):
        super(EffectObjectAbstract, self).__init__(position)
        self.effect_status = random.randint(20, 40)
