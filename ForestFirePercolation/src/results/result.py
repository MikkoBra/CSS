class Result:
    def __init__(self, size=0, density=0.0, wind=False, env_index=0.0, percolation=False, percentage_burnt_down=0.0):
        self.density = density
        self.size = size
        self.wind = wind
        self.env_index = env_index
        self.percolation = percolation
        self.percentage_burnt_down = percentage_burnt_down

    def dict_to_result(self, result_dict):
        self.density = float(result_dict['density'])
        self.size = float(result_dict['size'])
        self.wind = result_dict['wind'] == 'True'
        self.env_index = float(result_dict['env_index'])
        self.percolation = result_dict['percolation'] == 'True'
        self.density = float(result_dict['density'])
