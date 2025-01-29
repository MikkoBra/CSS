import matplotlib
import numpy as np
from scipy.optimize import curve_fit

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



class ClusterSizePlot:

    def __init__(self):
        self.cluster_sizes = []
        self.system_size = 0

    def calculate_bin_centers_and_histogram(self, cluster_sizes):
        bin_edges = np.logspace(np.log10(1e-4), np.log10(1), 16)
        counts, bin_edges = np.histogram(cluster_sizes, bins=bin_edges, density=True)

        # Calculate the bin centers
        bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

        # Normalize the histogram to obtain a probability density
        normalized_hist = counts / np.sum(counts)
        return bin_centers, normalized_hist

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
        bin_centers, normalized_hist = self.calculate_bin_centers_and_histogram(cluster_sizes)

        ax.plot(bin_centers, normalized_hist, lw=1.25, label=label)

        # Set the x and y axis to log-log scale
        ax.set_xscale('log')
        ax.set_yscale('log')

        # Set axis labels
        ax.set_xlabel('Cluster Density (Fraction)')
        ax.set_ylabel('Probability Density')
        return bin_centers, normalized_hist, ax

    def plot_power_law(self, bin_centers, normalized_hist, ax, label_power_law=False):
        try:
            # Log-transform the data for fitting
            normalized_hist[normalized_hist == 0] = np.finfo(float).eps
            log_bin_centers = np.log10(bin_centers)
            log_normalized_hist = np.log10(normalized_hist)

            # Define a linear function for log-log fitting (y = m * x + c corresponds to log(P) = b*log(x) + log(a))
            def log_power_law(log_x, log_a, b):
                return log_a + b * log_x

            # Perform curve fitting in log space
            popt, pcov = curve_fit(log_power_law, log_bin_centers, log_normalized_hist, maxfev=10000)
            log_a, b = popt

            # Convert log-space parameters back to linear space for plotting
            a = 10 ** log_a

            # Generate fitted curve data
            fitted_curve = a * bin_centers ** b

            # Plot the fitted curve
            if not label_power_law:
                label = ''
            else:
                label = 'power law'
            ax.plot(bin_centers, fitted_curve, 'r--', alpha = 0.6, lw=1, label=label)
        except RuntimeError:
            print("Curve fitting failed.")

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

    def plot_single_cluster_size_probability_vs_cluster_size_with_power_law(self, ax, label_power_law):
        """
            Function that creates a plot of percolation probability vs forest density for one set of results.

            index: Index of the results in the PercolationPlot object's results array
        """
        label = r'$N =$ ' + str(self.system_size)
        bin_centers, normalized_hist, ax = self.plot_cluster_size_probability_vs_cluster_size(self.cluster_sizes, ax, label)
        self.plot_power_law(bin_centers, normalized_hist, ax, label_power_law)
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

    def plot_single_cluster_size(self, results_per_system_size, system_size, title):
        fig, ax = plt.subplots()
        self.save_cluster_sizes(results_per_system_size[system_size])
        self.system_size = system_size
        self.plot_single_cluster_size_probability_vs_cluster_size(ax)
        # ax.set_xlabel(r'Density $d$')
        # ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title(title)
        ax.grid()
        plt.show()

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
        ax.grid()
        plt.show()

    def plot_multiple_cluster_size_with_power_law(self, results_per_system_size, title):
        fig, ax = plt.subplots()
        label_power_law = False
        total_items = len(results_per_system_size)
        for index, system_size in enumerate(results_per_system_size):
            if index == total_items - 1:
                label_power_law = True
            self.save_cluster_sizes(results_per_system_size[system_size])
            self.system_size = system_size
            self.plot_single_cluster_size_probability_vs_cluster_size_with_power_law(ax, label_power_law)
        # ax.set_xlabel(r'Density $d$')
        # ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title(title)
        ax.grid()
        plt.show()

    def plot_multiple_power_law(self, results_per_system_size, title):
        fig, ax = plt.subplots()
        total_items = len(results_per_system_size)
        label_power_law = False
        for index, system_size in enumerate(results_per_system_size):
            if index == total_items - 1:
                label_power_law = True
            self.save_cluster_sizes(results_per_system_size[system_size])
            self.system_size = system_size
            bin_centers, normalized_hist = self.calculate_bin_centers_and_histogram(self.cluster_sizes)
            self.plot_power_law(bin_centers, normalized_hist, ax, label_power_law)
        # ax.set_xlabel(r'Density $d$')
        # ax.set_ylabel(r'$P_N$')
        ax.set_xlabel(r'Cluster Size $s$')
        ax.set_ylabel(r'Cluster Size Probability $P_N(s)$')
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.legend()
        ax.set_title(title)
        ax.grid()
        plt.show()
