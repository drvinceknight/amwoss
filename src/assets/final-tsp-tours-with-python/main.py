from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics.pairwise
import sympy as sym

def plot_tour(ax, x, y, tour):
        xs = x[tour]
        ys = y[tour]
        ax.quiver(xs[:-1], ys[:-1], xs[1:]-xs[:-1], ys[1:]-ys[:-1], scale_units='xy', angles='xy', scale=2)
        ax.plot(xs, ys)

        for i, (x, y) in enumerate(zip(xs[:-1], ys[:-1])):
            ax.annotate(str(i), (x, y), backgroundcolor="grey", fontsize='xx-small')

seed = 1
number_of_stops = 13
np.random.seed(seed)
xs = np.random.randint(0, 100, number_of_stops)
ys = np.random.randint(0, 100, number_of_stops)

initial_candidate = [0, 9, 4, 7, 1, 2, 5, 3, 8, 6, 11, 12, 10, 0]
swap_stops_solution = [0, 7, 2, 8, 5, 3, 1, 9, 12, 11, 4, 10, 6, 0]
swap_paths_solution = [0, 8, 5, 3, 1, 9, 12, 11, 4, 10, 6, 2, 7, 0]

# Draw plot
fig, axarr = plt.subplots(1, 3, figsize=(15, 4))
plot_tour(ax=axarr[0], x=xs, y=ys, tour=initial_candidate)
axarr[0].set_title("Initial candidate")

plot_tour(ax=axarr[1], x=xs, y=ys, tour=swap_stops_solution)
axarr[1].set_title("Swapping stops after 1000 iterations")

plot_tour(ax=axarr[2], x=xs, y=ys, tour=swap_paths_solution)
axarr[2].set_title("Reversing path after 1000 iterations")

plt.tight_layout()
plt.savefig("main.pdf")
