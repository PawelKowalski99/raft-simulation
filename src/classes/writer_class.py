import csv
import os
from classes.round_class import Round


class Writer:
    """
    Class that writes information about every round in the program
    """
    round_count = 0
    food_count = 0
    stick_count = 0
    obstacle_count = 0

    def __init__(self):
        """
        Initialization function that deletes csv file if it exists.
        """
        self.remove_csv_file()

    def remove_csv_file(self):
        """
        Removes csv file in folder
        """
        os.remove('results.csv')

    def write_to_csv(self, board):
        """
        It writes information about exact round to the csv file by appends mode
        :param Board board: Is used to get information from board
        """
        round_count = Round.count
        food_count = len(board.get_thing('food'))
        stick_count = len(board.get_thing('stick'))
        obstacle_count = len(board.get_thing('obstacle'))

        with open('results.csv', mode='a') as result_file:
            result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            result_writer.writerow([
                round_count,
                food_count, stick_count, obstacle_count,
            ])
