from classes.reader_class import Reader
from classes.world_class import World
import time

if __name__ == "__main__":
    print(__name__)
    # action_queue = []
    reader = Reader('initial_data.txt')
    world = World(reader.size)
    world.initialize(reader)

    while True:
        print(world.round.count, 'Round count')
        # world.map.show_objects()
        world.map.show_map()
        try:
            world.simulate()
        except IndexError:
            break

        time.sleep(1)
        # if isinstance(any(world.map.objects_on_map.values()), RaftAndHuman):
        #     break
        # if not world.round.count < 100:
        #       break
