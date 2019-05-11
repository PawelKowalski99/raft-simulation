from reader_class import Reader
from world_class import World

if __name__ == "__main__":

    reader = Reader('initial_data.txt')

    world = World(reader.size)
    world.initialize(reader)

    while True:
        # world.map.show_objects()
        world.map.show_map()
        world.simulate()



        if not world.round.count < 20:
              break
