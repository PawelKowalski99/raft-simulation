from classes.entities.effect_entity_abstract_class import EffectEntityAbstract


class Obstacle(EffectEntityAbstract):
    """
    Representation of obstacle on ocean.
    Instance of class is used to lower hp of raft
    """
    type = 'obstacle'
    symbol = 'O'

    def __init__(self, position):
        super(Obstacle, self).__init__(position)
