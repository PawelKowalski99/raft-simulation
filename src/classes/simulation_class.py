from classes.round_class import Round
from classes.board_class import Board


class Simulation:
    """
    This class stores information about round and board
    """

    def __init__(self, size):
        """
        Inizilatization method for simulation.
        :param int size: Size of board
        """
        self.round = Round()
        self.board = Board(size)

    def initialize(self, reader):
        """
        Initialize board
        :param Reader reader: Initialization information about amount of objects on board (2D map)
        """
        self.board.initialize(reader)

    def simulate(self):
        """
        Simulation of behaviour of different objects on map every round
        """
        raft_and_human = self.board.__find_raft__()
        self.round.run()
        raft_and_human.simulation(self.board)
        self.board.move()
