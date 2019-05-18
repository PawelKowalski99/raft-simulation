import random
from abc import ABC

from Food_class import Food
from map.board_data_abstract_class import BoardDataAbstract
from obstacle_class import Obstacle
from raft_and_human_classes import RaftAndHuman
from stick_class import Stick
from water_class import Water


class BoardInitializeAbstract(BoardDataAbstract, ABC):

    def initialize(self, reader):
        self.__create_empty_map__()

        self.add_object_to_map(RaftAndHuman(self.__find_empty_position_for_raft__()))
        for _ in range(reader.number_of_food):
            self.add_object_to_map(Food(self.__find_empty_position_for_first_items__()))

        for _ in range(reader.number_of_wood):
            self.add_object_to_map(Stick(self.__find_empty_position_for_first_items__()))

        for _ in range(reader.number_of_cbstacles):
            self.add_object_to_map(Obstacle(self.__find_empty_position_for_first_items__()))

    def __find_empty_position_for_raft__(self):
        return random.choice([value.position for value in self.objects_on_board.values()
                              if value.type is 'water' and value.position[1] == self.size])

    def __find_empty_position_for_first_items__(self):
        return random.choice([value.position for value in self.objects_on_board.values()
                              if value.type is 'water' and value.position[1] < self.size])

    def __create_empty_map__(self):

        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                self.add_object_to_map(Water((x, y)))
