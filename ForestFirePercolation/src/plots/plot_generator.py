from ForestFirePercolation.src.csvs import csv_reader
from ForestFirePercolation.src.plots.percolation_plot import PercolationPlot


class PlotGenerator:
    def generate_percolation_plots(self):
        results_per_system_size = csv_reader.read_percolation_csv()
        plot = PercolationPlot()
        for system_size in results_per_system_size:
            plot.plot_percolation(results_per_system_size[system_size], system_size)

    def generate_percolation_plot(self, system_size):
        results_per_system_size = csv_reader.read_percolation_csv()
        plot = PercolationPlot()
        plot.plot_percolation(results_per_system_size[system_size], system_size)


generator = PlotGenerator()
generator.generate_percolation_plots()
