import random
from abc import ABC, abstractmethod


class RaftOrHumanSimulationAbstract(ABC):
    """
    Abstract class for items with some effect
    """
    @abstractmethod
    def __init__(self):
        self.is_gone = False
        self.effect_value = random.randint(65, 100)
        self.effect_status = False

    @abstractmethod
    def simulation(self):
        self.effect_value -= 5

        if self.effect_value < 0:
            self.is_gone = True
        elif self.effect_value <= 40:
            self.effect_status = True
        elif self.effect_value >= 75:
            self.effect_status = False

        print(self.effect_value)
