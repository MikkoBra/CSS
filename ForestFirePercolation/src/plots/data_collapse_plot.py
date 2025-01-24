import numpy as np
import matplotlib.pyplot as plt
from ..results.result import Result


class DataCollapsePlot:
    def __init__(self, results):
        self.results = results
        self.cluster_size_probability = {}

    def plot_cluster_size_probability(self, percent_burned, ax, label):
        """
            Function that plots the probability of the system percolating over the forest density.

            percent_burned: Array of values representing the forest density.
            probabilities: Array of values representing the probability of the system percolating for the corresponding
             density.
            system_size: System size N for an NxN square grid.
        """
        ax.hist(percent_burned, bins=20, label=label, histtype='step')
        return ax

    def plot_single_cluster_size_probability(self, system_size):
        """
            Function that creates a plot of percolation probability vs forest density for all sets of saved results in
            the same figure.
        """
        fig, ax = plt.subplots()
        cluster_sizes = self.gather_cluster_size_distribution(system_size)
        if len(cluster_sizes) == 0:
            print('No results found for system size ' + str(system_size))
            return
        label = r'$P(s, N)$, $N =$ ' + str(system_size)
        self.plot_cluster_size_probability(cluster_sizes, ax, label)
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title('Percolation probability vs forest density for varying system size.')
        plt.show()

    def get_result(self, index):
        return self.results[index]

    def gather_cluster_size_distribution(self, system_size):
        result_idx = 0
        cluster_sizes = []
        while result_idx < len(self.results):
            result = self.get_result(result_idx)
            if result.system_size == system_size:
                cluster_sizes.append(result.percent_burned/100.0)
                result_idx += 1
        return cluster_sizes
