import numpy as np
from model import ForestFireModel
from simulations import ForestFireSimulations
from density_sims import DensityForestFireSimulations

def main():
    size = int(input("Enter the size of the forest (e.g., 50 for a 50x50 grid): "))
    wind = (input("Is there wind in the forest? (False/True): "))
    env_index = float(input("How strong are the environmental influences? (0 worst for the fire, 1 optimal for fire): "))
    sim_method = input("Enter simulation method (random, center, corner): ")
    simulation_type = input("Run a a single simulation, multiple for a single density, or a range of densities? (single, multiple, range): ")

    if simulation_type == "multiple":
        p = float(input("Enter forest density percentage (0 to 1): "))
        num_simulations = int(input("Enter the number of simulations: "))

        if sim_method != "random":
            ignition_num = 0
        else:
            ignition_num = int(input("Enter the number of trees to ignite: "))

        simulation = ForestFireSimulations(size, p, num_simulations, sim_method,  env_index, wind, ignition_num)
        simulation.run_simulations()

        simulation.plot_burnt_distribution()
        simulation.plot_burnt_distribution_log_log()
        print(simulation.proportion_burns_left_to_right())

    elif simulation_type == "single":
        p = float(input("Enter forest density percentage (0 to 1): "))
        if sim_method == "random":
            ignition_num = int(input("Enter the number of trees to ignite: "))
            model = ForestFireModel(size, p, env_index, wind,ignition_num)
            model.ignite_fire_random()
        elif sim_method == "corner":
            model = ForestFireModel(size, p, env_index, wind)
            model.ignite_fire_corner()
        elif sim_method == "center":
            model = ForestFireModel(size, p, env_index, wind)
            model.ignite_fire_center()

        display = input("Display simulation? (yes/no): ")
        if display == "yes":
            model.display_single_simulation(env_index, wind)
        else:
            model.no_display_single_simulation(env_index, wind)

        print("Number of trees: ", model.get_num_trees())
        print("Number of burning trees: ", model.get_num_burning())
        print("Number of burnt trees: ", model.get_num_burnt())
        print("Burns left to right: ", model.burns_left_to_right())
    elif simulation_type == "range":
        num_simulations = int(input("Enter the number of simulations per density value: "))

        if sim_method != "random":
            ignition_num = 0
        else:
            ignition_num = int(input("Enter the number of trees to ignite: "))

        density_simulations = DensityForestFireSimulations(size, num_simulations, sim_method, ignition_num)

        density_values = np.linspace(0.01, 1, 100)
        
        density_results = density_simulations.run_density_simulations(density_values)

        density_simulations.plot_density_vs_burnt(density_results)


if __name__ == "__main__":
    main()
