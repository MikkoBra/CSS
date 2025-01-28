import matplotlib.pyplot as plt
from percolation_plot import PercolationPlot


class MultiSettingPlot(PercolationPlot):
    """
    Class for plots that take multiple system settings in one percolation plot (aside from system size).
    """

    def plot_multiple_settings(self, results_dict, title, single_size=None, plot_critical=False):
        """
        Function that creates a plot of percolation probability vs forest density for all sets of saved results in
        the same figure.

        :param results_dict: Dictionary of the following structure:
         {
            results: [dicts]
            critical_points: [floats]
            label_suffixes: [strings]
            colors: [strings]
         }
        :param title: Title of the figure.
        :param single_size: String representing a single system size to plot.
        :param plot_critical: Boolean that, if True, causes the x-axs to zoom in on the critical value.
        """
        fig, ax = plt.subplots()
        results_per_setting = results_dict['results']
        critical_points = results_dict['critical_points']
        label_suffixes = results_dict['label_suffixes']
        colors = results_dict['colors']
        results_index = 0
        for results_per_system_size in results_per_setting:
            if single_size:
                self.save_amount_percolated_per_density(results_per_system_size[single_size])
                self.system_size = single_size + label_suffixes[results_index]
                self.plot_single_percolation_vs_density(ax, critical_points[results_index])
            else:
                for system_size in results_per_system_size:
                    self.save_amount_percolated_per_density(results_per_system_size[system_size])
                    self.system_size = system_size + label_suffixes[results_index]
                    self.plot_single_percolation_vs_density(ax, critical_points[results_index])
            # Add critical point and/or zoom in on critical point
            critical_point = critical_points[results_index]
            if critical_point != 0.0:
                ax.axvline(x=critical_point, color=colors[results_index], ls='--', label=r'$d_c$ = '
                                                                                         + str(critical_point))
            results_index += 1
        if plot_critical:
            ax.set_xlim(critical_points[0] - 0.05, critical_points[-1] + 0.05)
        ax.grid()
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title(title)
        plt.show()
