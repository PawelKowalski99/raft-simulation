import csv


class Reader:
    """
    Holds information about inital data and is used for initialization of board
    """
    def __init__(self, file_name):
        """
        Initialization of Reader variables.
        :param string file_name: .csv file with suffix size, number_of_food, number_of_stick, number_of_obstacles
        """
        self.file_name = file_name
        self.size = None
        self.number_of_food = None
        self.number_of_stick = None
        self.number_of_cbstacles = None
        self.__read__()

    def __read__(self):
        """
        Reads information from .csv and set variables
        """
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.size = int(row[0])
                self.number_of_food = int(row[1])
                self.number_of_stick = int(row[2])
                self.number_of_cbstacles = int(row[3])
