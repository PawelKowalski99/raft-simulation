from classes.entities.entity_abstract_class import EntityAbstract


class WaterField(EntityAbstract):
    """
    Representation of empty field on ocean.
    """
    type = 'water'
    symbol = 'W'

    def __init__(self, position):
        """
        Initialization of WaterField
        :param (int, int) position: x and y position where WaterField should be put
        """
        super(WaterField, self).__init__(position)
