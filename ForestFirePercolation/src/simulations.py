import numpy as np
import matplotlib.pyplot as plt
from model import ForestFireModel

class ForestFireSimulations:
    def __init__(self, size, forest_density, num_simulations, ignition_num = 0):
        self.size = size
        self.forest_density = forest_density
        self.ignition_num = ignition_num
        self.num_simulations = num_simulations
        self.results = []

    def run_simulations_random(self):
        for _ in range(self.num_simulations):
            model = ForestFireModel(self.size, self.forest_density, self.ignition_num)
            model.ignite_fire_random()
            while model.get_num_burning() > 0:
                model.spread_fire()
            self.results.append({
                'percentage_burnt': model.percentage_burnt(),
                'percentage_burning': model.percentage_burning(),
                'percentage_trees': model.percentage_trees()
            })


    def run_simulations_corner(self):
        for _ in range(self.num_simulations):
            model = ForestFireModel(self.size, self.forest_density, self.ignition_num)
            model.ignite_fire_corner()
            while model.get_num_burning() > 0:
                model.spread_fire()
            self.results.append({
                'percentage_burnt': model.percentage_burnt(),
                'percentage_burning': model.percentage_burning(),
                'percentage_trees': model.percentage_trees()
            })

    def run_simulations_center(self):
        for _ in range(self.num_simulations):
            model = ForestFireModel(self.size, self.forest_density, self.ignition_num)
            model.ignite_fire_center()
            while model.get_num_burning() > 0:
                model.spread_fire()
            self.results.append({
                'percentage_burnt': model.percentage_burnt(),
                'percentage_burning': model.percentage_burning(),
                'percentage_trees': model.percentage_trees()
            })

    def plot_burnt_distribution(self):
        burnt_percentages = [result['percentage_burnt'] for result in self.results]
        plt.hist(burnt_percentages, bins=10, edgecolor='black')
        plt.title('Distribution of Burnt Trees')
        plt.xlabel('Percentage of Burnt Trees')
        plt.ylabel('Frequency')
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
    

    def get_results(self):
        return self.results