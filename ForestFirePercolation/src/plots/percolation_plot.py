import numpy as np
import matplotlib.pyplot as plt
from ForestFirePercolation.src.results import Results


class PercolationPlot:
    def __init__(self, results):
        self.results = results

    def plot_percolation_vs_density(self, densities, probabilities, system_size, ax):
        """
            Function that plots the probability of the system percolating over the forest density.

            densities: Array of values representing the forest density.
            probabilities: Array of values representing the probability of the system percolating for the corresponding
             density.
            system_size: System size N for an NxN square grid.
        """
        ax.plot(densities, probabilities, label=r'$P_N(d)$, $N =$ ' + str(system_size))
        return ax

    def plot_single_percolation_vs_density(self, index=0):
        """
            Function that creates a plot of percolation probability vs forest density for one set of results.

            index: Index of the results in the PercolationPlot object's results array
        """
        fig, ax = plt.subplots()
        results = self.get_result(index)
        self.plot_percolation_vs_density(results.densities, results.probabilities, results.system_size, ax)
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        plt.show()

    def plot_multiple_percolation_vs_density(self):
        """
            Function that creates a plot of percolation probability vs forest density for all sets of saved results in
            the same figure.
        """
        fig, ax = plt.subplots()
        result_idx = 0
        while result_idx < len(self.results):
            results = self.get_result(result_idx)
            self.plot_percolation_vs_density(results.densities, results.probabilities, results.system_size, ax)
            result_idx += 1
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        plt.show()

    def add_results(self, results):
        """
            Function that adds a set of results to the PercolationPlot's results array.

            results: Results object to add to the results array.
        """
        self.results.append(results)
        return

    def get_result(self, index):
        return self.results[index]

    def clear_results(self):
        self.results = []


density = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
p_perc1 = np.array([0.0, 0.2, 0.4, 0.6, 0.4, 0.2])
result1 = Results(density, p_perc1, 100)
p_perc2 = np.array([0.0, 0.1, 0.2, 0.3, 0.2, 0.1])
result2 = Results(density, p_perc2, 200)
plot = PercolationPlot([result1, result2])
plot.plot_multiple_percolation_vs_density()
plot.plot_single_percolation_vs_density()
