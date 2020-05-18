import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def plot_occupancy(fig_occupancy, linklist, title="OK"):
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
