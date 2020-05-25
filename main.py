import sys
import string
import os

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
    generations = 10000
    demand_number = "D452"

    nodemap, linklist, demandlist = get_data('network/usa.xml')

    # Select demand
    # D452
    demand = demandlist[demand_number]

    # Check if we can satisfy demand

    fig_occupancy = plot_occupancy(0, linklist)
    anthill = []
    for i in range(generations):
        # Create new ants
        for j in range(demand.demandValue):
            anthill.append(add_Ant(demand.source))

        # Clear roads
        for link in linklist:
            linklist[link].occupancy = 0

        # Sent ants to journey
        for ant in anthill:
            target = select_target(nodemap[get_actual_city(ant)])
            move_Ant(ant, target)

        # plot actual state of roads
        fig_occupancy = plot_occupancy(fig_occupancy, linklist)

        # Check for destination and update pheromone
        for ant in anthill:
            if get_actual_city(ant) == demand.destination:
                # TODO update pheromone
                # TODO delete ant
                continue

    print("OK")
