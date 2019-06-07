import random
from abc import ABC, abstractmethod


class DamagableAbstract(ABC):
    """
    Abstract class for items with some effect
    """
    @abstractmethod
    def __init__(self):
        """
        Initialization of DamagableAbstract
        """
        self.is_gone = False
        self.effect_value = random.randint(70, 100)
        self.effect_status = False

    @abstractmethod
    def simulate_damage(self):
        """
        Simulation of effect.
        :return:
        """
        pass
