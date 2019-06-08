from classes.reader_class import Reader
from classes.writer_class import Writer
from classes.simulation_class import Simulation

if __name__ == "__main__":
    reader = Reader('initial_data.txt')
    writer = Writer()
    world = Simulation(reader.size)
    world.initialize(reader)

    while True:
        print(world.round.count, 'Round count')
        # world.map.show_objects()
        world.board.show_map()
        try:
            world.simulate()
            writer.write_to_csv(world.board)
        except IndexError:
            break
