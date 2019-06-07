from abc import ABC

from enities.water_class import WaterField


class BoardDataAbstract(ABC):

    def __init__(self, size):
        self.size = size
        self.objects_on_board = {}

    def add_object_to_map(self, map_object):
        self.objects_on_board[map_object.position] = map_object

    def remove_object_from_map(self, map_object):
        self.objects_on_board[map_object.position] = WaterField(map_object.position)