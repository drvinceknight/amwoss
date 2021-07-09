from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics.pairwise
import sympy as sym

seed = 1
number_of_stops = 13
np.random.seed(seed)
xs = np.random.randint(0, 100, number_of_stops)
ys = np.random.randint(0, 100, number_of_stops)


# Draw plot
plt.figure()
plt.scatter(xs, ys)
plt.title("Map of all stops")
plt.savefig("main.pdf")

# Write distance matrices
with open("main.tex", "w") as f:
    f.write(r"\begin{equation}")
    f.write(f"d=")
    distance_matrix = sklearn.metrics.pairwise.euclidean_distances(tuple(zip(xs, ys)))
    distance_matrix = np.round(a=distance_matrix, decimals=0).astype('int')
    latex = sym.latex(sym.Matrix(distance_matrix))
    f.write(latex)
    f.write(f"\label{{eqn:tsp}}")
    f.write(r"\end{equation}")
    f.write("\n")
