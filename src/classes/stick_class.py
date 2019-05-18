from effect_object_abstract_class import EffectObjectAbstract
import random


class Stick(EffectObjectAbstract):
    """
    Instance of class is used to fix raft
    """
    def __init__(self, position):
        super(Stick, self).__init__(position)
        self.type = 'stick'
        self.symbol = 'S'
        self.repair_value = random.randint(30, 45)
