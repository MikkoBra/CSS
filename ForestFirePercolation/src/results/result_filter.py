class ResultFilter:
    def wind_conditions(self, result):
        value = not result.wind and result.env_index == 1.0 and result.plant_tree_proportion == 0.0
        return value

    def no_wind_filter(self, results_per_system_size):
        return {key: [result for result in value if self.wind_conditions(result)] for key, value in
                                 results_per_system_size.items()}
