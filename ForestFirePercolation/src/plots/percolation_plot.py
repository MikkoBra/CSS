import numpy as np
import matplotlib
matplotlib.use('TkAgg')
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

    def plot_single_percolation_vs_density(self, ax):
        """
            Function that creates a plot of percolation probability vs forest density for one set of results.

            index: Index of the results in the PercolationPlot object's results array
        """
        label = r'$N =$ ' + str(self.system_size)
        self.plot_percolation_vs_density(self.densities, self.probabilities, ax, label)
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        return ax

    def save_amount_percolated_per_density(self, results):
        """
        Creates a dictionary that contains as keys the densities found in the results, and as values arrays where the
        first element is the total number of results for that density, and the second element is the number of results
        for that density where percolation = True.

        :return:
        """
        self.densities = []
        self.probabilities = []
        percolation_probability = {}
        for result in results:
            density = result.density
            if density in percolation_probability:
                percolation_probability[density][0] += 1.0
            else:
                percolation_probability[density] = [1, 0]
            if result.percolation:
                percolation_probability[density][1] += 1.0
        for density in percolation_probability:
            self.densities.append(density)
            probability = percolation_probability[density][1]/percolation_probability[density][0]
            self.probabilities.append(probability)

    def plot_percolation(self, results, system_size):
        fig, ax = plt.subplots()
        self.save_amount_percolated_per_density(results)
        self.system_size = system_size
        self.plot_single_percolation_vs_density(ax)
        plt.show()

    # def plot_multiple_percolation(self, results_per_system_size):
    #     fig, ax = plt.subplots()
    #     for system_size in results_per_system_size:
    #         self.save_amount_percolated_per_density(results_per_system_size[system_size])
    #         self.system_size = system_size
    #         self.plot_single_percolation_vs_density(ax)
    #     plt.show()

    def plot_multiple_percolation(self, results_per_system_size, title):
        fig, ax = plt.subplots()
        for system_size in results_per_system_size:
            self.save_amount_percolated_per_density(results_per_system_size[system_size])
            self.system_size = system_size
            self.plot_single_percolation_vs_density(ax)
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title(title)
        plt.show()

    def plot_around_critical(self, results_per_system_size, title):
        fig, ax = plt.subplots()
        for system_size in results_per_system_size:
            self.save_amount_percolated_per_density(results_per_system_size[system_size])
            self.system_size = system_size
            self.plot_single_percolation_vs_density(ax)
            ax.set_xlim(0.45, 0.7)
            ax.set_xlabel(r'Density $d$')
            ax.set_ylabel(r'$P_N$')
            ax.legend()
            ax.set_title(title)
        plt.show()

