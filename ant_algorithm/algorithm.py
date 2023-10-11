import math
import random
import matplotlib
import matplotlib.pyplot as plt

from network.get_data import *
from ant_algorithm.ant import *


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

    # Return 0 and kill ant if it cant move further
    return 0


def update_pheromone(ant, multiplier):
    cities = 0
    for i in ant.track:
        cities += 1

    for link in ant.track:
        ant.track[link].pheromone += multiplier / ant.distance


def delete_best_option(linklist, map_occupancy):
    pom = 0
    li = 0
    # plt.figure(map_occupancy.number)
    # plt.show()
    for link in linklist:
        if linklist[link].pheromone > pom:
            pom = linklist[link].pheromone
            li = link
    del linklist[li]


def send_ants(anthill, nodemap):
    killed = 0
    for ant in anthill:
        target = select_target(nodemap[get_actual_city(ant)])
        if check_propriety_target(ant, target):
            move_Ant(ant, target)
        else:
            anthill.remove(ant)
            killed += 1

    return killed


def check_reaching_target(anthill, demand):
    killed = 0
    for ant in anthill:
        if get_actual_city(ant) == demand.destination:
            # TODO to 1000 jest trochę broken przy krótkich trasach, trzeba to naprawić i uzależnić od długości trasy
            update_pheromone(ant, 1000)
            anthill.remove(ant)
            killed += 1
            # TODO Czasami, w sumie nawet dość często mrówka nie jest zabijana lub wykrywana jak dojdzie do celu
            # i nie potrafię tego namierzyć i wyeliminować

    return killed


def evaporate_pheromone(linklist, pheromone_resistance, pheromone_min):
    for link in linklist:
        linklist[link].pheromone = pheromone_resistance * linklist[link].pheromone
        if linklist[link].pheromone < pheromone_min:
            linklist[link].pheromone = pheromone_min
