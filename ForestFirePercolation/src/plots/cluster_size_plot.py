import matplotlib
import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class ClusterSizePlot:

    def __init__(self):
        self.cluster_sizes = []
        self.system_size = 0

    def plot_cluster_size_probability_vs_cluster_size(self, cluster_sizes, ax, label):
        """
            Function that plots the probability of a given final cluster size for a simulation of the system per cluster
            size.

            cluster_sizes: Array of values representing the cluster sizes.
            probabilities: Array of values representing the probability of those cluster sizes occurring for one
             simulation.
            ax: matplotlib.pyplot ax object to plot the probabilities with.
            label: String label to assign to the plot.
        """
        counts, bins = np.histogram(cluster_sizes, bins=10)
        proportions = counts / counts.sum()
        bin_centers = (bins[:-1] + bins[1:]) / 2

        # Plot the proportions as a line
        plt.plot(bin_centers, proportions, marker='o', linestyle='-', color='black', label=label, linewidth=1)
        tick_positions = np.linspace(0, 1, 11)  # 15 evenly spaced ticks
        plt.xticks(tick_positions)
        return ax

    def plot_single_cluster_size_probability_vs_cluster_size(self, ax):
        """
            Function that creates a plot of percolation probability vs forest density for one set of results.

            index: Index of the results in the PercolationPlot object's results array
        """
        label = r'$N =$ ' + str(self.system_size)
        self.plot_cluster_size_probability_vs_cluster_size(self.cluster_sizes, ax, label)
        ax.set_xlabel(r'Cluster Size $s$')
        ax.set_ylabel(r'Cluster Size Probability $P_N(s)$')
        ax.legend()
        return ax

    def save_cluster_sizes(self, results):
        """


            :return:
        """
        self.cluster_sizes = []
        for result in results:
            self.cluster_sizes.append(result.percentage_burnt_down)

    def plot_multiple_cluster_size(self, results_per_system_size, title):
        fig, ax = plt.subplots()
        for system_size in results_per_system_size:
            self.save_cluster_sizes(results_per_system_size[system_size])
            self.system_size = system_size
            self.plot_single_cluster_size_probability_vs_cluster_size(ax)
        # ax.set_xlabel(r'Density $d$')
        # ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title(title)
        plt.show()
