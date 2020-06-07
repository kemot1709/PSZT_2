from network.get_data import *

import math
import random


def select_target(source):
    probability = {}
    prob_sum = 0
    for link in source.linklist:
        if link.occupancy < link.capacity:
            probability[link.uid] = link.pheromone + 1 / link.cost
            prob_sum += probability[link.uid]
        else:
            probability[link.uid] = 0

    rand = random.uniform(0, prob_sum)

    for link in source.linklist:
        if rand < probability[link.uid]:
            return link
        rand -= probability[link.uid]

    # Return 0 and kill ant if it cant move
    return 0


def update_pheromone(ant):
    cities = 0
    for i in ant.track:
        cities += 1

    for link in ant.track:
        # TODO to 1000 jest trochę broken przy krótkich trasach, trzeba to naprawić
        ant.track[link].pheromone += 1000 / ant.distance
