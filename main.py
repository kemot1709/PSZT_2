import datetime
import time
import math

from opt.opt_parser import *
from opt.opt_config import *

from network.get_data import *

from ant_algorithm.ant import *
from ant_algorithm.algorithm import *

from visualize.occupancy import *


if __name__ == "__main__":
    parser = OptParser(get_opt_config())
    parsedOptions = parser.parse(sys.argv[1:])
    print("Perform ant algorithm with given options:\n", parsedOptions)

    # Assign parsed options to variables
    generations = parsedOptions["generations"]
    pheromone_min = parsedOptions["ph_min"]
    pheromone_resistance = parsedOptions["ph_res"]
    demand_number = parsedOptions["demand"]
    flag_delete = parsedOptions["elimination"]

    source = parsedOptions["source"]
    target = parsedOptions["target"]
    requirement = parsedOptions["requirement"]

    # Get data from file
    nodemap, linklist, demandlist = get_data('network/usa.xml')

    # Select demand
    if demand_number >= 0:
        demand = demandlist["D" + str(demand_number)]
    else:
        if source == '' or target == '':
            demand = random.choice(list(demandlist.values()))
        else:
            flag_s = 0
            flag_t = 0
            for city in nodemap:
                if city == source:
                    flag_s = 1

                if city == target:
                    flag_t = 1
            if flag_s and flag_t:
                demand = Demand("D___", source, target, requirement)
            else:
                print('Wrong city passed, taking random demand')
                demand = random.choice(list(demandlist.values()))

    # Check if we can satisfy demand
    cap_source = 0
    cap_target = 0
    for link in nodemap[demand.source].linklist:
        cap_source += link.capacity
    for link in nodemap[demand.destination].linklist:
        cap_target += link.capacity
    demand.demandValue = min(demand.demandValue, cap_source, cap_target)

    # Info about searched path
    print("From ", demand.source, " to ", demand.destination, " with demand ", demand.demandValue)

    # Start searching
    map_occupancy = plot_map(0, nodemap, linklist)
    anthill = []
    start = time.time()
    for i in range(generations):
        print("\t", math.floor(i / generations * 100), "%", end="\r")

        # Delete best link and make algorithm interesting
        if flag_delete:
            if i % int(generations / 4) == 0 and i > 0:
                delete_best_option(linklist, map_occupancy)

        # Create new ants
        for j in range(demand.demandValue):
            anthill.append(add_Ant(demand.source))

        # Clear roads
        for link in linklist:
            linklist[link].occupancy = 0

        # Sent ants to journey
        send_ants(anthill, nodemap)

        # Check for destination and update pheromone
        check_reaching_target(anthill, demand)

        # Update amount of pheromone on tracks
        evaporate_pheromone(linklist, pheromone_resistance, pheromone_min)

        # Plot actual state of roads
        map_occupancy = plot_map(map_occupancy, nodemap, linklist)

    stop = time.time()
    print("\t", "100%", end='\r')

    # Summary
    plt.figure(map_occupancy.number)
    plt.show()

    print("Complete, calculation time: ", datetime.timedelta(seconds=(stop - start)))
