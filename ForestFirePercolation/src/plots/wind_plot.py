import matplotlib.pyplot as plt
from percolation_plot import PercolationPlot


class WindPlot(PercolationPlot):

    def plot_wind_vs_no_wind(self):
        """
            Function that creates a plot of percolation probability vs forest density for all sets of saved results in
            the same figure.
        """
        fig, ax = plt.subplots()
        result_idx = 0
        results = self.get_result(result_idx)
        label = r'Wind = True'
        self.plot_percolation_vs_density(results.densities, results.probabilities, results.system_size, ax, label)

        result_idx += 1
        label = r'Wind = False'
        results = self.get_result(result_idx)
        self.plot_percolation_vs_density(results.densities, results.probabilities, results.system_size, ax, label)

        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title('Percolation probability vs forest density for wind and no wind')
        plt.show()
