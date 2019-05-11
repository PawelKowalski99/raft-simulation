import csv


class Reader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.size = None
        self.number_of_food = None
        self.number_of_wood = None
        self.number_of_cbstacles = None
        self.__read__()

    def __read__(self):

        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.size = int(row[0])
                self.number_of_food = int(row[1])
                self.number_of_wood = int(row[2])
                self.number_of_cbstacles = int(row[3])
