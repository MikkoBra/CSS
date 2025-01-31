from tkinter import Tk, Label, Entry, IntVar, StringVar, OptionMenu, Button, Toplevel
from ForestFirePercolation.src.gui.run_single_sim_gui import RunSingleSimGUI
from ForestFirePercolation.src.gui.save_single_sim_gui import SaveSingleSimGUI

"""
Class to input additional conditional parameters for the simulation.
Includes specifying the number of random ignition points, the number of simulations, and the seed.
Also includes the option to display the simulation.
Inputs are conditionally based on previous window inputs

Attributes:
    master (Tk): The main window of the application.
    size (int): The size of the forest.
    density (float): The density of the forest.
    env_index (float): The environmental index.
    plant_tree_proportion (float): The proportion of trees to plants.
    tree_burn_time (int): The time taken for a tree to burn.
    plant_burn_time (int): The time taken for a plant to burn.
    ignition_location (str): The location of the ignition point ('random', 'corner', 'center').
    sim_type (str): The type of simulation to run.
    wind (bool): Whether wind is present.
    use_seed (bool): Whether to use a seed for the simulation.

Methods:
    start_simulation: Start the simulation with the specified parameters.
    specify_sim_save: Specify the simulation and save the results.

Connects to:
    RunSingleSim
    SaveSingleSim
"""
class InputConditionalsGUI:
    def __init__(self, master, size, density, env_index, plant_tree_proportion, 
                 tree_burn_time, plant_burn_time, ignition_location, sim_type, 
                 wind, use_seed):
        self.master = master
        master.title("Additional Settings")

        current_row = 0
        self.size = size
        self.density = density
        self.env_index = env_index
        self.plant_tree_proportion = plant_tree_proportion
        self.tree_burn_time = tree_burn_time
        self.plant_burn_time = plant_burn_time
        self.ignition_location = ignition_location
        self.sim_type = sim_type
        self.wind = wind
        self.use_seed = use_seed

        self.size_label = Label(master, text=f"Size: {size}")
        self.size_label.grid(row=current_row, column=0, columnspan=2)

        self.density_label = Label(master, text=f"Density: {density}")
        self.density_label.grid(row=current_row, column=0, columnspan=2)
        current_row += 1

        self.env_index_label = Label(master, text=f"Environment Index: {env_index}")
        self.env_index_label.grid(row=current_row, column=0, columnspan=2)
        current_row += 1

        self.plant_tree_proportion_label = Label(master, text=f"Plant Tree Proportion: {plant_tree_proportion}")
        self.plant_tree_proportion_label.grid(row=current_row, column=0, columnspan=2)
        current_row += 1

        self.tree_burn_time_label = Label(master, text=f"Tree Burn Time: {tree_burn_time}")
        self.tree_burn_time_label.grid(row=current_row, column=0, columnspan=2)
        current_row += 1

        self.plant_burn_time_label = Label(master, text=f"Plant Burn Time: {plant_burn_time}")
        self.plant_burn_time_label.grid(row=current_row, column=0, columnspan=2)
        current_row += 1

        self.ignition_location_label = Label(master, text=f"Ignition Location: {ignition_location}")
        self.ignition_location_label.grid(row=current_row, column=0, columnspan=2)
        current_row += 1

        self.sim_type_label = Label(master, text=f"Simulation Type: {sim_type}")
        self.sim_type_label.grid(row=current_row, column=0, columnspan=2)
        current_row += 1

        self.wind_label = Label(master, text=f"Wind: {wind}")
        self.wind_label.grid(row=current_row, column=0, columnspan=2)
        current_row += 1

        self.use_seed_label = Label(master, text=f"Use Seed: {use_seed}")
        self.use_seed_label.grid(row=current_row, column=0, columnspan=2)
        current_row += 1

        current_row += 1

        if ignition_location == 'random':
            self.ignition_num_label = Label(master, text="Enter the number of random ignition points:")
            self.ignition_num_label.grid(row=current_row, column=0)
            self.ignition_num_entry = Entry(master)
            self.ignition_num_entry.grid(row=current_row, column=1)
            current_row += 1
        else:
            self.ignition_num_entry = None

        if sim_type in ('single density, multiple sim', 'multiple density, multiple sim'):
            self.num_simulations_label = Label(master, text="Enter the number of simulations:")
            self.num_simulations_label.grid(row=current_row, column=0)
            self.num_simulations_var = IntVar()
            self.num_simulations_entry = Entry(master, textvariable=self.num_simulations_var)
            self.num_simulations_entry.grid(row=current_row, column=1)
            current_row += 1
        else:
            self.num_simulations_var = None

        if use_seed:
            self.seed_label = Label(master, text="Enter the seed:")
            self.seed_label.grid(row=current_row, column=0)
            self.seed_entry = Entry(master)
            self.seed_entry.grid(row=current_row, column=1)
            current_row += 1
        else:
            self.seed_entry = None

        if sim_type == "single density, single sim":
            self.display_label = Label(master, text="Display simulation?")
            self.display_label.grid(row=current_row, column=0)
            self.display_var = StringVar()
            self.display_var.set("yes")
            self.display_menu = OptionMenu(master, self.display_var, "yes", "no")
            self.display_menu.grid(row=current_row, column=1)
            current_row += 1

            self.next_button = Button(master, text="Next", command=self.specify_sim_save)
            self.next_button.grid(row=current_row, column=0, columnspan=2, pady=10)
        else:
            self.display_var = None
        
            self.start_button = Button(master, text="Start Simulation", command=self.start_simulation)
            self.start_button.grid(row=current_row, column=0, columnspan=2, pady=10)

    def start_simulation(self):
        self.master.withdraw()

        ignition_num = int(self.ignition_num_entry.get()) if self.ignition_num_entry else None
        num_simulations = int(self.num_simulations_var.get()) if self.num_simulations_var else None
        seed = int(self.seed_entry.get()) if self.seed_entry else None
        display = self.display_var.get() if self.display_var else None

        run_single_sim = Toplevel(self.master)
        RunSingleSimGUI(
            run_single_sim,
            self.size,
            self.env_index,
            self.plant_tree_proportion,
            self.tree_burn_time,
            self.plant_burn_time,
            self.ignition_location,
            self.sim_type,
            self.wind,
            self.use_seed,
            ignition_num,
            num_simulations,
            self.density,
            seed,
            display
        )

    def specify_sim_save(self):
        self.master.withdraw()

        ignition_num = int(self.ignition_num_entry.get()) if self.ignition_num_entry else None
        num_simulations = int(self.num_simulations_var.get()) if self.num_simulations_var else None
        seed = int(self.seed_entry.get()) if self.seed_entry else None
        display = self.display_var.get() if self.display_var else None

        next_window = Toplevel(self.master)
        SaveSingleSimGUI(
            next_window,
            self.size,
            self.env_index,
            self.plant_tree_proportion,
            self.tree_burn_time,
            self.plant_burn_time,
            self.ignition_location,
            self.sim_type,
            self.wind,
            self.use_seed,
            ignition_num,
            num_simulations,
            self.density,
            seed,
            display
        )