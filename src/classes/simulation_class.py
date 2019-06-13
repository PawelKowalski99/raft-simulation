from classes.round_class import Round
from classes.board_class import Board


class Simulation:
    """
    This class stores information about round and board
    """

    def __init__(self):
        """
        Inizilatization method for simulation.
        """
        self.round = Round()
        self.board = Board()

    def initialize(self):
        """
        Initialize board
        """
        self.board.initialize()

    def simulate(self):
        """
        Simulation of behaviour of different objects on map every round
        """
        raft_and_human = self.board.__find_raft__()
        self.round.run()
        raft_and_human.simulation(self.board)
        self.board.move()
        self.board.writer.write_to_csv()
