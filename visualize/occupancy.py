import matplotlib
import matplotlib.pyplot as plt

from network.get_data import *


# Old and not developed!!!
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
        map_occupancy = plt.figure(1, figsize=(19.8, 10.8), dpi=100)
    else:
        plt.figure(map_occupancy.number)
        plt.clf()

    # Get max of capacity
    capacity = 0
    for link in linklist:
        capacity = max(capacity, linklist[link].capacity)

    # Plot points
    for city in city_list:
        plt.plot(city_list[city].x, city_list[city].y, 'bo')
        plt.text(city_list[city].x + 0.1, city_list[city].y + 0.1, city, fontsize=9)

    # Plot links
    for link in linklist:
        if linklist[link].occupancy == 0:
            kolor = (0, 0, 1)
        else:
            kolor = (linklist[link].occupancy / capacity)
            if kolor > 1:
                print(kolor, capacity, linklist[link].occupancy)
                # TODO Czasami tu wchodzi choć nie powinien, bo ma ograniczenia wcześniej nałożone, trzeba to na
                #  którymś etapie naprawić
                # UPDATE chyba jest już OK, ale nie jestem pewny
                kolor = 1
            kolor = (1 - kolor, kolor, 0)
        width = max(0.1, linklist[link].pheromone / 10)

        plt.plot([city_list[linklist[link].source].x - 0.1, city_list[linklist[link].target].x + 0.1],
                 [city_list[linklist[link].source].y + 0.1, city_list[linklist[link].target].y - 0.1], color=kolor,
                 linewidth=width)

    plt.title(title)
    plt.draw()
    plt.pause(0.01)

    return map_occupancy
