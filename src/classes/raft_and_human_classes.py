import random
from empty_object_class import EmptyObjectAbstract
from water_class import Water
from Food_class import Food


class RaftAndHuman(EmptyObjectAbstract):

    def __init__(self, position):
        super(RaftAndHuman, self).__init__(position)
        self.raft = Raft()
        self.human = Human()
        self.type = 'raft_and_human'
        self.symbol = 'R'

    def move(self, end_position):
        if end_position is None:
            return False

        previous_position = self.position
        if self.position[0] - end_position[0] > 0 and \
                not map.objects_on_map[(self.position[0] - 1, self.position[1])].is_animal:
            self.position = (self.position[0] - 1, self.position[1])
            map.objects_on_map(self)

        elif self.position[0] - end_position[0] < 0 and \
                not map.objects_on_map[(self.position[0] + 1, self.position[1])].is_animal:
            self.position = (self.position[0] + 1, self.position[1])
            map.objects_on_map(self)

        map.objects_on_map(Water(previous_position))

    def get_end_position(self, map):
        if map.objects_on_map[(self.position[0], self.position[1] - 1)].type == "obstacle" and \
            not (map.objects_on_map[(self.position[0] + 1, self.position[1] - 1)].type or
                 map.objects_on_map[(self.position[0] - 1, self.position[1] - 1)].type) == "obstacle":
            return None
        elif self.human._is_hungry:
            foods = sorted(map.get_food(), key=lambda food: self.position[0] - food.position[0] + self.position[1] - food.position[1])
            print(foods)
            return foods[0].position

    def simulation(self, map):
        self.__get_to_inv__()

        self.human.human_simulation()
        if self.human is None:
            map.remove_object_from_map(self)
        if self.human._is_hungry:
            food_in_inv = [object for object in self.raft.inventory if object.type == 'food']
            if food_in_inv:
                self.human += food_in_inv[0].effect_status
                del food_in_inv[0]

    def __get_to_inv__(self):
        

class Raft:

    def __init__(self):
        self.__inv_slots = random.randint(5, 10)
        self.inventory = []

    def add_to_inventory(self):
        pass


class Human:

    def __init__(self):
        self._is_hungry = False
        self.__hungry_status = random.randint(60, 101)

    def human_simulation(self):
        self.__hungry_status -= 5
        print(self.__hungry_status)
        if self.__hungry_status < 0:
            del self

        elif self.__hungry_status <= 40:
            self._is_hungry = True
        elif self.__hungry_status >= 80:
            self._is_hungry = False

    def eat(self):
        pass
