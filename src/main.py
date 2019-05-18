from reader_class import Reader
from world_class import World
from raft_and_human_classes import RaftAndHuman

if __name__ == "__main__":
    # action_queue = []
    reader = Reader('initial_data.txt')

    world = World(reader.size)
    world.initialize(reader)

    while True:
        print(world.round.count)
        # world.map.show_objects()
        world.map.show_map()
        try:
            world.simulate()
        except IndexError:
            break


        # if isinstance(any(world.map.objects_on_map.values()), RaftAndHuman):
        #     break
        # if not world.round.count < 100:
        #       break
