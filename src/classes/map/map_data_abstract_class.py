from abc import ABC

from water_class import Water


class MapDataAbstract(ABC):

    def __init__(self, size):
        self.size = size
        self.objects_on_map = {}

    def add_object_to_map(self, map_object):
        self.objects_on_map[map_object.position] = map_object

    def remove_object_from_map(self, map_object):
        self.objects_on_map[map_object.position] = Water(map_object.position)