from ForestFirePercolation.src.csvs import csv_reader
from ForestFirePercolation.src.plots.cluster_size_plot import ClusterSizePlot
from ForestFirePercolation.src.plots.percolation_plot import PercolationPlot
from ForestFirePercolation.src.results.result_filter import ResultFilter


class PlotGenerator:
    def __init__(self, file_name='Simulation_data.csv'):
        self.file_name = file_name
        self.percolation_plot = PercolationPlot()
        self.cluster_size_plot = ClusterSizePlot()
        self.result_filter = ResultFilter()
        self.results_per_system_size = csv_reader.read_percolation_csv(self.file_name)
        self.critical_points = {'base': 0.596, 'wind': 0.0, 'env_index': 0.0, 'plant': 0.0}

    def generate_single_percolation_plot_per_size(self, results_per_system_size, title):
        """
            Generates individual percolation probability vs density plots for each system size.

            :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
             keys.
            :param title: Title of the plot.
        """
        for system_size in results_per_system_size:
            self.percolation_plot.plot_percolation({system_size: results_per_system_size[system_size]}, title)

    def generate_single_percolation_plot(self, results_per_system_size, system_size, title, critical_point):
        """
            Generates a percolation probability vs density plot for a specified system size.

            :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
             keys.
            :param system_size: System size to create a percolation plot for.
            :param title: Title of the plot.
            :param critical_point: Critical point to add a vertical line for.
        """
        self.percolation_plot.plot_percolation({system_size: results_per_system_size[system_size]}, title,
                                               critical_point)

    def generate_percolation_multi_plot(self, results_per_system_size, title, critical_point=0.0):
        """
            Generates a single figure containing percolation probability vs density plots for all system sizes in the
            csv data.

            :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
             keys.
            :param title: Title of the plot.
            :param critical_point: Critical point to add a vertical line for.
        """
        self.percolation_plot.plot_percolation(results_per_system_size, title, critical_point)

    def generate_critical_point_multi_plot(self, results_per_system_size, title, critical_point=0.0):
        """
            Generates a single figure containing percolation probability vs density plots for all system sizes in the
            csv data.

            :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
             keys.
            :param title: Title of the plot.
            :param critical_point: Critical point to add a vertical line for.
        """
        self.percolation_plot.plot_percolation(results_per_system_size, title, critical_point, plot_critical=True)

    def generate_cluster_size_multi_plot(self, results_per_system_size, title):
        self.cluster_size_plot.plot_multiple_cluster_size(results_per_system_size, title)

    def generate_base_experiment_plot(self):
        filtered_results = self.result_filter.no_wind_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density"
        self.generate_percolation_multi_plot(filtered_results, title, self.critical_points['base'])
        title2 = "Percolation probability vs forest density around the critical point"
        self.generate_critical_point_multi_plot(filtered_results, title2, self.critical_points['base'])

    def generate_wind_experiment_plot(self):
        filtered_results = self.result_filter.wind_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density with wind"
        self.generate_percolation_multi_plot(filtered_results, title, self.critical_points['wind'])

    def generate_env_index_experiment_plot(self):
        filtered_results = self.result_filter.env_index_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density with an environmental index"
        self.generate_percolation_multi_plot(filtered_results, title, self.critical_points['env_index'])

    def generate_vegetation_experiment_plot(self):
        filtered_results = self.result_filter.vegetation_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density with different types of vegetation"
        self.generate_percolation_multi_plot(filtered_results, title, self.critical_points['plant'])

    def generate_SOC_plot(self):
        filtered_results = self.result_filter.no_wind_filter(self.results_per_system_size)
        title = "Cluster size probability vs cluster size"
        self.generate_cluster_size_multi_plot(filtered_results, title)


generator = PlotGenerator("Simulation_data_all_1.csv")
generator.generate_base_experiment_plot()
# generator.generate_wind_experiment_plot()
# generator.generate_env_index_experiment_plot()
# generator.generate_vegetation_experiment_plot()
# generator.generate_SOC_plot()
