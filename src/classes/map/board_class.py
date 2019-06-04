import random

from classes.map.board_initialize_abstract_class import BoardInitializeAbstract
from classes.map.board_simulation_abstract_class import BoardSimulationAbstract


class Board(BoardInitializeAbstract, BoardSimulationAbstract):

    def __init__(self, size):
        super(Board, self).__init__(size)

    def show_map(self):
        for y in range(1, self.size + 1):
            object_list = []
            i = 0
            for x in range(1, self.size + 1):
                object_list.append(self.objects_on_board[(x, y)].symbol)
                i += 1
                if i == self.size:
                    print(object_list)
        print(self.size * 5 * "-")

    def show_objects(self):
        for key, value in self.objects_on_board.items():
            print(key, value)

    def get_thing(self, thing):
        return [object_on_map for object_on_map in self.objects_on_board.values() if
                object_on_map.type is thing]

    def __find_empty_position__(self):
        return random.choice([value.position for value in self.objects_on_board.values()
                              if value.type is 'water' and value.position[1] == 1])
