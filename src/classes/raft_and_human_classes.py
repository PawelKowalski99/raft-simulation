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

    def get_end_position(self, map):
        try:
            if map.objects_on_map[(self.position[0], self.position[1] - 1)].type == "obstacle" and \
            not (map.objects_on_map[(self.position[0] + 1, self.position[1] - 1)].type or
                 map.objects_on_map[(self.position[0] - 1, self.position[1] - 1)].type) == "obstacle":
                return None
            elif self.human._is_hungry:
                foods = sorted(map.get_food(), key=lambda food: self.position[0] - food.position[0] + self.position[1] - food.position[1])
                print(foods)
                if foods:
                    return foods[0].position
                elif not foods:
                    return None
        except:
            pass

    def simulation(self, map):
        self.__get_to_inv__()
        self.human.human_simulation()
        self.raft.raft_simulation()

        if self.raft.inventory['food'] and self.human._is_hungry is True:
            self.human._hungry_status += self.raft.inventory['food'][0].wholesomeness
            self.raft.inventory['food'].pop(0)
        if self.raft.inventory['stick'] and self.raft._durability < 40:
            self.raft._durability += self.raft.inventory['stick'][0].effect_status
            self.raft.inventory['food'].pop(0)
        if self.human is None:
            del self.human
            map.remove_object_from_map(self)
        #if self.human._is_hungry:
            #food_in_inv = [object for object in self.raft.inventory if object.type == 'food']
           # if food_in_inv:
                #self.human += food_in_inv[0].effect_status
                #del food_in_inv[0]

    def __get_to_inv__(self):
        pass


class Raft:

    def __init__(self):
        self.__inv_slots = random.randint(5, 10)
        self.inventory = {
            "stick": [],
            "food": [],
        }
        self._durability = random.randint(60, 101)

    def add_to_inventory(self):
        pass

    def raft_simulation(self):
        self._durability -= 5


class Human:

    def __init__(self):
        self._is_hungry = False
        self._hungry_status = random.randint(60, 101)

    def human_simulation(self):
        self._hungry_status -= 5
        print(self._hungry_status)
        if self._hungry_status < 0:
            del self

        elif self._hungry_status <= 40:
            self._is_hungry = True
        elif self._hungry_status >= 80:
            self._is_hungry = False

    def eat(self):
        pass
