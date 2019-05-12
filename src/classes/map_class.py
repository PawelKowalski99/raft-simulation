import random
from water_class import Water
from raft_and_human_classes import RaftAndHuman
from Food_class import Food
from stick_class import Stick
from obstacle_class import Obstacle


class Map:

    def __init__(self, size):
        self.size = size
        self.objects_on_map = {}

    def show_map(self):
        for y in range(1, self.size + 1):
            object_list = []
            i = 0
            for x in range(1, self.size + 1):
                object_list.append(self.objects_on_map[(x, y)].symbol)
                i += 1
                if i == self.size:
                    print(object_list)
        print(self.size * 5 * "-")

    def show_objects(self):
        for key, value in self.objects_on_map.items():
            print(key, value)

    def move(self):
        self.__move_raft__()
        self.__move_map_down__()
        self.__add_random__()

    def add_object_to_map(self, map_object):
        self.objects_on_map[map_object.position] = map_object

    def remove_object_from_map(self, map_object):
        self.objects_on_map[map_object.position] = Water(map_object.position)

    def initialize(self, reader):
        self.__create_empty_map__()

        self.add_object_to_map(RaftAndHuman(self.__find_empty_position_for_raft__()))
        for i in range(reader.number_of_food):
            self.add_object_to_map(Food(self.__find_empty_position_for_first_items__()))

        for i in range(reader.number_of_wood):
            self.add_object_to_map(Stick(self.__find_empty_position_for_first_items__()))

        for i in range(reader.number_of_cbstacles):
            self.add_object_to_map(Obstacle(self.__find_empty_position_for_first_items__()))

    def get_food(self):
        return [object_on_map for object_on_map in self.objects_on_map.values() if
                object_on_map.type is 'food']

    def __move_raft__(self):
        raft = self.__find_raft__()
        end_position = raft.get_end_position(self)

        if end_position is None:
            return None

        previous_position = raft.position
        if raft.position[0] - end_position[0] > 0 and \
                self.objects_on_map[(raft.position[0] - 1, raft.position[1])].type == 'water':
            raft.position = (raft.position[0] - 1, raft.position[1])
            self.add_object_to_map(raft)
            self.objects_on_map[previous_position] = Water(previous_position)

        elif raft.position[0] - end_position[0] < 0 and \
                self.objects_on_map[(raft.position[0] + 1, raft.position[1])].type == 'water':
            raft.position = (raft.position[0] + 1, raft.position[1])
            self.add_object_to_map(raft)
            self.objects_on_map[previous_position] = Water(previous_position)

    def __move_map_down__(self):

        for i in range(self.size, 0, -1):
            for j in range(self.size - 1, 0, -1):
                if self.objects_on_map[(i, j + 1)].type is not "raft_and_human":
                    self.objects_on_map[(i, j)].position = (i, j+1)
                    object_on_map = self.objects_on_map[(i, j)]
                    self.objects_on_map.update({(self.objects_on_map[(i, j)].position):object_on_map})

                elif self.objects_on_map[(i, j + 1)].type is "raft_and_human":
                    if self.objects_on_map[(i, j)].type is "obstacle":
                        pass

                    elif self.objects_on_map[(i, j)].type is "food":
                        print(self.__find_raft__().raft.inventory["food"])
                        self.__find_raft__().raft.inventory["food"].append(self.objects_on_map[(i, j)])

                    elif self.objects_on_map[(i, j)].type is "stick":
                        pass

                    self.objects_on_map[(i, j - 1)].position = (i, j)
                    object_on_map = self.objects_on_map[(i, j - 1)]
                    self.objects_on_map.update({(self.objects_on_map[(i, j - 1)].position): object_on_map})

    def __add_random__(self):
        for i in range(self.size, 0, -1):
            random_object = random.choice([Water((i,10)), Water((i,10)), Water((i,10)), Food((i,10)), Stick((i,10)), Obstacle((i,10))])
            self.objects_on_map.update({(i, 1): random_object})

    def __find_empty_position_for_raft__(self):
        return random.choice([value.position for value in self.objects_on_map.values()
                              if value.type is 'water' and value.position[1] == self.size])

    def __find_empty_position_for_first_items__(self):
        return random.choice([value.position for value in self.objects_on_map.values()
                              if value.type is 'water' and value.position[1] < self.size])

    def __find_empty_position__(self):
        return random.choice([value.position for value in self.objects_on_map.values()
                              if value.type is 'water' and value.position[1] == 1])

    def __find_raft__(self):
        return [value for value in self.objects_on_map.values() if
                value.type == 'raft_and_human'][0]

    def __create_empty_map__(self):

        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                self.add_object_to_map(Water((x, y)))
