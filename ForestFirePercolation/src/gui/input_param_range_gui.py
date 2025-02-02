import tkinter as tk
from tkinter import BooleanVar, Toplevel, Label, messagebox

from ForestFirePercolation.src.gui.run_range_sims_gui import RunRangeOfSimsGUI

"""
Class to input a range of parameters.
Includes running multiple simulations with the specified ranges of parameters.

Attributes:
    master (Tk): The main window of the application.

Methods:
    start_simulation: Start the simulation with the specified parameters.

Connects to:
    OutputFullSim
"""
class InputParameterRangeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simulation Specification")

        self.sizes_label = tk.Label(master, text="Enter forest sizes (comma-separated):")
        self.sizes_label.pack()
        self.sizes_entry = tk.Entry(master)
        self.sizes_entry.insert(0, "100,250,500,1000")
        self.sizes_entry.pack()

        self.densities_label = tk.Label(master, text="Enter forest densities (comma-separated):")
        self.densities_label.pack()
        self.densities_entry = tk.Entry(master)
        self.densities_entry.insert(0, "0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0")
        self.densities_entry.pack()
        
        self.env_indexes_label = tk.Label(master, text="Enter environmental indices (comma-separated):")
        self.env_indexes_label.pack()
        self.env_indexes_entry = tk.Entry(master)
        self.env_indexes_entry.insert(0, "0.25,0.5,0.75,1.0")
        self.env_indexes_entry.pack()

        self.plant_tree_proportions_label = tk.Label(master, text="Enter plant/tree proportions (comma-separated):")
        self.plant_tree_proportions_label.pack()
        self.plant_tree_proportions_entry = tk.Entry(master)
        self.plant_tree_proportions_entry.insert(0, "0.0,0.5,1.0")
        self.plant_tree_proportions_entry.pack()

        self.tree_burn_times_label = tk.Label(master, text="Enter tree burn times (comma-separated):")
        self.tree_burn_times_label.pack()
        self.tree_burn_times_entry = tk.Entry(master)
        self.tree_burn_times_entry.insert(0, "1,3,5,10")
        self.tree_burn_times_entry.pack()

        self.plant_burn_times_label = tk.Label(master, text="Enter plant burn times (comma-separated):")
        self.plant_burn_times_label.pack()
        self.plant_burn_times_entry = tk.Entry(master)
        self.plant_burn_times_entry.insert(0, "1,3,5,10")
        self.plant_burn_times_entry.pack()

        self.wind_options_label = tk.Label(master, text="Eastward wind options:")
        self.wind_options_label.pack()
        self.wind_options = ["Wind", "No Wind", "Both"]
        self.wind_var = tk.StringVar(master)
        self.wind_var.set(self.wind_options[0])
        self.wind_menu = tk.OptionMenu(master, self.wind_var, *self.wind_options)
        self.wind_menu.pack()

        self.num_simulations_label = tk.Label(master, text="Enter the number of simulations per setting:")
        self.num_simulations_label.pack()
        self.num_simulations_entry = tk.Entry(master)
        self.num_simulations_entry.insert(0, "1")
        self.num_simulations_entry.pack()

        self.run_parallel_label = tk.Label(master, text="Run simulations in parallel using logical processors:")
        self.run_parallel_label.pack()
        self.run_parallel = BooleanVar()
        self.run_parallel_checkbutton = tk.Checkbutton(master, text="Parallel", variable=self.run_parallel)
        self.run_parallel_checkbutton.pack()

        self.file_name_label = tk.Label(master, text="Enter the name of the output file:")
        self.file_name_label.pack()
        self.file_name_entry = tk.Entry(master)
        self.file_name_entry.insert(0, "Simulation_data.csv")
        self.file_name_entry.pack()


        self.start_button = tk.Button(master, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()

    def start_simulation(self):
        try:
            sizes = [int(size) for size in self.sizes_entry.get().split(",")]
            densities = [float(density) for density in self.densities_entry.get().split(",")]
            env_indexes = [float(env_index) for env_index in self.env_indexes_entry.get().split(",")]
            plant_tree_proportions = [float(plant_tree_proportion) for plant_tree_proportion in self.plant_tree_proportions_entry.get().split(",")]
            tree_burn_times = [int(tree_burn_time) for tree_burn_time in self.tree_burn_times_entry.get().split(",")]
            plant_burn_times = [int(plant_burn_time) for plant_burn_time in self.plant_burn_times_entry.get().split(",")]
            file_name = self.file_name_entry.get()
            test_wind = self.wind_var.get()
            num_simulations_per_setting = int(self.num_simulations_entry.get())
            run_parallel = self.run_parallel.get()

            error = False

            if any(size <= 0 for size in sizes):
                error = True
                raise ValueError("Forest sizes must be positive integers.")
            if any(density < 0 or density > 1 for density in densities):
                error = True
                raise ValueError("Forest densities must be between 0 and 1.")
            if any(env_index < 0 or env_index > 1 for env_index in env_indexes):
                error = True
                raise ValueError("Environmental indices must be between 0 and 1.")
            if any(plant_tree_proportion < 0 or plant_tree_proportion > 1 for plant_tree_proportion in plant_tree_proportions):
                error = True
                raise ValueError("Plant/tree proportions must be between 0 and 1.")
            if any(tree_burn_time <= 0 for tree_burn_time in tree_burn_times):
                error = True
                raise ValueError("Tree burn times must be positive integers.")
            if any(plant_burn_time <= 0 for plant_burn_time in plant_burn_times):
                error = True
                raise ValueError("Plant burn times must be positive integers.")
            if num_simulations_per_setting <= 0:
                error = True
                raise ValueError("Number of simulations per setting must be a positive integer.")
            if not file_name.endswith(".csv"):
                error = True
                raise ValueError("Output file name must end with .csv")
            
            if not error:
                self.master.withdraw()

                run_range_of_sims = Toplevel(self.master)
                RunRangeOfSimsGUI(
                    run_range_of_sims,
                    sizes,
                    densities,
                    test_wind,
                    env_indexes,
                    plant_tree_proportions,
                    tree_burn_times,
                    plant_burn_times,
                    run_parallel,
                    file_name,
                    num_simulations_per_setting
            )
        except ValueError as e:
            tk.messagebox.showerror("Invalid input", f"Invalid input: {e}. Please check your inputs.")

        
