import numpy as np
import matplotlib.pyplot as plt
from ..results.result import Result


class PercolationPlot:

    def __init__(self):
        self.densities = []
        self.probabilities = []
        self.system_size = 0

    def plot_percolation_vs_density(self, densities, probabilities, ax, label):
        """
            Function that plots the probability of the system percolating over the forest density.

            densities: Array of values representing the forest density.
            probabilities: Array of values representing the probability of the system percolating for the corresponding
             density.
            system_size: System size N for an NxN square grid.
        """
        ax.plot(densities, probabilities, label=label)
        return ax

    def plot_single_percolation_vs_density(self):
        """
            Function that creates a plot of percolation probability vs forest density for one set of results.

            index: Index of the results in the PercolationPlot object's results array
        """
        fig, ax = plt.subplots()
        label = r'$P_N(d)$, $N =$ ' + str(self.system_size)
        self.plot_percolation_vs_density(self.densities, self.probabilities, ax, label)
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title('Percolation probability vs forest density for system size ' + str(self.system_size) + 'x'
                     + str(self.system_size))
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

    def add_multiple_results(self, results):
        for result in results:
            self.results.append(results)

    def get_result(self, index):
        return self.results[index]

    def get_results(self):
        return self.results

    def clear_results(self):
        self.results = []

    def save_amount_percolated_per_density(self, results):
        """
        Creates a dictionary that contains as keys the densities found in the results, and as values arrays where the
        first element is the total number of results for that density, and the second element is the number of results
        for that density where percolation = True.

        :return:
        """
        percolation_probability = {}
        for result in self.results:
            density = result.density
            if density in percolation_probability:
                percolation_probability[density][0] += 1
            else:
                percolation_probability[density] = [1, 0]
            if result.percolation:
                percolation_probability[density][0] += 1

    def plot_percolation(self, results, system_size):
        self.save_amount_percolated_per_density(results)
        self.system_size = system_size

