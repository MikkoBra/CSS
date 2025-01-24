import numpy as np
import matplotlib.pyplot as plt
from model import ForestFireModel
from simulations import ForestFireSimulations
from typing import Optional, Dict, Any

class DensityForestFireSimulations:
    def __init__(self, size: int, num_sims_per_prob: int, ignition_location: str, 
                 env_index: float, wind: bool, plant_tree_proportion: float, 
                 tree_burn_time: int, plant_burn_time: int, ignition_num: int = 0, random_seed: Optional[int] = None):
        self.tree_burn_time = tree_burn_time
        self.plant_burn_time = plant_burn_time
        self.plant_tree_proportion = plant_tree_proportion
        self.size = size
        self.ignition_num = ignition_num
        self.num_simulations = num_sims_per_prob
        self.env_index = env_index
        self.wind = wind
        self.ignition_location = ignition_location
        self.random_seed = random_seed
        self.results = []

    def run_density_simulations(self, density_values):
        all_results = []
        for density in density_values:
            print(density)
            self.forest_density = density
            sim_results = self.run_simulations()
            all_results.append({
                'density': density,
                'results': sim_results
            })
        return all_results

    def run_simulations(self):
        sim_results = []
        for _ in range(self.num_simulations):
            simulation = ForestFireSimulations(self.size, self.forest_density, self.num_simulations, 
                                               self.ignition_location, self.env_index, self.wind, 
                                               self.plant_tree_proportion, self.tree_burn_time, self.plant_burn_time, 
                                               self.ignition_num, random_seed=self.random_seed)
            simulation.run_simulations()
            sim_results.append(simulation.get_results())
        return sim_results

    def plot_density_vs_burnt(self, density_results):
        densities = []
        burnt_percentages = []
        for result in density_results:
            densities.append(result['density'])
            results = result['results']

            temp_burnt = []
            for result_sim in results:
                for i in result_sim:
                    temp_burnt.append(i['percentage_burnt'])

            avg_burnt_percentage = np.mean(temp_burnt)
            burnt_percentages.append(avg_burnt_percentage)

        plt.plot(densities, burnt_percentages, marker='o')
        plt.title('Average Burnt Percentage vs Forest Density')
        plt.xlabel('Forest Density')
        plt.ylabel('Average Percentage of Burnt Trees')
        plt.show()