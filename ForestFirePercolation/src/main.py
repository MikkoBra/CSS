import numpy as np
import matplotlib.pyplot as plt
from model import ForestFireModel
from simulations import ForestFireSimulations



def main():
    size = int(input("Enter the size of the forest (e.g., 50 for a 50x50 grid): "))
    p = float(input("Enter forest density percentage (0 to 1): "))
    sim_method = input("Enter simulation method (random, center, corner): ")
    single_simulation = input("Run a single simulation? (yes/no): ")

    if single_simulation == "no":
        num_simulations = int(input("Enter the number of simulations: "))

        if sim_method == "random":
            ignition_num = int(input("Enter the number of trees to ignite: "))
            simulation = ForestFireSimulations(size, p, num_simulations, ignition_num)
            simulation.run_simulations_random()
        elif sim_method == "corner":
            simulation = ForestFireSimulations(size, p, num_simulations)
            simulation.run_simulations_corner()
        elif sim_method == "center":
            simulation = ForestFireSimulations(size, p, num_simulations)
            simulation.run_simulations_center()

        simulation.plot_burnt_distribution()

    else:
        steps = int(input("Enter the number of simulation steps: "))
        if sim_method == "random":
            ignition_num = int(input("Enter the number of trees to ignite: "))
            model = ForestFireModel(size, p, ignition_num)
            model.ignite_fire_random()
        elif sim_method == "corner":
            model = ForestFireModel(size, p)
            model.ignite_fire_corner()
        elif sim_method == "center":
            model = ForestFireModel(size, p)
            model.ignite_fire_center()

        display = input("Display simulation? (yes/no): ")
        if display == "yes":
            model.display_simulation(steps)
        else:
            model.run_simulation(steps)

        print("Number of trees: ", model.get_num_trees())
        print("Number of burning trees: ", model.get_num_burning())
        print("Number of burnt trees: ", model.get_num_burnt())

if __name__ == "__main__":
    main()
