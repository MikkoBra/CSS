from ForestFirePercolation.src.csvs import csv_reader
from ForestFirePercolation.src.plots.percolation_plot import PercolationPlot
from ForestFirePercolation.src.results.result_filter import ResultFilter


class PlotGenerator:
    def __init__(self):
        self.percolation_plot = PercolationPlot()
        self.result_filter = ResultFilter()
        self.results_per_system_size = csv_reader.read_percolation_csv()

    def generate_percolation_plots(self, results_per_system_size):
        """
            Generates individual percolation probability vs density plots for each system size setting in the csv data.

            :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
             keys.
        """
        for system_size in results_per_system_size:
            self.percolation_plot.plot_percolation(results_per_system_size[system_size], system_size)

    def generate_percolation_plot(self, results_per_system_size, system_size):
        """
            Generates a percolation probability vs density plot for a specified system size.

            :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
             keys.
            :param system_size: System size to create a percolation plot for.
        """
        self.percolation_plot.plot_percolation(results_per_system_size[system_size], system_size)

    def generate_percolation_multi_plot(self, results_per_system_size):
        """
            Generates a single figure containing percolation probability vs density plots for all system sizes in the
            csv data.

            :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
             keys.
        """
        self.percolation_plot.plot_multiple_percolation(results_per_system_size)

    def generate_base_experiment_plot(self):
        filtered_results = self.result_filter.no_wind_filter(self.results_per_system_size)
        self.generate_percolation_multi_plot(filtered_results)

    def generate_wind_experiment_plot(self):
        filtered_results = self.result_filter.wind_filter(self.results_per_system_size)
        self.generate_percolation_multi_plot(filtered_results)

    def generate_env_index_experiment_plot(self):
        filtered_results = self.result_filter.env_index_filter(self.results_per_system_size)
        self.generate_percolation_multi_plot(filtered_results)

    def generate_vegetation_experiment_plot(self):
        filtered_results = self.result_filter.vegetation_filter(self.results_per_system_size)
        self.generate_percolation_multi_plot(filtered_results)


generator = PlotGenerator()
generator.generate_base_experiment_plot()
generator.generate_wind_experiment_plot()
generator.generate_percolation_multi_plot(generator.results_per_system_size)
