from ForestFirePercolation.src.csvs import csv_reader
from ForestFirePercolation.src.plots.cluster_size_plot import ClusterSizePlot
from ForestFirePercolation.src.plots.percolation_plot import PercolationPlot
from ForestFirePercolation.src.plots.multi_setting_plot import MultiSettingPlot
from ForestFirePercolation.src.results.result_filter import ResultFilter


class PlotGenerator:
    def __init__(self, file_name='Simulation_data.csv'):
        self.file_name = file_name
        self.percolation_plot = PercolationPlot()
        self.multi_setting_plot = MultiSettingPlot()
        self.cluster_size_plot = ClusterSizePlot()
        self.result_filter = ResultFilter()
        self.results_per_system_size = csv_reader.read_percolation_csv(self.file_name)
        self.critical_points = {'base': 0.596, 'wind': 0.549, 'env_index':  0.736, 'env_wind': 0.883, 'plant': 0.661}

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

    def generate_single_critical_point_plot(self, results_per_system_size, system_size, title, critical_point=0.0):
        """
        Generates a percolation probability vs density plot for a specified system size zoomed in around the
         critical point.

        :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
         keys.
        :param system_size: System size to create a percolation plot for.
        :param title: Title of the plot.
        :param critical_point: Critical point to add a vertical line for.
        """
        self.percolation_plot.plot_percolation({system_size: results_per_system_size[system_size]}, title,
                                               critical_point, plot_critical=True)

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
        csv data zoomed in around the critical point.

        :param results_per_system_size: Dictionary containing arrays of Result objects as values and system sizes as
         keys.
        :param title: Title of the plot.
        :param critical_point: Critical point to add a vertical line for.
        """
        self.percolation_plot.plot_percolation(results_per_system_size, title, critical_point, plot_critical=True)

    def generate_single_size_multiple_settings_plot(self, results_dict, title, system_size):
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
        """
        self.multi_setting_plot.plot_multiple_settings(results_dict, title, single_size=system_size)

    def generate_single_size_multiple_settings_critical_plot(self, results_dict, title, system_size):
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
        """
        self.multi_setting_plot.plot_multiple_settings(results_dict, title, single_size=system_size, plot_critical=True)

    def generate_multiple_settings_multi_plot(self, results_dict, title):
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
        """
        self.multi_setting_plot.plot_multiple_settings(results_dict, title)

    def generate_base_experiment_plots(self):
        filtered_results = self.result_filter.no_wind_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density"
        title2 = "Percolation probability vs forest density around the critical point"
        self.generate_single_percolation_plot(filtered_results, '300', title, self.critical_points['base'])
        self.generate_single_critical_point_plot(filtered_results, '300', title2, self.critical_points['base'])
        self.generate_percolation_multi_plot(filtered_results, title, self.critical_points['base'])
        self.generate_critical_point_multi_plot(filtered_results, title2, self.critical_points['base'])

    def generate_wind_experiment_plots(self):
        wind_dict = self.result_filter.init_wind_vs_no_wind_dict(self.results_per_system_size, self.critical_points)
        wind_results = self.result_filter.wind_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density"
        self.generate_single_size_multiple_settings_plot(wind_dict, title, '300')
        self.generate_single_size_multiple_settings_critical_plot(wind_dict, title, '300')
        self.generate_percolation_multi_plot(wind_results, title, self.critical_points['wind'])
        self.generate_critical_point_multi_plot(wind_results, title, self.critical_points['wind'])

    def generate_env_index_experiment_plots(self):
        env_index_dict = self.result_filter.init_env_index_dict(self.results_per_system_size, self.critical_points)
        env_index_results = self.result_filter.env_075_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density"
        title2 = "Percolation probability vs forest density (env_index 0.75)"
        self.generate_single_size_multiple_settings_plot(env_index_dict, title, '300')
        self.generate_percolation_multi_plot(env_index_results, title2, self.critical_points['env_index'])
        self.generate_critical_point_multi_plot(env_index_results, title2, self.critical_points['env_index'])

    def generate_env_index_050_and_wind_experiment_plots(self):
        env_wind_dict = self.result_filter.init_env_wind_dict(self.results_per_system_size, self.critical_points)
        env_wind_results = self.result_filter.env_wind_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density"
        title2 = "Percolation probability vs forest density (env_index 0.5 + wind)"
        self.generate_single_size_multiple_settings_plot(env_wind_dict, title, '300')
        self.generate_percolation_multi_plot(env_wind_results, title2, self.critical_points['env_wind'])
        self.generate_critical_point_multi_plot(env_wind_results, title2, self.critical_points['env_wind'])

    def generate_plant_experiment_plots(self):
        plant_dict = self.result_filter.init_plant_075_dict(self.results_per_system_size, self.critical_points)
        plant_results = self.result_filter.plant_filter(self.results_per_system_size)
        title = "Percolation probability vs forest density"
        title2 = "Percolation probability vs forest density (env_index 0.75 + 50% plant)"
        self.generate_single_size_multiple_settings_plot(plant_dict, title, '300')
        self.generate_percolation_multi_plot(plant_results, title2, self.critical_points['plant'])
        self.generate_critical_point_multi_plot(plant_results, title2, self.critical_points['plant'])

    def generate_SOC_plots(self, filtered_results):
        title = "Cluster size probability vs cluster size"
        self.cluster_size_plot.plot_multiple_cluster_size(filtered_results, title)
        self.cluster_size_plot.plot_multiple_cluster_size_with_power_law(filtered_results, title)
        self.cluster_size_plot.plot_multiple_power_law(filtered_results, title)

    def generate_base_SOC_plots(self):
        filtered_results = self.result_filter.no_wind_at_critical_filter(self.results_per_system_size,
                                                                         self.critical_points['base'])
        self.generate_SOC_plots(filtered_results)

    def generate_wind_SOC_plots(self):
        filtered_results = self.result_filter.wind_at_critical_filter(self.results_per_system_size,
                                                                      self.critical_points['wind'])
        self.generate_SOC_plots(filtered_results)

    def generate_env_index_SOC_plots(self):
        filtered_results = self.result_filter.env_075_at_critical_filter(self.results_per_system_size,
                                                                         self.critical_points['env_index'])
        self.generate_SOC_plots(filtered_results)

    def generate_plant_SOC_plots(self):
        filtered_results = self.result_filter.plant_at_critical_filter(self.results_per_system_size,
                                                                       self.critical_points['plant'])
        self.generate_SOC_plots(filtered_results)

    def generate_env_wind_SOC_plots(self):
        filtered_results = self.result_filter.env_wind_at_critical_filter(self.results_per_system_size,
                                                                          self.critical_points['env_wind'])
        self.generate_SOC_plots(filtered_results)


# generator = PlotGenerator("Snellius/totaldensity_extended_extra.csv")
# generator.generate_base_experiment_plots()
# generator.generate_wind_experiment_plots()
# generator.generate_env_index_experiment_plots()
# generator.generate_env_index_050_and_wind_experiment_plots()
# generator.generate_plant_experiment_plots()
# generator.generate_SOC_plot()
