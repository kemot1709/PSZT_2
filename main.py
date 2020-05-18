import sys
import string
import os

from opt.opt_parser import *
from opt.opt_config import *

from network.get_data import  *

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

    nodemap, linklist, demandlist = get_data('network/usa.xml')

    # Select demand
    # D452

    fig_occupancy = plot_occupancy(0, linklist)

    print("OK")
