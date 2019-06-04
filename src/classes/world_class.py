from classes.round_class import Round
from classes.map.board_class import Board


class World:

    def __init__(self, size):
        self.round = Round()
        self.map = Board(size)

    def initialize(self, reader):
        self.map.initialize(reader)

    def simulate(self):
        raft_and_human = self.map.__find_raft__()
        self.round.run()
        raft_and_human.simulation(self.map)
        self.map.move()
