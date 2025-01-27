from tkinter import Tk, Button, Toplevel
from gui.input_window import InputWindow
from gui.full_sim_specification import FullSimSpecification

class SimSelection:
    def __init__(self, master):
        self.master = master
        master.title("Simulation Selection")

        self.single_sim_button = Button(master, text="Single Density, Single Simulation", command=self.single_sim)
        self.single_sim_button.pack()

        self.multi_sim_button = Button(master, text="Single Density, Multiple Simulations", command=self.multi_sim)
        self.multi_sim_button.pack()

        self.range_multi_sim_button = Button(master, text="Simulate Parameter Range", command=self.range_multi_sim)
        self.range_multi_sim_button.pack()

    def single_sim(self):
        self.master.withdraw()
        input_window = Toplevel(self.master)

        InputWindow(input_window, "single density, single sim")

    def multi_sim(self):
        self.master.withdraw()
        input_window = Toplevel(self.master)

        InputWindow(input_window, "single density, multiple sim")


    def range_multi_sim(self):
        self.master.withdraw()
        full_sim_specification = Toplevel(self.master)
        FullSimSpecification(full_sim_specification)

    
