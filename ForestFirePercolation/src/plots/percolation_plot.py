import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class PercolationPlot:

    def __init__(self):
        self.densities = []
        self.probabilities = []
        self.system_size = 0

    def plot_percolation_vs_density(self, densities, probabilities, ax, label):
        """
            Function that plots the probability of the system percolating over forest densities.

            :param densities: Array of values representing the forest density.
            :param probabilities: Array of values representing the probability of the system percolating for the corresponding
             density.
            :param ax: pyplot ax object to generate the plot in.
            :param label: Label to attach to the plot, to be used in the legend of the figure.
        """
        ax.plot(densities, probabilities, label=label)
        return ax

    def plot_single_percolation_vs_density(self, ax):
        """
            Function that creates a plot of percolation probability vs forest density for one system size.

            :param ax: pyplot ax object to generate the plot in.
        """
        label = r'$N =$ ' + str(self.system_size)
        self.plot_percolation_vs_density(self.densities, self.probabilities, ax, label)
        return ax

    def save_amount_percolated_per_density(self, results):
        """
            Computes the percolation probability per density, and saves the results in the PercolationPlot object's
             "densities" and "probabilities" arrays.
        """
        self.densities = []
        self.probabilities = []
        percolation_probability = {}
        # Fill dictionary with total number of results and number of results with percolation = True per density
        for result in results:
            density = result.density
            if density in percolation_probability:
                percolation_probability[density][0] += 1.0
            else:
                percolation_probability[density] = [1, 0]
            if result.percolation:
                percolation_probability[density][1] += 1.0
        # Save (number percolated/total number) per density
        sorted_probabilities = dict(sorted(percolation_probability.items()))
        for density in sorted_probabilities:
            self.densities.append(density)
            probability = sorted_probabilities[density][1]/sorted_probabilities[density][0]
            self.probabilities.append(probability)

    def plot_percolation(self, results_per_system_size, title, critical_point=0.0, plot_critical=False):
        """
            Generates percolation plots for every passed system size. If the critical point is given and non-zero, it
            generates a vertical line for the critical point. If plot_critical is given and True, the combined plot will
            range from [critical point - 0.15, critical point + 0.15] on the x-axis.

            :param results_per_system_size: Dictionary with Result objects per system size.
            :param title: Title of the plot.
            :param critical_point: Critical point for which, if given, a vertical line will be plotted.
            :param plot_critical: Boolean which, if True and critical point != 0.0, causes the x-axis to zoom in on the
             critical point.
        """
        fig, ax = plt.subplots()
        for system_size in results_per_system_size:
            self.save_amount_percolated_per_density(results_per_system_size[system_size])
            self.system_size = system_size
            self.plot_single_percolation_vs_density(ax)
        # Add critical point and/or zoom in on critical point
        if critical_point != 0.0:
            ax.axvline(x=critical_point, ls='--', label=r'$d_c$ = ' + str(critical_point))
            if plot_critical:
                ax.set_xlim(critical_point - 0.05, critical_point + 0.05)
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title(title)
        plt.show()

