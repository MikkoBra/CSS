from tkinter import *

from csv_writer import simulation_to_csv
from csv_writer_parallel import simulation_to_csv_parallel

class OutputFullSim:
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
            simulation_to_csv_parallel(sizes, densities, test_wind, env_indexes, plant_tree_proportions, tree_burn_times, file_name, num_simulations_per_setting)
        else:
            simulation_to_csv(sizes, densities, test_wind, env_indexes, plant_tree_proportions, tree_burn_times, file_name, num_simulations_per_setting)

        self.finish_button = Button(master, text="Finish", command=self.finish)
        self.finish_button.grid(row=row, column=0)
        row += 1

    def finish(self):
        self.master.destroy()
        self.master.quit()
