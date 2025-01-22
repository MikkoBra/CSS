import numpy as np
import matplotlib.pyplot as plt


def plot_density_percolation(density, p_perc, size):
    """
        Function that plots the probability of the system percolating over the forest density.

        density: Array of values representing the forest density.
        p_perc: Array of values representing the probability of the system percolating for the corresponding density.
        size: System size N for an NxN square grid.
    """
    fig, ax = plt.subplots()
    ax.plot(density, p_perc, label=r'$P_N(d)$, $N =$ ' + str(size))
    critical_idx = p_perc.argmax()
    ax.axvline(x=density[critical_idx], color='black', ls='--', label=r'$p_c$')
    ax.set_xlabel(r'Density $d$')
    ax.set_ylabel(r'$P_N$')
    ax.legend()
    plt.show()
    return


density = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
p_perc = np.array([0.0, 0.2, 0.4, 0.6, 0.4, 0.2])
plot_density_percolation(density, p_perc, 100)
