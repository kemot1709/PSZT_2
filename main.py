import sys
import string
import os
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
            # TODO
            print("Not implemented")
            demand = demandlist["D" + str(demand_number)]  # Rozwiązanie chwilowe

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

    map_occupancy = plot_map(0, nodemap, linklist)
    anthill = []
    start = time.time()
    for i in range(generations):
        print("\t", math.floor(i / generations * 100), "%", end="\r")

        # # Delete best link
        # if i % 200 == 0 and i > 0:
        #     pom = 0
        #     li = 0
        #     for link in linklist:
        #         if linklist[link].pheromone > pom:
        #             pom = linklist[link].pheromone
        #             li = link
        #     del linklist[li]

        # Create new ants
        for j in range(demand.demandValue):
            anthill.append(add_Ant(demand.source))

        # Clear roads
        for link in linklist:
            linklist[link].occupancy = 0

        # Sent ants to journey
        for ant in anthill:
            target = select_target(nodemap[get_actual_city(ant)])
            if check_propriety_target(ant, target):
                move_Ant(ant, target)
            else:
                anthill.remove(ant)

        # Check for destination and update pheromone
        for ant in anthill:
            if get_actual_city(ant) == demand.destination:
                update_pheromone(ant)
                anthill.remove(ant)
                # TODO Czasami, w sumie nawet dość często mrówka nie jest zabijana lub wykrywana jak dojdzie do celu
                # i nie potrafię tego namierzyć

        for link in linklist:
            linklist[link].pheromone = pheromone_resistance * linklist[link].pheromone
            if linklist[link].pheromone < pheromone_min:
                linklist[link].pheromone = pheromone_min

        # plot actual state of roads
        map_occupancy = plot_map(map_occupancy, nodemap, linklist)

    stop = time.time()
    print("\t", "100%", end='\r')

    # TODO jakieś statystyki

    print("Complete, calculation time: ", datetime.timedelta(seconds=(stop - start)))
