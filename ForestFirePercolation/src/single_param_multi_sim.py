import numpy as np
import matplotlib.pyplot as plt

from ForestFirePercolation.src.model import ForestFireModel
from typing import Optional

class SingleParamMultiSim:
    def __init__(self, size: int, forest_density: float, num_simulations: int, ignition_location: str, 
                 env_index: float, wind: bool, plant_tree_proportion: float, tree_burn_time: int, 
                 plant_burn_time: int, ignition_num: int = 0, random_seed: Optional[int] = None):
        """
        Class to run multiple simulations of the forest fire model with a specified set of parameters.

        Parameters:
            size (int): The size of the forest.
            forest_density (float): The density of the forest.
            num_simulations (int): The number of simulations to run.
            ignition_location (str): The location of the ignition point ('random', 'corner', 'center').
            env_index (float): The environmental index.
            wind (bool): Whether wind is present.
            plant_tree_proportion (float): The proportion of trees to plants.
            tree_burn_time (int): The time taken for a tree to burn.
            plant_burn_time (int): The time taken for a plant to burn.
            ignition_num (int): The number of ignition points.
            random_seed (Optional[int]): The random seed to use for the simulations.

        Methods:
            run_simulations: Run the specified number of simulations with the specified parameters.
            plot_burnt_distribution: Plot a histogram of the distribution of burnt trees.
            plot_burnt_distribution_log_log: Plot a log-log histogram of the distribution of burnt trees.
            get_average_results: Get the average percentage of burnt trees, burning trees, and trees remaining.
            proportion_burns_left_to_right: Get the proportion of simulations that burn from left to right.
            get_results: Get the results of the simulations.
        """
        self.tree_burn_time = tree_burn_time
        self.plant_burn_time = plant_burn_time
        self.plant_tree_proportion = plant_tree_proportion
        self.size = size
        self.forest_density = forest_density
        self.env_index = env_index
        self.wind = wind
        self.ignition_num = ignition_num
        self.num_simulations = num_simulations
        self.ignition_location = ignition_location
        self.random_seed = random_seed 
        self.results = []

    def run_simulations(self):
        """
        Run the specified number of simulations with the specified parameters.
        This method runs the specified number of simulations with the specified parameters and stores the results.
        """
        for _ in range(self.num_simulations):
            model = ForestFireModel(self.size, self.forest_density, self.env_index, self.wind, 
                                    self.plant_tree_proportion, self.tree_burn_time, 
                                    self.plant_burn_time, self.ignition_num, self.random_seed)

            if self.ignition_location == 'random':
                model.ignite_fire_random()
            elif self.ignition_location == 'corner':
                model.ignite_fire_corner()
            elif self.ignition_location == 'center':
                model.ignite_fire_center()

            while model.get_num_burning() > 0:
                model.spread_fire()
            self.results.append({
                'percentage_burnt': model.percentage_burnt(),
                'percentage_burning': model.percentage_burning(),
                'percentage_trees': model.percentage_trees(),
                'burns_left_to_right': model.burns_left_to_right()
            })

    def plot_burnt_distribution(self):
        """
        Plot a histogram of the distribution of burnt trees.

        This method creates a histogram showing the frequency distribution of the percentage of burnt trees
        across all simulations.
        """
        burnt_percentages = [result['percentage_burnt'] for result in self.results]
        plt.hist(burnt_percentages, bins=10, edgecolor='black')
        plt.hist(burnt_percentages, bins=10, edgecolor='black')

        plt.title('Distribution of Burnt Trees')
        plt.xlabel('Percentage of Burnt Trees')
        plt.ylabel('Frequency')
        plt.show()

    def plot_burnt_distribution_log_log(self):
        """
        Plot a log-log histogram of the distribution of burnt trees.

        This method plots the distribution of the percentage of burnt trees
        on a log-log scale using a histogram.
        """
        burnt_percentages = [result['percentage_burnt'] for result in self.results]
        bins = np.logspace(np.log10(min(burnt_percentages)), np.log10(max(burnt_percentages)), 10)
        
        plt.hist(burnt_percentages, bins=bins, edgecolor='black')
        plt.xscale('log')
        plt.yscale('log')

        plt.title('Distribution of Burnt Trees (Log-Log Scale)')
        plt.xlabel('Percentage of Burnt Trees (Log Scale)')
        plt.ylabel('Frequency (Log Scale)')
        plt.show()

    def get_average_results(self):
        """
        Calculate and return the average percentage of burnt trees, burning trees, and trees remaining.

        Returns:
            dict: A dictionary containing the average percentage of burnt trees, burning trees, and trees remaining.
        """
        avg_burnt = np.mean([result['percentage_burnt'] for result in self.results])
        avg_burning = np.mean([result['percentage_burning'] for result in self.results])
        avg_trees = np.mean([result['percentage_trees'] for result in self.results])
        return {
            'average_percentage_burnt': avg_burnt,
            'average_percentage_burning': avg_burning,
            'average_percentage_trees': avg_trees
        }
    
    def proportion_burns_left_to_right(self):
        """
        Calculate the proportion of simulations that burn from left to right.

        Returns:
            float: The proportion of simulations that burn from left to right.
        """
        count = 0
        for result in self.results:
            if result['burns_left_to_right'] == True:
                count += 1

        return count / self.num_simulations

    def get_results(self):
        """
        Get the results of the simulations.
        """
        return self.results
