import random
from empty_object_class import EmptyObjectAbstract
from RaftOrHumanSimulationAbstract import RaftOrHumanSimulationAbstract


class RaftAndHuman(EmptyObjectAbstract):

    def __init__(self, position):
        super(RaftAndHuman, self).__init__(position)
        self.raft = Raft()
        self.human = Human()
        self.type = 'raft_and_human'
        self.symbol = 'R'

    def get_end_position(self, board):
        try:
            if board.objects_on_board[(self.position[0] + 1, self.position[1] - 1)] not in board.objects_on_board or \
                    board.objects_on_board[(self.position[0] - 1, self.position[1] - 1)] not in board.objects_on_board:
                if board.objects_on_board[(self.position[0], self.position[1] - 1)].type == "obstacle" and \
                     board.objects_on_board[(self.position[0] + 1, self.position[1] - 1)] != "obstacle":
                    return board.objects_on_board[(self.position[0] + 1, self.position[1])].position
                elif board.objects_on_board[(self.position[0], self.position[1] - 1)].type == "obstacle" and \
                     board.objects_on_board[(self.position[0] - 1, self.position[1] - 1)] != "obstacle":
                    return board.objects_on_board[(self.position[0] - 1, self.position[1])].position

            if board.objects_on_board[(self.position[0] + 1, self.position[1] - 1)] in board.objects_on_board or \
               board.objects_on_board[(self.position[0] - 1, self.position[1] - 1)] in board.objects_on_board:
                if board.objects_on_board[(self.position[0], self.position[1] - 1)].type != "obstacle" and \
                      (board.objects_on_board[(self.position[0] + 1, self.position[1] - 1)].type == "obstacle" and
                        board.objects_on_board[(self.position[0] - 1, self.position[1] - 1)].type) == "obstacle":
                    return self.position

                elif board.objects_on_board[(self.position[0], self.position[1] - 1)].type == "obstacle" and \
                        board.objects_on_board[(self.position[0] + 1, self.position[1] - 1)] is None:
                    print(board.objects_on_board[(self.position[0] + 1, self.position[1] - 1)])
                    return self.position

            elif self.human.effect_status:
                foods = sorted(board.get_food(),
                               key=lambda food:
                               self.position[0] - food.position[0] + self.position[1] - food.position[1])
                if foods:
                    print(foods[0].position)
                    if board.objects_on_board[(self.position[0] - 1, self.position[1] - 1)].type is not "obstacle":
                        return foods[0].position
                elif not foods:
                    return None
        except AttributeError:
            pass

    def simulation(self, board):
        self.__get_to_inv__()
        self.human.simulation()
        self.raft.simulation()

        if self.raft.inventory['food'] and self.human.effect_status is True:
            self.human.effect_value += self.raft.inventory['food'][0].wholesomeness
            self.raft.inventory['food'].pop(0)
        if self.raft.inventory['stick'] and self.raft.effect_value < 40:
            self.raft.effect_value += self.raft.inventory['stick'][0].effect_object_value
            self.raft.inventory['stick'].pop(0)
        if self.human.is_gone or self.raft.is_gone:
            del self.human
            board.remove_object_from_map(self)

        #if self.human._is_hungry:
            #food_in_inv = [object for object in self.raft.inventory if object.type == 'food']
           # if food_in_inv:
                #self.human += food_in_inv[0].effect_status
                #del food_in_inv[0]

    def __get_to_inv__(self):
        pass


class Raft(RaftOrHumanSimulationAbstract):

    def __init__(self):
        super(Raft, self).__init__()
        self.inv_slots = random.randint(5, 10)
        self.inventory = {
            "stick": [],
            "food": [],
        }

    def add_to_inventory(self):
        pass

    def simulation(self):
        super(Raft, self).simulation()


class Human(RaftOrHumanSimulationAbstract):

    def __init__(self):
        super(Human, self).__init__()

    def simulation(self):
        super(Human, self).simulation()

    def eat(self):
        pass
