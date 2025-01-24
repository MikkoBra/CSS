class ResultFilter:
    def no_wind_filter(self, results_per_system_size):
        return {key: [result for result in value if not result.wind] for key, value in
                                 results_per_system_size.items()}
