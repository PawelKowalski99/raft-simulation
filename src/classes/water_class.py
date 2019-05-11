from empty_object_class import EmptyObjectAbstract


class Water(EmptyObjectAbstract):

    def __init__(self, position):
        super(Water, self).__init__(position)
        self.type = 'water'
        self.symbol = 'W'
