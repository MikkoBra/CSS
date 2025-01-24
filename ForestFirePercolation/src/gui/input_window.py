from tkinter import *
from gui.conditional_window import ConditionalWindow

class InputWindow:
    def __init__(self, master):
        self.master = master
        master.title("Forest Fire Simulation - Input")

        self.size_label = Label(master, text="Enter the size of the forest\n(e.g., 50 for a 50x50 grid):")
        self.size_label.pack()
        self.size_entry = Entry(master)
        self.size_entry.insert(0, "100")
        self.size_entry.pack()

        self.env_index_label = Label(master, text="Enter the overall probability for fire ignition:")
        self.env_index_label.pack()
        self.env_index = DoubleVar()
        self.env_index_scale = Scale(master, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, variable=self.env_index)
        self.env_index_scale.pack()

        self.plant_tree_proportion_label = Label(master, text="Enter the proportion of plants to trees (0 to 1):")
        self.plant_tree_proportion_label.pack()
        self.plant_tree_proportion = DoubleVar()
        self.plant_tree_proportion_scale = Scale(master, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, variable=self.plant_tree_proportion)
        self.plant_tree_proportion_scale.pack()

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

        self.ignition_location_label = Label(master, text="Select ignition location:")
        self.ignition_location_label.pack()
        self.ignition_location = StringVar(master)
        self.ignition_location.set("center")  # default value
        self.ignition_location_menu = OptionMenu(master, self.ignition_location, "center", "corner", "random")
        self.ignition_location_menu.pack()

        self.simulation_type_label = Label(master, text="Select simulation type:")
        self.simulation_type_label.pack()
        self.simulation_type = StringVar(master)
        self.simulation_type.set("single density, single sim")  # default value
        self.simulation_type_menu = OptionMenu(master, self.simulation_type, "single density, single sim", "single density, multiple sim", "multiple density, multiple sim")
        self.simulation_type_menu.pack()

        self.wind_option_label = Label(master, text="Enable eastward wind:")
        self.wind_option_label.pack()
        self.wind_option = BooleanVar()
        self.wind_option_checkbutton = Checkbutton(master, text="Wind", variable=self.wind_option)
        self.wind_option_checkbutton.pack()

        self.use_random_seed_label = Label(master, text="Use a seed for random number generation:")
        self.use_random_seed_label.pack()
        self.use_random_seed = BooleanVar()
        self.use_random_seed_checkbutton = Checkbutton(master, text="Seed", variable=self.use_random_seed)
        self.use_random_seed_checkbutton.pack()

        self.next_button = Button(master, text="Next", command=self.open_next_window)
        self.next_button.pack()

    def open_next_window(self):
        self.master.withdraw()

        conditional_window = Toplevel(self.master)
        ConditionalWindow(
            conditional_window,
            int(self.size_entry.get()),
            float(self.env_index.get()),
            float(self.plant_tree_proportion.get()),
            int(self.tree_burn_time_entry.get()),
            int(self.plant_burn_time_entry.get()),
            self.ignition_location.get(),
            self.simulation_type.get(),
            self.wind_option.get(),
            self.use_random_seed.get()
        )

