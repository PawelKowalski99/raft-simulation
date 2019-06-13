from classes.simulation_class import Simulation

if __name__ == "__main__":
    world = Simulation()
    world.initialize()

    while True:
        print(world.round.count, 'Round count')
        # world.map.show_objects()
#        world.board.show_map()
        try:
            world.simulate()
        except IndexError:
            break
