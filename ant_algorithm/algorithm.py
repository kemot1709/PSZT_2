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

    # TODO zabijać jak nie ma żadnego wyboru

    print('Algorithm.py/select_target: no link probability')
    return link


def update_pheromone(ant):
    # stara formuła
    # for link in ant.track:
    #     ant.track[link].pheromone += 1 * ant.track[link].cost / ant.distance

    cities = 0
    for i in ant.track:
        cities += 1

    for link in ant.track:
        ant.track[link].pheromone += 1 / cities
