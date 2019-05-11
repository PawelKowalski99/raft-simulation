from effect_object_abstract_class import EffectObjectAbstract
import random


class Obstacle(EffectObjectAbstract):
    """
    Instance of class is used to lower hp of raft
    """
    def __init__(self, position):
        super(Obstacle, self).__init__(position)
        self.type = 'obstacle'
        self.symbol = 'O'
