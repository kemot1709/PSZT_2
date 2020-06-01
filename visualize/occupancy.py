import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from network.get_data import *


def plot_occupancy(fig_occupancy, linklist, title=""):
    if type(fig_occupancy) != matplotlib.figure.Figure:
        fig_occupancy = plt.figure(figsize=(19.8, 10.8), dpi=100)
    else:
        plt.figure(fig_occupancy)

    bar_nr = len(linklist)
    width = 0.4

    i = 0
    plt.subplot(2, 1, 1)
    for link in linklist:
        if i == bar_nr / 2:
            plt.subplot(2, 1, 2)
            i = 0
        column1 = plt.bar(i - width / 2, linklist[link].occupancy, width, color="#0000FF")
        column2 = plt.bar(i + width / 2, linklist[link].pheromone, width, color="#FF0000")
        i += 1

    plt.suptitle(title)
    plt.show()


def plot_map(map_occupancy, city_list, linklist, title=""):
    if type(map_occupancy) != matplotlib.figure.Figure:
        map_occupancy = plt.figure(figsize=(19.8, 10.8), dpi=100)
    else:
        plt.figure(map_occupancy)

    # Plot points
    for city in city_list:
        plt.plot(city_list[city].x, city_list[city].y, 'bo')
        plt.text(city_list[city].x + 0.1, city_list[city].y + 0.1, city, fontsize=9)

    # Plot links
    for link in linklist:
        kolor = (linklist[link].occupancy / linklist[link].capacity)
        kolor = (1 - kolor, kolor, 0)
        width = linklist[link].pheromone / 10

        plt.plot([city_list[linklist[link].source].x - 0.1, city_list[linklist[link].target].x + 0.1],
                 [city_list[linklist[link].source].y + 0.1, city_list[linklist[link].target].y - 0.1], color=kolor,
                 linewidth=width)

    plt.suptitle(title)
    plt.show()
