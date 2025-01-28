import matplotlib.pyplot as plt
from percolation_plot import PercolationPlot


class WindPlot(PercolationPlot):

    def plot_wind_vs_no_wind(self, results_per_wind_setting, title):
        """
            Function that creates a plot of percolation probability vs forest density for all sets of saved results in
            the same figure.
        """
        fig, ax = plt.subplots()
        for wind_setting_results in results_per_wind_setting:
            for system_size in wind_setting_results:
                self.save_amount_percolated_per_density(wind_setting_results[system_size])
                self.system_size = system_size + results_per_wind_setting['label_suffix']
                self.plot_single_percolation_vs_density(ax)
            # Add critical point and/or zoom in on critical point
            critical_point = results_per_wind_setting['crit']
            if critical_point != 0.0:
                ax.axvline(x=critical_point, ls='--', label=r'$d_c$ = ' + str(critical_point))
        ax.set_xlabel(r'Density $d$')
        ax.set_ylabel(r'$P_N$')
        ax.legend()
        ax.set_title(title)
        plt.show()
