import random
from abc import ABC, abstractmethod

from classes.enities.entity_abstract_class import EntityAbstract


class EffectEntityAbstract(EntityAbstract, ABC):
    """
    Abstract class for items with some effect
    """
    @abstractmethod
    def __init__(self, position):
        super(EffectEntityAbstract, self).__init__(position)
        self.effect_value = random.randint(10, 20)
