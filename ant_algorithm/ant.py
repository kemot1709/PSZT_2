import sys

from network.get_data import *


class Ant:
    def __init__(self, actual_city):
        # self.ID = ID
        self.distance = 0
        self.track = {}
        self.actual_city = actual_city


def add_Ant(start):
    ant = Ant(start)
    return ant


def move_Ant(ant, link):
    ant.distance += link.cost
    ant.track[link.uid] = link
    ant.actual_city = link.target
    link.occupancy += 1


def get_actual_city(ant):
    return ant.actual_city


def check_propriety_target(ant, link):
    for walked in ant.track:
        if walked == link.uid:
            return 0
    return 1
