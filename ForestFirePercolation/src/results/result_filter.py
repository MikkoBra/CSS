class ResultFilter:
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

    def env_index_conditions(self, result):
        value = not result.wind and result.plant_tree_proportion == 0.0
        return value

    def env_index_filter(self, results_per_system_size):
        return {key: [result for result in value if self.env_index_conditions(result)] for key, value in
                                 results_per_system_size.items()}

    def vegetation_conditions(self, result):
        value = not result.wind  and result.env_index == 1.0 and result.plant_tree_proportion == 0.5
        return value

    def vegetation_filter(self, results_per_system_size):
        return {key: [result for result in value if self.vegetation_conditions(result)] for key, value in
                                 results_per_system_size.items()}
