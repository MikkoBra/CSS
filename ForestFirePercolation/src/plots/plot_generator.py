from ForestFirePercolation.src.csvs import csv_reader
from ForestFirePercolation.src.plots.cluster_size_plot import ClusterSizePlot
from ForestFirePercolation.src.plots.percolation_plot import PercolationPlot
from ForestFirePercolation.src.plots.multi_setting_plot import MultiSettingPlot
from ForestFirePercolation.src.results.result_filter import ResultFilter
from ForestFirePercolation.src.critical_values import read_critical_values_json


class PlotGenerator:
    def __init__(self, file_name='Simulation_data.csv'):
        self.file_name = file_name
        self.percolation_plot = PercolationPlot()
        self.multi_setting_plot = MultiSettingPlot()
        self.cluster_size_plot = ClusterSizePlot()
        self.result_filter = ResultFilter()
        self.results_per_system_size = csv_reader.read_percolation_csv(self.file_name)
        self.critical_points = {'base': 0.596,
                                'wind': 0.549,
                                'env_index':  0.7375,
                                'env_wind': 0.883,
                                'plant': 0.661}
        self.critical_points_dens = read_critical_values_json()

    def generate_single_percolation_plot_per_size(self, results_per_system_size, title, file_name):
        """
        Generates individual percolation probability vs density plots for each system size.

        :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
         keys.
        :param title: Title of the plot.
        :param file_name: Name of the file the plot is saved in.
        """
        for system_size in results_per_system_size:
            new_file_name = file_name + '_' + system_size
            self.percolation_plot.plot_percolation({system_size: results_per_system_size[system_size]}, title,
                                                   new_file_name)

    def generate_single_percolation_plot(self, results_per_system_size, system_size, title, file_name, critical_point):
        """
        Generates a percolation probability vs density plot for a specified system size.

        :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
         keys.
        :param system_size: System size to create a percolation plot for.
        :param title: Title of the plot.
        :param file_name: Name of the file the plot is saved in.
        :param critical_point: Critical point to add a vertical line for.
        """
        self.percolation_plot.plot_percolation({system_size: results_per_system_size[system_size]}, title, file_name +
                                               '_' + system_size, critical_point)

    def generate_single_critical_point_plot(self, results_per_system_size, system_size, title, file_name,
                                            critical_point=0.0):
        """
        Generates a percolation probability vs density plot for a specified system size zoomed in around the
         critical point.

        :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
         keys.
        :param system_size: System size to create a percolation plot for.
        :param title: Title of the plot.
        :param file_name: Name of the file the plot is saved in.
        :param critical_point: Critical point to add a vertical line for.
        """
        self.percolation_plot.plot_percolation({system_size: results_per_system_size[system_size]}, title, file_name +
                                               '_' + system_size, critical_point, plot_critical=True)

    def generate_percolation_multi_plot(self, results_per_system_size, title, file_name, critical_point=0.0):
        """
        Generates a single figure containing percolation probability vs density plots for all system sizes in the
        csv data.

        :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
         keys.
        :param title: Title of the plot.
        :param file_name: Name of the file the plot is saved in.
        :param critical_point: Critical point to add a vertical line for.
        """
        self.percolation_plot.plot_percolation(results_per_system_size, title, file_name, critical_point)

    def generate_critical_point_multi_plot(self, results_per_system_size, title, file_name, critical_point=0.0):
        """
        Generates a single figure containing percolation probability vs density plots for all system sizes in the
        csv data zoomed in around the critical point.

        :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
         keys.
        :param title: Title of the plot.
        :param file_name: Name of the file the plot is saved in.
        :param critical_point: Critical point to add a vertical line for.
        """
        self.percolation_plot.plot_percolation(results_per_system_size, title, file_name,
                                               critical_point, plot_critical=True)

    def generate_single_size_multiple_settings_plot(self, results_dict, title, system_size, file_name):
        """
        Generates a percolation probability vs density plot for a specified system size.

        :param results_dict: Dictionary of the following structure:
             {
                results: [dicts]
                critical_points: [floats]
                label_suffixes: [strings]
                colors: [strings]
             }
        :param title: Title of the figure.
        :param system_size: String representation of the system size to plot for.
        :param file_name: Name of the file the plot is saved in.
        """
        self.multi_setting_plot.plot_multiple_settings(results_dict, title, file_name + '_' + system_size,
                                                       single_size=system_size)

    def generate_single_size_multiple_settings_critical_plot(self, results_dict, title, system_size, file_name):
        """
        Generates a percolation probability vs density plot for a specified system size zoomed in around the critical
        points of the systems.

        :param results_dict: Dictionary of the following structure:
             {
                results: [dicts]
                critical_points: [floats]
                label_suffixes: [strings]
                colors: [strings]
             }
        :param title: Title of the figure.
        :param system_size: String representation of the system size to plot for.
        :param file_name: Name of the file the plot is saved in.
        """
        self.multi_setting_plot.plot_multiple_settings(results_dict, title, file_name + '_' + system_size,
                                                       single_size=system_size, plot_critical=True)

    def generate_multiple_settings_multi_plot(self, results_dict, title, file_name):
        """
        Generates a percolation probability vs density plot for multiple systems and all system sizes.

        :param results_dict: Dictionary of the following structure:
             {
                results: [dicts]
                critical_points: [floats]
                label_suffixes: [strings]
                colors: [strings]
             }
        :param title: Title of the figure.
        :param file_name: Name of the file the plot is saved in.
        """
        self.multi_setting_plot.plot_multiple_settings(results_dict, title, file_name)

    def generate_base_experiment_plots(self):
        """
        Generates all percolation plots needed to visualize the data from the base model experiment.
        Includes:
        - percolation plot for a single size
        - percolation plot for a single size, zoomed in around the critical point
        - percolation plot for all sizes
        - percolation plot for all sizes, zoomed in around the critical point
        """
        filtered_results = self.result_filter.no_wind_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density\n(base)"
        title2 = "Percolation probability vs forest density around the critical point\n(base)"
        self.generate_single_percolation_plot(filtered_results, '300', title, 'single_percolation_base',
                                              self.critical_points['base'])
        self.generate_single_critical_point_plot(filtered_results, '300', title2, 'single_percolation_critical_base',
                                                 self.critical_points['base'])
        self.generate_percolation_multi_plot(filtered_results, title, 'multi_percolation_base',
                                             self.critical_points['base'])
        self.generate_critical_point_multi_plot(filtered_results, title2, 'multi_percolation_critical_base',
                                                self.critical_points['base'])

    def generate_wind_experiment_plots(self):
        """
        Generates all percolation plots needed to visualize the data from the wind model experiment.
        Includes:
        - percolation plot for a single size (wind vs no wind)
        - percolation plot for a single size, zoomed in around the critical point (wind vs no wind)
        - percolation plot for all sizes (wind only)
        - percolation plot for all sizes, zoomed in around the critical point (wind only)
        """
        wind_dict = self.result_filter.init_wind_vs_no_wind_dict(self.results_per_system_size, self.critical_points)
        wind_results = self.result_filter.wind_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density\n(wind vs no wind)"
        title2 = "Percolation probability vs forest density around the critical point\n(wind vs no wind)"
        self.generate_single_size_multiple_settings_plot(wind_dict, title, '300', 'single_percolation_wind')
        self.generate_single_size_multiple_settings_critical_plot(wind_dict, title2, '300',
                                                                  'single_percolation_critical_wind')
        self.generate_percolation_multi_plot(wind_results, title, 'multi_percolation_wind', self.critical_points['wind'])
        self.generate_critical_point_multi_plot(wind_results, title2, 'multi_percolation_critical_wind',
                                                self.critical_points['wind'])

    def generate_env_index_experiment_plots(self):
        """
        Generates all percolation plots needed to visualize the data from the env_index model experiment.
        Includes:
        - percolation plot for a single size (all env_indices)
        - percolation plot for all sizes (env_index 0.75)
        - percolation plot for all sizes, zoomed in around the critical point (env_index 0.75)
        """
        env_index_dict = self.result_filter.init_env_index_dict(self.results_per_system_size, self.critical_points)
        env_index_results = self.result_filter.env_075_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density\n(environmental influences)"
        title2 = "Percolation probability vs forest density\n(env_index 0.75)"
        title3 = "Percolation probability vs forest density around the critical point\n(env_index 0.75)"
        self.generate_single_size_multiple_settings_plot(env_index_dict, title, '300', 'single_percolation_env_index')
        self.generate_percolation_multi_plot(env_index_results, title2, 'multi_percolation_env_index',
                                             self.critical_points['env_index'])
        self.generate_critical_point_multi_plot(env_index_results, title3, 'multi_percolation_critical_env_index',
                                                self.critical_points['env_index'])

    def generate_env_index_050_and_wind_experiment_plots(self):
        """
        Generates all percolation plots needed to visualize the data from the env_index + wind model experiment.
        Includes:
        - percolation plot for a single size (env_index 0.50, env_index 0.50 with wind, base model)
        - percolation plot for all sizes (env_index 0.50 with wind)
        - percolation plot for all sizes, zoomed in around the critical point (env_index 0.50 with wind)
        """
        env_wind_dict = self.result_filter.init_env_wind_dict(self.results_per_system_size, self.critical_points)
        env_wind_results = self.result_filter.env_wind_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density\n(env_index 0.5 + wind)"
        title2 = "Percolation probability vs forest density around the critical point\n(env_index 0.5 + wind)"
        self.generate_single_size_multiple_settings_plot(env_wind_dict, title, '300', 'single_percolation_env_wind')
        self.generate_percolation_multi_plot(env_wind_results, title, 'multi_percolation_env_wind',
                                             self.critical_points['env_wind'])
        self.generate_critical_point_multi_plot(env_wind_results, title2, 'multi_percolation_critical_env_wind',
                                                self.critical_points['env_wind'])

    def generate_plant_experiment_plots(self):
        """
        Generates all percolation plots needed to visualize the data from the plant experiment.
        Includes:
        - percolation plot for a single size (plant_tree_proportion 0.50 burn_time 3 env_index 0.75, env_index 0.75)
        - percolation plot for all sizes (plant_tree_proportion 0.50 burn_time 3 env_index 0.75)
        - percolation plot for all sizes, zoomed in around the critical point (plant_tree_proportion 0.50 burn_time 3
          env_index 0.75)
        """
        plant_dict = self.result_filter.init_plant_075_dict(self.results_per_system_size, self.critical_points)
        plant_results = self.result_filter.plant_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density\n(env_index 0.75 + 50% plant)"
        title2 = "Percolation probability vs forest density around the critical point\n(env_index 0.75 + 50% plant)"
        self.generate_single_size_multiple_settings_plot(plant_dict, title, '300', 'single_percolation_plant')
        self.generate_percolation_multi_plot(plant_results, title, 'multi_percolation_plant', self.critical_points['plant'])
        self.generate_critical_point_multi_plot(plant_results, title2, 'multi_percolation_plant_critical',
                                                self.critical_points['plant'])

    def generate_SOC_plots(self, filtered_results, title, file_name):
        # self.cluster_size_plot.plot_single_cluster_size(filtered_results, '100', title)
        self.cluster_size_plot.plot_multiple_cluster_size(filtered_results, title, file_name + '_multiple')
        # self.cluster_size_plot.plot_multiple_cluster_size_with_power_law(filtered_results, title)
        # self.cluster_size_plot.plot_multiple_power_law(filtered_results, title)

    def generate_base_SOC_plots(self):
        filtered_results = self.result_filter.no_wind_at_size_specific_critical_filter(self.results_per_system_size,
                                                                         self.critical_points_dens['base'])
        title = "Cluster density probability vs cluster density\n(base)"
        self.generate_SOC_plots(filtered_results, title, 'base')

    def generate_wind_SOC_plots(self):
        filtered_results = self.result_filter.wind_at_size_specific_critical_filter(self.results_per_system_size,
                                                                      self.critical_points_dens['wind'])
        title = "Cluster density probability vs cluster density\n(wind)"
        self.generate_SOC_plots(filtered_results, title, 'wind')

    def generate_env_index_SOC_plots(self):
        filtered_results = self.result_filter.env_075_at_size_specific_critical_filter(self.results_per_system_size,
                                                                         self.critical_points_dens['env_index'])
        title = "Cluster density probability vs cluster density\n(env_index)"
        self.generate_SOC_plots(filtered_results, title, 'env')

    def generate_plant_SOC_plots(self):
        filtered_results = self.result_filter.plant_at_size_specific_critical_filter(self.results_per_system_size,
                                                                       self.critical_points_dens['plant'])
        title = "Cluster density probability vs cluster density\n(plant)"
        self.generate_SOC_plots(filtered_results, title, 'plant')

    def generate_env_wind_SOC_plots(self):
        filtered_results = self.result_filter.env_wind_at_size_specific_critical_filter(self.results_per_system_size,
                                                                          self.critical_points_dens['env_wind'])
        title = "Cluster density probability vs cluster density\n(env_index + wind)"
        self.generate_SOC_plots(filtered_results, title, 'env_wind')


# generator = PlotGenerator("Snellius/totaldensity_extended_extra.csv")
# generator.generate_base_experiment_plots()
# generator.generate_wind_experiment_plots()
# generator.generate_env_index_experiment_plots()
# generator.generate_env_index_050_and_wind_experiment_plots()
# generator.generate_plant_experiment_plots()
# generator.generate_SOC_plot()
