import numpy as np
import matplotlib.pyplot as plt
from model import ForestFireModel

class ForestFireSimulations:
    def __init__(self, size, forest_density, num_simulations, sim_type, env_index, wind ,ignition_num = 0):
        self.size = size
        self.forest_density = forest_density
        self.env_index = env_index
        self.wind = wind
        self.ignition_num = ignition_num
        self.num_simulations = num_simulations
        self.sim_type = sim_type
        self.results = []

    def run_simulations(self):
        for _ in range(self.num_simulations):
            model = ForestFireModel(self.size, self.forest_density, self.env_index, self.wind, self.ignition_num)

            if self.sim_type == 'random':
                model.ignite_fire_random()
            elif self.sim_type == 'corner':
                model.ignite_fire_corner()
            elif self.sim_type == 'center':
                model.ignite_fire_center()

            model.ignite_fire_random()
            while model.get_num_burning() > 0:
                model.spread_fire()
            self.results.append({
                'percentage_burnt': model.percentage_burnt(),
                'percentage_burning': model.percentage_burning(),
                'percentage_trees': model.percentage_trees(),
                'burns_left_to_right': model.burns_left_to_right()
            })

    def plot_burnt_distribution(self):
        burnt_percentages = [result['percentage_burnt'] for result in self.results]
        plt.hist(burnt_percentages, bins=10, edgecolor='black')
        plt.title('Distribution of Burnt Trees')
        plt.xlabel('Percentage of Burnt Trees')
        plt.ylabel('Frequency')
        plt.show()

    def plot_burnt_distribution_log_log(self):
        burnt_percentages = [result['percentage_burnt'] for result in self.results]
        plt.hist(burnt_percentages, bins=10, edgecolor='black', log=True)
        plt.xscale('log')
        plt.yscale('log')
        plt.title('Log-Log Distribution of Burnt Trees')
        plt.xlabel('Percentage of Burnt Trees (log scale)')
        plt.ylabel('Frequency (log scale)')
        plt.show()

    def get_average_results(self):
        avg_burnt = np.mean([result['percentage_burnt'] for result in self.results])
        avg_burning = np.mean([result['percentage_burning'] for result in self.results])
        avg_trees = np.mean([result['percentage_trees'] for result in self.results])
        return {
            'average_percentage_burnt': avg_burnt,
            'average_percentage_burning': avg_burning,
            'average_percentage_trees': avg_trees
        }
    
    
    
    def proportion_burns_left_to_right(self):
        count = 0
        for result in self.results:
            if result['burns_left_to_right'] == True:
                count += 1

        return count / self.num_simulations

    def get_results(self):
        return self.results
