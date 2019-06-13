import random
from abc import ABC, abstractmethod
from src.classes.entities.entity_abstract_class import EntityAbstract

from classes.entities.entity_abstract_class import EntityAbstract

class EffectEntityAbstract(EntityAbstract, ABC):
    """
    Abstract class for items with some effect
    """
    @abstractmethod
    def __init__(self, position):
        """
        Abstract initialization of effect objects
        :param (int, int) position: x and y position where Stick should be put
        """
        super(EffectEntityAbstract, self).__init__(position)
        self.effect_value = random.randint(10, 20)
