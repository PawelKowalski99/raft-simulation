import random
from classes.entities.entity_abstract_class import EntityAbstract
from classes.raft.DamagableAbstract import DamagableAbstract


class RaftAndHuman(EntityAbstract):
    """
    Class created for composing human and raft as a one object on map
    """
    type = 'raft_and_human'
    symbol = 'R'

    def __init__(self, position):
        """
        Initialization of object
        :param (int, int) position: Position x, y given as int 0<x<board.size; 0<y<board.size
        """
        super(RaftAndHuman, self).__init__(position)
        self.raft = Raft()
        self.human = Human()

    def get_end_position(self, board):
        """
        Needed for choosing correct position to move on board
        :param Board board: The place where RaftAndHuman moves
        :return: position where to move (int, int)
        """
        try:
            if (self.position[0] + 1, self.position[1] - 1) not in board.objects_on_board or \
                    (self.position[0] - 1, self.position[1] - 1) not in board.objects_on_board:
                if board.objects_on_board[(self.position[0], self.position[1] - 1)].type == "obstacle" and \
                        (self.position[0] + 1, self.position[1] - 1) not in board.objects_on_board:
                    return board.objects_on_board[(self.position[0] - 1, self.position[1])].position
                elif board.objects_on_board[(self.position[0], self.position[1] - 1)].type == "obstacle" and \
                        (self.position[0] - 1, self.position[1] - 1) not in board.objects_on_board:
                    return board.objects_on_board[(self.position[0] + 1, self.position[1])].position
            # [W][O][X]   or   [X][O][W]
            # [W][R][X]        [X][R][W]

            elif (self.position[0] + 1, self.position[1] - 1) in board.objects_on_board and \
                    (self.position[0] - 1, self.position[1] - 1) in board.objects_on_board:

                if board.objects_on_board[(self.position[0], self.position[1] - 1)].type == "obstacle":
                    if board.objects_on_board[(self.position[0] - 1, self.position[1] - 1)].type == "obstacle":
                        return self.position[0] + 1, self.position[1] - 1
                    elif board.objects_on_board[(self.position[0] + 1, self.position[1] - 1)].type == "obstacle":
                        return self.position[0] - 1, self.position[1] - 1
                    else:
                        return random.choice([(self.position[0] + 1, self.position[1] - 1),
                                              (self.position[0] - 1, self.position[1] - 1)])

            if self.human.effect_status:
                foods = sorted(board.get_thing("food"),
                               key=lambda food:
                               self.position[0] - food.position[0] + self.position[1] - food.position[1])
                if foods:
                    print(foods[0].position, 'next goal is food')
                    return foods[0].position
                elif not foods:
                    return self.position
            elif self.raft.effect_status:
                sticks = sorted(board.get_thing("stick"),
                                key=lambda stick:
                                self.position[0] - stick.position[0] + self.position[1] - stick.position[1])
                if sticks:
                    print(sticks[0].position, 'next goal is stick')
                    return sticks[0].position
                elif not sticks:
                    return self.position
            else:
                return self.position

        except AttributeError:
            pass

    def simulation(self, board):
        """
        Simulation of behaviour of RaftAndHuman on board
        If human is hungry (effect_status = True), it is eating.
        If raft is damaged (effect_status = True), it is being fixed.
        :param Board board: The place where RaftAndHuman moves
        """
        self.human.simulate_damage()
        self.raft.simulate_damage()

        if self.raft.inventory['food'] and self.human.effect_status is True:
            self.human.effect_value += self.raft.inventory['food'][0].effect_value
            self.raft.inventory['food'].pop(0)
        if self.raft.inventory['stick'] and self.raft.effect_status is True:
            self.raft.effect_value += self.raft.inventory['stick'][0].effect_value
            self.raft.inventory['stick'].pop(0)
        if self.human.is_gone or self.raft.is_gone:
            board.remove_object_from_map(self)

        for food in self.raft.inventory['food']:
            food.decomposition()
        # print(self.raft.inventory)

        # if self.human._is_hungry:
        # food_in_inv = [object for object in self.raft.inventory if object.type == 'food']
        # if food_in_inv:
        # self.human += food_in_inv[0].effect_status
        # del food_in_inv[0]


class Human(DamagableAbstract):
    """
    Representation of human on raft.
    It is an object which needs to survive as long as it can.
    """

    def __init__(self):
        """
        Initialization of human object.
        """
        super(Human, self).__init__()

    def simulate_damage(self):
        """
        Siumlation of human hunger.
        If human is hungry it changes its effect status to True, if not to False.
        """
        self.effect_value -= 4

        if self.effect_value < 0:
            self.is_gone = True
        elif self.effect_value <= 40:
            self.effect_status = True
        elif self.effect_value >= 60:
            self.effect_status = False
        print(self.effect_value, 'hunger value')


class Raft(DamagableAbstract):
    """
    Representation of raft on ocean.
    It is an object which helps human to survive.
    Every round its durability is decreased
    """

    def __init__(self):
        """
        Initialization of raft object
        """
        super(Raft, self).__init__()
        self.__inv_slots = random.randint(5, 10)
        self.inventory = {
            "stick": [],
            "food": [],
        }

    def add_to_inventory(self, item):
        """
        Adding items to raft inventory
        :param EffectEntityAbstract item: Food or Stick object
        """
        if item.type == "food" and \
                len(self.inventory['stick']) + len(self.inventory['food']) < self.__inv_slots:
            self.inventory["food"].append(item)
        elif item.type == "stick" and \
                len(self.inventory['stick']) + len(self.inventory['food']) < self.__inv_slots:
            self.inventory["stick"].append(item)

    def simulate_damage(self):
        """
        Simulation of usage of raft on ocean every round.
        """
        self.effect_value -= 2

        if self.effect_value < 0:
            self.is_gone = True
        elif self.effect_value <= 40:
            self.effect_status = True
        elif self.effect_value >= 60:
            self.effect_status = False

        print(self.effect_value, 'durability raft value')
