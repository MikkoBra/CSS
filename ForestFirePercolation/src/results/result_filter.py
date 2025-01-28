class ResultFilter:
    def __init__(self):
        self.colors = ['midnightblue', 'darkgoldenrod', 'darkolivegreen', 'maroon']

    def no_wind_conditions(self, result):
        value = not result.wind and result.env_index == 1.0 and result.plant_tree_proportion == 0.0
        return value

    def no_wind_filter(self, results_per_system_size):
        return {key: [result for result in value if self.no_wind_conditions(result)] for key, value in
                results_per_system_size.items()}

    def wind_conditions(self, result):
        value = result.wind and result.env_index == 1.0 and result.plant_tree_proportion == 0.0
        return value

    def wind_filter(self, results_per_system_size):
        return {key: [result for result in value if self.wind_conditions(result)] for key, value in
                results_per_system_size.items()}

    def env_025_conditions(self, result):
        value = not result.wind and result.plant_tree_proportion == 0.0 and result.env_index == 0.25
        return value

    def env_050_conditions(self, result):
        value = not result.wind and result.plant_tree_proportion == 0.0 and result.env_index == 0.5
        return value

    def env_075_conditions(self, result):
        value = not result.wind and result.plant_tree_proportion == 0.0 and result.env_index == 0.75
        return value

    def env_025_filter(self, results_per_system_size):
        return {key: [result for result in value if self.env_025_conditions(result)] for key, value in
                results_per_system_size.items()}

    def env_050_filter(self, results_per_system_size):
        return {key: [result for result in value if self.env_050_conditions(result)] for key, value in
                results_per_system_size.items()}

    def env_075_filter(self, results_per_system_size):
        return {key: [result for result in value if self.env_075_conditions(result)] for key, value in
                results_per_system_size.items()}

    def vegetation_conditions(self, result):
        value = not result.wind and result.env_index == 0.5 and result.plant_tree_proportion == 0.5
        return value

    def vegetation_filter(self, results_per_system_size):
        return {key: [result for result in value if self.vegetation_conditions(result)] for key, value in
                results_per_system_size.items()}

    def init_wind_vs_no_wind_dict(self, results_per_system_size, critical_point_dict):
        no_wind_results = self.no_wind_filter(results_per_system_size)
        wind_results = self.wind_filter(results_per_system_size)
        results = [wind_results, no_wind_results]
        critical_points = [critical_point_dict['wind'], critical_point_dict['base']]
        label_suffixes = [' (wind)', ' (no wind)']
        colors = ['blue', 'green']
        results_dict = {
            'results': results,
            'critical_points': critical_points,
            'label_suffixes': label_suffixes,
            'colors': colors
        }
        return results_dict

    def init_env_index_dict(self, results_per_system_size, critical_point_dict):
        env_025_results = self.env_025_filter(results_per_system_size)
        env_050_results = self.env_050_filter(results_per_system_size)
        env_075_results = self.env_075_filter(results_per_system_size)
        no_index_results = self.no_wind_filter(results_per_system_size)
        results = [env_025_results, env_050_results, env_075_results, no_index_results]
        critical_points = [0.0, 0.0, critical_point_dict['env_index'], critical_point_dict['base']]
        label_suffixes = [' (env_index 0.25)', ' (env_index 0.50)',  ' (env_index 0.75)', ' (env_index 1.0)']
        results_dict = {
            'results': results,
            'critical_points': critical_points,
            'label_suffixes': label_suffixes,
            'colors': self.colors
        }
        return results_dict
