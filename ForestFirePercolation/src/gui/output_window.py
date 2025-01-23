import numpy as np
from tkinter import *
from model import ForestFireModel
from density_sims import DensityForestFireSimulations
from simulations import ForestFireSimulations


class OutputWindow:
    def __init__(self, master, size, env_index, plant_tree_proportion, 
                 tree_burn_time, plant_burn_time, ignition_location, sim_type, 
                 wind, use_seed, ignition_num=None, num_simulations=None, 
                 density=None, random_seed=None, display_single=None):
        self.master = master
        master.title("Output")

        self.size = size
        self.env_index = env_index
        self.plant_tree_proportion = plant_tree_proportion
        self.tree_burn_time = tree_burn_time
        self.plant_burn_time = plant_burn_time
        self.ignition_location = ignition_location
        self.sim_type = sim_type
        self.wind = wind
        self.use_seed = use_seed
        self.ignition_num = ignition_num
        self.num_simulations = num_simulations
        self.density = density
        self.random_seed = random_seed
        self.display_single = display_single


        if sim_type == "single density, single sim":
            simulation = ForestFireModel(size, density, env_index, wind, 
                                 plant_tree_proportion, tree_burn_time, 
                                 plant_burn_time, ignition_num=ignition_num, 
                                 random_seed=self.random_seed)
            if ignition_location == "random":
                simulation.ignite_fire_random()
            elif ignition_location == "corner":
                simulation.ignite_fire_corner()
            elif ignition_location == "center":
                simulation.ignite_fire_center()

            if display_single == "yes":
                simulation.display_single_simulation()
            else:
                simulation.no_display_single_simulation()
            
            self.num_trees = simulation.get_num_trees()
            self.num_trees_label = Label(master, text=f"Number of trees: {self.num_trees}")
            self.num_trees_label.grid(row=0, column=0)

            self.num_burning = simulation.get_num_burning()
            self.num_burning_label = Label(master, text=f"Number of burning trees: {self.num_burning}")
            self.num_burning_label.grid(row=1, column=0)

            self.num_burnt = simulation.get_num_burnt()
            self.num_burnt_label = Label(master, text=f"Number of burnt trees: {self.num_burnt}")
            self.num_burnt_label.grid(row=2, column=0)

            self.burnt_prop = simulation.burns_left_to_right()
            self.burnt_prop_label = Label(master, text=f"Proportion of burns left to right: {self.burnt_prop}")
            self.burnt_prop_label.grid(row=3, column=0)

        elif sim_type == 'single density, multiple sim':
            simulation = ForestFireSimulations(size, density, num_simulations, ignition_location, 
                                              env_index, wind, plant_tree_proportion, 
                                              tree_burn_time, plant_burn_time, ignition_num=self.ignition_num, 
                                              random_seed=self.random_seed)
            simulation.run_simulations()

            simulation.plot_burnt_distribution()
            simulation.plot_burnt_distribution_log_log()

            self.burnt_prop = simulation.proportion_burns_left_to_right()
            self.burnt_prop_label = Label(master, text=f"Proportion of burns left to right: ")
            self.burnt_prop_label.grid(row=0, column=0)

        elif sim_type == 'multiple density, multiple sim':
            density_values = np.linspace(0.01, 1, 100)

            simulation = DensityForestFireSimulations(size, num_simulations, ignition_location, 
                                                    env_index, wind, plant_tree_proportion, 
                                                    tree_burn_time, plant_burn_time, ignition_num=self.ignition_num, 
                                                    random_seed=self.random_seed)

            density_results = simulation.run_density_simulations(density_values)

            simulation.plot_density_vs_burnt(density_results)

            self.density_range_label = Label(master, text="Density range: 0.01 to 1")
            self.density_range_label.grid(row=0, column=0)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=4, column=0)
        