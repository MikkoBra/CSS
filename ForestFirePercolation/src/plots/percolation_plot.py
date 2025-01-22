import numpy as np
import matplotlib.pyplot as plt
from ..results import Results


class PercolationPlot:

    def __init__(self, results):
        self.results = results

    def plot_percolation_vs_density(self, densities, probabilities, system_size, ax, label):
        """
            Function that plots the probability of the system percolating over the forest density.

            densities: Array of values representing the forest density.
            probabilities: Array of values representing the probability of the system percolating for the corresponding
             density.
            system_size: System size N for an NxN square grid.
        """
        ax.plot(densities, probabilities, label=label)
        return ax

    def plot_single_percolation_vs_density(self, index=0):
        """
            Function that creates a plot of percolation probability vs forest density for one set of results.

            index: Index of the results in the PercolationPlot object's results array
        """
        fig, ax = plt.subplots()
        results = self.get_result(index)
        label = r'$P_N(d)$, $N =$ ' + str(results.system_size)
        self.plot_percolation_vs_density(results.densities, results.probabilities, results.system_size, ax, label)
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title('Percolation probability vs forest density for system size ' + str(results.system_size) + 'x'
                     + str(results.system_size))
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
            label = r'$P_N(d)$, $N =$ ' + str(results.system_size)
            self.plot_percolation_vs_density(results.densities, results.probabilities, results.system_size, ax, label)
            result_idx += 1
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title('Percolation probability vs forest density for varying system size.')
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

    def get_results(self):
        return self.results

    def clear_results(self):
        self.results = []
