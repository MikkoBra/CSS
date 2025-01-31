from tkinter import *

from ForestFirePercolation.src.multi_param_multi_sim import multi_param_multi_sim
from ForestFirePercolation.src.multi_param_multi_sim_parallel import multi_param_multi_sim_parallel

"""
Class to run many simulations with a range of parameters 
and save the results to a CSV file.

Attributes:
    master (Tk): The root Tk object.
    sizes (List[int]): The range of sizes to simulate.
    densities (List[float]): The range of densities to simulate.
    test_wind (str): The wind condition to simulate.
    env_indexes (List[float]): The range of environmental indexes to simulate.
    plant_tree_proportions (List[float]): The range of plant tree proportions to simulate.
    tree_burn_times (List[int]): The range of tree burn times to simulate.
    run_parallel (bool): Whether to run the simulations in parallel.
    file_name (str): The name of the output CSV file.
    num_simulations_per_setting (int): The number of simulations to run for each parameter setting.

Methods:
    finish: Close the window and exit the program.
"""
class RunRangeOfSimsGUI:
    def __init__(self, 
                 master,
                 sizes,
                 densities,
                 test_wind,
                 env_indexes,
                 plant_tree_proportions,
                 tree_burn_times,
                 run_parallel,
                 file_name,
                 num_simulations_per_setting):
        self.master = master
        master.title("Simulation")

        self.sizes = sizes
        self.densities = densities
        self.test_wind = test_wind
        self.env_indexes = env_indexes
        self.plant_tree_proportions = plant_tree_proportions
        self.tree_burn_times = tree_burn_times
        self.file_name = file_name
        self.num_simulations_per_setting = num_simulations_per_setting

        row = 0

        print(sizes, densities, test_wind, env_indexes, plant_tree_proportions, tree_burn_times, file_name, num_simulations_per_setting)

        self.size_range_label = Label(master, text=f"Sizes: {sizes}")
        self.size_range_label.grid(row=row, column=0)
        row += 1

        self.density_range_label = Label(master, text=f"Densities: {densities}")
        self.density_range_label.grid(row=row, column=0)
        row += 1

        self.env_index_range_label = Label(master, text=f"Environment Indexes: {env_indexes}")
        self.env_index_range_label.grid(row=row, column=0)
        row += 1

        self.plant_tree_proportion_range_label = Label(master, text=f"Plant Tree Proportions: {plant_tree_proportions}")
        self.plant_tree_proportion_range_label.grid(row=row, column=0)
        row += 1

        self.tree_burn_time_range_label = Label(master, text=f"Tree Burn Times: {tree_burn_times}")
        self.tree_burn_time_range_label.grid(row=row, column=0)
        row += 1

        self.test_wind_label = Label(master, text=f"Test Wind: {test_wind}")
        self.test_wind_label.grid(row=row, column=0)
        row += 1

        self.num_simulations_label = Label(master, text=f"Number of Simulations per Setting: {num_simulations_per_setting}")
        self.num_simulations_label.grid(row=row, column=0)
        row += 1

        self.file_name_label = Label(master, text=f"Output File Name: {file_name}")
        self.file_name_label.grid(row=row, column=0)
        row += 1

        if run_parallel:
            multi_param_multi_sim_parallel(sizes, densities, test_wind, env_indexes, plant_tree_proportions, tree_burn_times, file_name, num_simulations_per_setting)
        else:
            multi_param_multi_sim(sizes, densities, test_wind, env_indexes, plant_tree_proportions, tree_burn_times, file_name, num_simulations_per_setting)

        self.finish_button = Button(master, text="Finish", command=self.finish)
        self.finish_button.grid(row=row, column=0)
        row += 1

    def finish(self):
        self.master.destroy()
        self.master.quit()
