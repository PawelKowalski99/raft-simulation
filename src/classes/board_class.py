import random
from classes.entities.Food_class import Food
from classes.entities.obstacle_class import Obstacle
from classes.raft.raft_and_human_classes import RaftAndHuman
from classes.entities.stick_class import Stick
from classes.entities.water_class import WaterField


class Board:
    """
    Holds information about objects and makes operations on them
    """
    def __init__(self, size):
        self.size = size
        self.objects_on_board = {}

    def initialize(self, reader):
        """
        Initialize new map using given info from .csv. Adds objects to board.
        :param Reader reader: informations about amount of specific objects that are to be added to board
        """
        self.__create_empty_map__()

        self.add_object_to_map(RaftAndHuman(self.__find_empty_position_for_raft__()))
        for _ in range(reader.number_of_food):
            self.add_object_to_map(Food(self.__find_empty_position_for_first_items__()))

        for _ in range(reader.number_of_stick):
            self.add_object_to_map(Stick(self.__find_empty_position_for_first_items__()))

        for _ in range(reader.number_of_cbstacles):
            self.add_object_to_map(Obstacle(self.__find_empty_position_for_first_items__()))

    def add_object_to_map(self, map_object):
        """
        Add object to map
        :param EntityAbstract map_object: an object that is to be added to board
        """
        self.objects_on_board[map_object.position] = map_object

    def remove_object_from_map(self, map_object):
        """
        Remove object from map
        :param EntityAbstract map_object: an object that is to be removed from board
        """
        self.objects_on_board[map_object.position] = WaterField(map_object.position)

    def move(self):
        """
        Collection of private methods responsible of movement of objects on board.
        """
        self.__move_raft__()
        self.__move_map_down__()
        self.__add_random__()

    def show_map(self):
        """
        Visualizing board on console
        """
        for y in range(1, self.size + 1):
            object_list = []
            i = 0
            for x in range(1, self.size + 1):
                object_list.append(self.objects_on_board[(x, y)].symbol)
                i += 1
                if i == self.size:
                    print(object_list)
        print(self.size * 5 * "-")

    def get_thing(self, kind):
        """
        Get list of objects of given type
        :param string kind: Type of object to filter of
        :return: list of objects on board of given type
        """
        return [object_on_map for object_on_map in self.objects_on_board.values() if
                object_on_map.type is kind]

    def __move_raft__(self):
        """
        Movement of raft in horizontal
        """
        raft = self.__find_raft__()
        end_position = raft.get_end_position(self)

        if end_position is None:
            return None

        previous_position = raft.position
        if raft.position[0] - end_position[0] > 0 and \
                self.objects_on_board[(raft.position[0] - 1, raft.position[1])].type == 'water':
            raft.position = (raft.position[0] - 1, raft.position[1])
            self.add_object_to_map(raft)
            self.objects_on_board[previous_position] = WaterField(previous_position)

        elif raft.position[0] - end_position[0] < 0 and \
                self.objects_on_board[(raft.position[0] + 1, raft.position[1])].type == 'water':
            raft.position = (raft.position[0] + 1, raft.position[1])
            self.add_object_to_map(raft)
            self.objects_on_board[previous_position] = WaterField(previous_position)

    def __move_map_down__(self):
        """
        Movement of map down
        """
        raft = self.__find_raft__().raft
        raft_inv = raft.inventory
        for i in range(self.size, 0, -1):
            for j in range(self.size - 1, 0, -1):
                if self.objects_on_board[(i, j + 1)].type is not "raft_and_human":
                    object_on_map = self.objects_on_board[(i, j)]
                    object_on_map.position = (i, j + 1)
                    self.objects_on_board.update({object_on_map.position: object_on_map})

                elif self.objects_on_board[(i, j + 1)].type is "raft_and_human" and \
                        len(raft_inv['stick']) + len(raft_inv['food']) < self.__find_raft__().raft.inv_slots:

                    if self.objects_on_board[(i, j)].type is "obstacle":
                        self.__find_raft__().raft.effect_value -= self.objects_on_board[(i, j)].effect_value

                    elif self.objects_on_board[(i, j)].type is "food" or 'stick':
                        raft.add_to_inventory(self.objects_on_board[(i, j)])

                    self.objects_on_board[(i, j - 1)].position = (i, j)
                    object_on_map = self.objects_on_board[(i, j - 1)]
                    self.objects_on_board.update({self.objects_on_board[(i, j - 1)].position: object_on_map})

    def __find_raft__(self):
        """
        Find raft on board
        :return HumanAndRaft: Object which represents human and raft on board
        """
        return [value for value in self.objects_on_board.values() if
                value.type == 'raft_and_human'][0]

    def __add_random__(self):
        """
        Randomly generate first row of map in order to fulfill first row with new objects
        Chances of creating Water field is 50%, Food 17%, Stick 17%, Obstacle 17%
        """
        for i in range(self.size, 0, -1):
            random_object = random.choice([WaterField((i, 1)), WaterField((i, 1)),
                                           WaterField((i, 1)), Food((i, 1)),
                                           Stick((i, 1)), Obstacle((i, 1))])
            self.add_object_to_map(random_object)

    def __find_empty_position_for_raft__(self):
        """
        FInd empty position for placing raft in the initialization phase.
        :return (int, int): position of x and y
        """
        return random.choice([value.position for value in self.objects_on_board.values()
                              if value.type is 'water' and value.position[1] == self.size])

    def __find_empty_position_for_first_items__(self):
        """
        Find empty positions for placing effect objects on board in the initialization phase.
        Finds positions in every row except the last one for objects.
        :return: (int, int): position of x and y
        """
        return random.choice([value.position for value in self.objects_on_board.values()
                              if value.type is 'water' and value.position[1] < self.size])

    def __create_empty_map__(self):
        """
        Creates board with only WaterFields.
        In next phase it is fulfilled with random number of effect object
        """
        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                self.add_object_to_map(WaterField((x, y)))
