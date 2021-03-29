from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics.pairwise
import sympy as sym

seed = 1
number_of_itinieraries = 3
number_of_stops = 20
np.random.seed(seed)
xs = np.random.randint(0, 100, (number_of_itinieraries, number_of_stops))
ys = np.random.randint(0, 100, (number_of_itinieraries, number_of_stops))
markers = Line2D.markers.keys()


# Draw plot
plt.figure()
for number, (x, y, marker) in enumerate(zip(xs, ys, markers)):
    plt.scatter(x, y, marker=marker, label=f"Itinerary {number}")
plt.legend(loc=9)
plt.title("Map of all stops")
plt.savefig("main.pdf")

# Write distance matrices
with open("main.tex", "w") as f:
    for number, (x, y) in enumerate(zip(xs, ys)):
        f.write(r"\begin{equation}")
        f.write(f"d^{{({number})}}=")
        distance_matrix = sklearn.metrics.pairwise.euclidean_distances(tuple(zip(x, y)))
        distance_matrix = np.round(a=distance_matrix, decimals=1)
        latex = sym.latex(sym.Matrix(distance_matrix))
        f.write(latex)
        f.write(f"\label{{eqn:tsp-{number}}}")
        f.write(r"\end{equation}")
        f.write("\n")
