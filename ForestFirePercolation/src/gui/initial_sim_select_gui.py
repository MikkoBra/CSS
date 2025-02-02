from tkinter import Tk, Button, Toplevel
from ForestFirePercolation.src.gui.input_param_single_gui import InputParameterSingleGUI
from ForestFirePercolation.src.gui.input_param_range_gui import InputParameterRangeGUI

"""
Class to select the type of simulation to run.

Attributes:
    master (Tk): The main window of the application.

Methods:
    single_sim: Run a single density, single simulation.
    multi_sim: Run a single density, multiple simulations.
    range_multi_sim: Run simulations over a range of parameters.

Connects to:
    InputParameterSingle
    InputParameterRange
"""
class InitialSimSelectionGUI:
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
        input_parameter_single = Toplevel(self.master)

        InputParameterSingleGUI(input_parameter_single, "single density, single sim")

    def multi_sim(self):
        self.master.withdraw()
        input_parameter_single = Toplevel(self.master)

        InputParameterSingleGUI(input_parameter_single, "single density, multiple sim")


    def range_multi_sim(self):
        self.master.withdraw()
        input_parameter_range = Toplevel(self.master)
        InputParameterRangeGUI(input_parameter_range)