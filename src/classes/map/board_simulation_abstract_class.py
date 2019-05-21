import random
from abc import ABC

from Food_class import Food
from map.board_data_abstract_class import BoardDataAbstract
from obstacle_class import Obstacle
from stick_class import Stick
from water_class import Water


class BoardSimulationAbstract(BoardDataAbstract, ABC):

    def move(self):
        self.__move_raft__()
        self.__move_map_down__()
        self.__add_random__()

    def __move_raft__(self):
        raft = self.__find_raft__()
        end_position = raft.get_end_position(self)

        if end_position is None:
            return None

        previous_position = raft.position
        if raft.position[0] - end_position[0] > 0 and \
                self.objects_on_board[(raft.position[0] - 1, raft.position[1])].type == 'water':
            raft.position = (raft.position[0] - 1, raft.position[1])
            self.add_object_to_map(raft)
            self.objects_on_board[previous_position] = Water(previous_position)

        elif raft.position[0] - end_position[0] < 0 and \
                self.objects_on_board[(raft.position[0] + 1, raft.position[1])].type == 'water':
            raft.position = (raft.position[0] + 1, raft.position[1])
            self.add_object_to_map(raft)
            self.objects_on_board[previous_position] = Water(previous_position)

    def __move_map_down__(self):

        raft_inv = self.__find_raft__().raft.inventory
        for i in range(self.size, 0, -1):
            for j in range(self.size - 1, 0, -1):
                if self.objects_on_board[(i, j + 1)].type is not "raft_and_human":
                    object_on_map = self.objects_on_board[(i, j)]
                    object_on_map.position = (i, j + 1)
                    self.objects_on_board.update({object_on_map.position: object_on_map})

                elif self.objects_on_board[(i, j + 1)].type is "raft_and_human" and \
                        len(raft_inv['stick']) + len(raft_inv['food']) < self.__find_raft__().raft.inv_slots:

                    if self.objects_on_board[(i, j)].type is "obstacle":
                        self.__find_raft__().raft.effect_value -= self.objects_on_board[(i, j)].effect_object_value

                    elif self.objects_on_board[(i, j)].type is "food":
                        raft_inv["food"].append(self.objects_on_board[(i, j)])

                    elif self.objects_on_board[(i, j)].type is "stick":
                        raft_inv["stick"].append(self.objects_on_board[(i, j)])

                    self.objects_on_board[(i, j - 1)].position = (i, j)
                    object_on_map = self.objects_on_board[(i, j - 1)]
                    self.objects_on_board.update({self.objects_on_board[(i, j - 1)].position: object_on_map})

    def __find_raft__(self):
        return [value for value in self.objects_on_board.values() if
                value.type == 'raft_and_human'][0]

    def __add_random__(self):
        for i in range(self.size, 0, -1):
            random_object = random.choice([Water((i, 1)), Water((i, 1)),
                                           Water((i, 1)), Food((i, 1)),
                                           Stick((i, 1)), Obstacle((i, 1))])
            self.add_object_to_map(random_object)
