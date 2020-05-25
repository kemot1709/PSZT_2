from network.get_data import *

import math
import random


def select_target(source):
    probability = []
    for link in source.linklist:
        probability[link.uid] = link.pheromone + 1/link.cost

    prob_sum = math.fsum(probability)
    rand = random.uniform(0, prob_sum)

    for link in source.linklist:
        if rand < probability[link.uid]:
            return link
        rand -= probability[link.uid]

    print('Algorithm.py/select_target: no link probability')
    return link
