from classes.entities.effect_entity_abstract_class import EffectEntityAbstract
import random


class Stick(EffectEntityAbstract):
    """
    Representation of stick on ocean.
    Instance of class is used to fix a raft
    """
    type = 'stick'
    symbol = 'S'
    def __init__(self, position):
        """
        Initialization of Stick
        :param (int, int) position: x and y position where Stick should be put
        """
        super(Stick, self).__init__(position)
        self.effect_value = random.randint(35, 45)
