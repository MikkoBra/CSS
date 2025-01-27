from tkinter import Tk, Label, BooleanVar, Radiobutton, Entry, Button, Toplevel

from gui.output_window import OutputWindow

class SaveSingleSim:
    def __init__(self, master, size, env_index, plant_tree_proportion, 
                 tree_burn_time, plant_burn_time, ignition_location, sim_type, 
                 wind, use_seed, ignition_num=None, num_simulations=None, 
                 density=None, random_seed=None, display_single=None):
        
        self.master = master
        master.title("Save Single Simulation")

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

        self.must_wait_label = Label(master, text="The Simulation must finish before saving occurs")
        self.must_wait_label.pack()

        if display_single == "yes":
            self.save_single_option_label = Label(master, text="Save single simulation?")
            self.save_single_option_label.pack()
            self.save_single_option = BooleanVar()
            self.save_single_option.set(False)
            self.save_single_option_yes = Radiobutton(master, text="Yes", variable=self.save_single_option, value=True)
            self.save_single_option_yes.pack()
            self.save_single_option_no = Radiobutton(master, text="No", variable=self.save_single_option, value=False)
            self.save_single_option_no.pack()

            self.save_name_label = Label(master, text="Enter the name of the output file:")
            self.save_name_label.pack()
            self.save_name_entry = Entry(master)
            self.save_name_entry.insert(0, "Forest_fire_sim.gif")
            self.save_name_entry.pack()
        
        self.start_button = Button(master, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()


    def start_simulation(self):
        self.master.withdraw()

        output_window = Toplevel(self.master)
        OutputWindow(
            output_window,
            self.size,
            self.env_index,
            self.plant_tree_proportion,
            self.tree_burn_time,
            self.plant_burn_time,
            self.ignition_location,
            self.sim_type,
            self.wind,
            self.use_seed,
            self.ignition_num,
            self.num_simulations,
            self.density,
            self.random_seed,
            self.display_single,
            self.save_single_option.get() if self.display_single == "yes" else None,
            self.save_name_entry.get() if self.display_single == "yes" else None
        )