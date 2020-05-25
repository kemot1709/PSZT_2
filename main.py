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
    # function_type = FunctionType(parsedOptions["function"])
    # selection_type = SelectionType(parsedOptions["sel_type"])
    # replacement_type = ReplacementType(parsedOptions["rep_type"])
    # crossover_probability = parsedOptions["crossover_p"]
    # dimensions = parsedOptions["dimensions"]
    # iterations = parsedOptions["iterations"]
    # cardinality = parsedOptions["cardinality"]
    # attempts = parsedOptions["attempts"]
    # mut_range = parsedOptions["mut_sigma"]
    # x_min = parsedOptions["x_min"]
    # x_max = parsedOptions["x_max"]
    generations = 100
    demand_number = "D452"

    nodemap, linklist, demandlist = get_data('network/usa.xml')

    # Select demand
    # D452
    demand = demandlist[demand_number]

    # Check if we can satisfy demand

    fig_occupancy = plot_occupancy(0, linklist)
    anthill = []
    start = time.time()
    for i in range(generations):
        print("\t", math.floor(i / generations * 100), "%", end="\r")
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

        # plot actual state of roads
        fig_occupancy = plot_occupancy(fig_occupancy, linklist)

        # Check for destination and update pheromone
        for ant in anthill:
            if get_actual_city(ant) == demand.destination:
                update_pheromone(ant)
                anthill.remove(ant)

        # TODO zwietrz pheromone
        for link in linklist:
            linklist[link].pheromone = 0.9 * linklist[link].pheromone

    stop = time.time()
    print("\t", "100%", end='\r')

    # TODO jakieś statystyki

    print("Complete, calculation time: ", datetime.timedelta(seconds=(stop - start)))
