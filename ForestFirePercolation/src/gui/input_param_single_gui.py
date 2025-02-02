from tkinter import Tk, Label, Entry, DoubleVar, Scale, StringVar, OptionMenu, BooleanVar, Checkbutton, Button, Toplevel, HORIZONTAL
from ForestFirePercolation.src.gui.input_conditionals_gui import InputConditionalsGUI

"""
Class to input a single set of parameters.
Includes running a single simulation with the specified parameters
as well as the option to run multiple simulations with the same parameters.

Attributes:
    master (Tk): The main window of the application.
    simulation_type (str): The type of simulation to run.

Methods:
    open_next_window: Open the next window to input conditional parameters.
    show_error: Display an error message in a new window.

Connects to:
    InputConditionals
"""
class InputParameterSingleGUI:
    def __init__(self, 
                 master, 
                 sim_type):
        self.master = master
        master.title("Forest Fire Simulation - Input")

        self.simulation_type = sim_type

        self.create_size_input(master)
        self.create_density_input(master)
        self.create_env_index_input(master)
        self.create_plant_tree_proportion_input(master)
        self.create_burn_time_inputs(master)
        self.create_ignition_location_input(master)
        self.create_wind_option_input(master)
        print(self.simulation_type)
        self.create_random_seed_input(master)
            
        self.create_next_button(master)

    def create_size_input(self, master):
        self.size_label = Label(master, text="Enter the size of the forest\n(e.g., 100 for a 100x100 grid):")
        self.size_label.pack()
        self.size_entry = Entry(master)
        self.size_entry.insert(0, "100")
        self.size_entry.pack()

    def create_density_input(self, master):
        self.density_label = Label(master, text="Select overall forest density percentage:")
        self.density_label.pack()
        self.density_var = DoubleVar()
        self.density_scale = Scale(master, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, variable=self.density_var, length=200)
        self.density_scale.pack()

    def create_env_index_input(self, master):
        self.env_index_label = Label(master, text="Enter the overall probability for fire ignition:")
        self.env_index_label.pack()
        self.env_index = DoubleVar()
        self.env_index_scale = Scale(master, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, variable=self.env_index, length=200)
        self.env_index_scale.pack()

    def create_plant_tree_proportion_input(self, master):
        self.plant_tree_proportion_label = Label(master, text="Enter the proportion of plants to trees (0 to 1):")
        self.plant_tree_proportion_label.pack()
        self.plant_tree_proportion = DoubleVar()
        self.plant_tree_proportion_scale = Scale(master, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, variable=self.plant_tree_proportion, length=200)
        self.plant_tree_proportion_scale.pack()

    def create_burn_time_inputs(self, master):
        self.tree_burn_time_label = Label(master, text="Enter the burn time for trees:")
        self.tree_burn_time_label.pack()
        self.tree_burn_time_entry = Entry(master)
        self.tree_burn_time_entry.insert(0, "1")
        self.tree_burn_time_entry.pack()

        self.plant_burn_time_label = Label(master, text="Enter the burn time for plants:")
        self.plant_burn_time_label.pack()
        self.plant_burn_time_entry = Entry(master)
        self.plant_burn_time_entry.insert(0, "1")
        self.plant_burn_time_entry.pack()

    def create_ignition_location_input(self, master):
        self.ignition_location_label = Label(master, text="Select ignition location:")
        self.ignition_location_label.pack()
        self.ignition_location = StringVar(master)
        self.ignition_location.set("center")  # default value
        self.ignition_location_menu = OptionMenu(master, self.ignition_location, "center", "corner", "random")
        self.ignition_location_menu.pack()

    def create_wind_option_input(self, master):
        self.wind_option_label = Label(master, text="Enable eastward wind:")
        self.wind_option_label.pack()
        self.wind_option = BooleanVar()
        self.wind_option_checkbutton = Checkbutton(master, text="Wind", variable=self.wind_option)
        self.wind_option_checkbutton.pack()

    def create_random_seed_input(self, master):
        if self.simulation_type == "single density, single sim":
            self.use_random_seed_label = Label(master, text="Use a seed for random number generation:")
            self.use_random_seed_label.pack()
            self.use_random_seed = BooleanVar()
            self.use_random_seed_checkbutton = Checkbutton(master, text="Seed", variable=self.use_random_seed)
            self.use_random_seed_checkbutton.pack()
        else:
            self.use_random_seed = BooleanVar()
            self.use_random_seed.set(False)

    def create_next_button(self, master):
        self.next_button = Button(master, text="Next", command=self.open_next_window)
        self.next_button.pack()

    def open_next_window(self):
            try:
                size = int(self.size_entry.get())
            except ValueError:
                self.show_error("Invalid input for size. Please enter a valid integer.")
                return
    
            try:
                density = float(self.density_var.get())
            except ValueError:
                self.show_error("Invalid input for density. Please enter a valid float.")
                return
    
            try:
                env_index = float(self.env_index.get())
            except ValueError:
                self.show_error("Invalid input for environmental index. Please enter a valid float.")
                return
    
            try:
                plant_tree_proportion = float(self.plant_tree_proportion.get())
            except ValueError:
                self.show_error("Invalid input for plant to tree proportion. Please enter a valid float.")
                return
    
            try:
                tree_burn_time = int(self.tree_burn_time_entry.get())
            except ValueError:
                self.show_error("Invalid input for tree burn time. Please enter a valid integer.")
                return
    
            try:
                plant_burn_time = int(self.plant_burn_time_entry.get())
            except ValueError:
                self.show_error("Invalid input for plant burn time. Please enter a valid integer.")
                return
    
            ignition_location = self.ignition_location.get()
            wind_option = self.wind_option.get()
            use_random_seed = self.use_random_seed.get()
    
            self.master.withdraw()
    
            input_conditionals = Toplevel(self.master)
            InputConditionalsGUI(
                input_conditionals,
                size,
                density,
                env_index,
                plant_tree_proportion,
                tree_burn_time,
                plant_burn_time,
                ignition_location,
                self.simulation_type,
                wind_option,
                use_random_seed
            )
    
    def show_error(self, message):
        error_window = Toplevel(self.master)
        error_label = Label(error_window, text=message)
        error_label.pack()
        close_button = Button(error_window, text="Close", command=error_window.destroy)
        close_button.pack()