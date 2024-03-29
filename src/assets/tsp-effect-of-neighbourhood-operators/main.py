from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics.pairwise
import sympy as sym

def plot_tour(ax, x, y, tour):
        xs = x[tour]
        ys = y[tour]
        ax.quiver(xs[:-1], ys[:-1], xs[1:]-xs[:-1], ys[1:]-ys[:-1], scale_units='xy', angles='xy', scale=1.8, width=0.0001, headwidth=180, headlength=180, headaxislength=140)
        ax.plot(xs, ys, c='black', linewidth=1)
        ax.scatter(xs, ys, s=170, zorder=3, c='white', edgecolor='black')
        ax.tick_params(labelsize=6)

        for i, (x, y) in enumerate(zip(xs[:-1], ys[:-1])):
            ax.annotate(str(tour[i]), (x, y), fontsize='small', ha='center', va='center')

xs = np.array([0, 1, 2, 4, 3, 2, 1])
ys = np.array([0, 0.5, 3, 2.75, 1, 2, 2.75])

initial_candidate = [0, 1, 2, 3, 4, 5, 6, 0]
swap_stops_candidate = [0, 1, 5, 3, 4, 2, 6, 0]
swap_paths_candidate = [0, 1, 5, 4, 3, 2, 6, 0]

# Draw plot
fig, axarr = plt.subplots(1, 3, figsize=(13, 4))
plot_tour(ax=axarr[0], x=xs, y=ys, tour=initial_candidate)
axarr[0].set_title("Initial candidate")

plot_tour(ax=axarr[1], x=xs, y=ys, tour=swap_stops_candidate)
axarr[1].set_title("Swapping two stops")

plot_tour(ax=axarr[2], x=xs, y=ys, tour=swap_paths_candidate)
axarr[2].set_title("Reversing path between two stops")

plt.tight_layout()
plt.savefig("main.pdf")
