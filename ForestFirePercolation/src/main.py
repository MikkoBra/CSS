import numpy as np
from model import ForestFireModel
from simulations import ForestFireSimulations
from density_sims import DensityForestFireSimulations

def main():
    size = int(input("Enter the size of the forest (e.g., 50 for a 50x50 grid): "))
    plant_tree_proportion = float(input("Enter the proportion of plants to trees (0 to 1): "))
    wind = input("Is there wind in the forest? (False/True): ").lower() == 'true'
    tree_burn_time = int(input("Enter the burn time for trees: "))
    plant_burn_time = int(input("Enter the burn time for plants: "))
    env_index = float(input("How strong are the environmental influences? (0 worst for the fire, 1 optimal for fire): "))
    ignition_location = input("Enter ignition location (random, center, corner): ").lower()
    simulation_type = input("Run a a single simulation, multiple for a single density, or a range of densities? (single, multiple, range): ").lower()
    use_seed = input("Use a seed for random number generation? (yes/no): ").lower() == 'yes'

    if use_seed:
        seed = int(input("Enter the seed: "))
    else:
        seed = None

    if simulation_type == "multiple":
        p = float(input("Enter forest density percentage (0 to 1): "))
        num_simulations = int(input("Enter the number of simulations: "))

        if ignition_location != "random":
            ignition_num = 0
        else:
            ignition_num = int(input("Enter the number of trees to ignite: "))

        simulation = ForestFireSimulations(size, p, num_simulations, ignition_location,  env_index, wind, plant_tree_proportion, tree_burn_time, ignition_num)
        simulation.run_simulations()

        simulation.plot_burnt_distribution()
        simulation.plot_burnt_distribution_log_log()
        print(simulation.proportion_burns_left_to_right())

    elif simulation_type == "single":
        p = float(input("Enter forest density percentage (0 to 1): "))
        if ignition_location == "random":
            ignition_num = int(input("Enter the number of trees to ignite: "))
            model = ForestFireModel(size, p, env_index, wind, plant_tree_proportion, tree_burn_time, plant_burn_time, ignition_num)
            model.ignite_fire_random()
        elif ignition_location == "corner":
            model = ForestFireModel(size, p, env_index, wind, plant_tree_proportion, tree_burn_time, plant_burn_time)
            model.ignite_fire_corner()
        elif ignition_location == "center":
            model = ForestFireModel(size, p, env_index, wind, plant_tree_proportion, tree_burn_time, plant_burn_time)
            model.ignite_fire_center()

        display = input("Display simulation? (yes/no): ").lower()
        if display == "yes":
            model.display_single_simulation()
        else:
            model.no_display_single_simulation()

        print("Number of trees: ", model.get_num_trees())
        print("Number of burning trees: ", model.get_num_burning())
        print("Number of burnt trees: ", model.get_num_burnt())
        print("Burns left to right: ", model.burns_left_to_right())
    elif simulation_type == "range":
        num_simulations = int(input("Enter the number of simulations per density value: "))

        if ignition_location != "random":
            ignition_num = 0
        else:
            ignition_num = int(input("Enter the number of trees to ignite: "))

        density_simulations = DensityForestFireSimulations(size, num_simulations, ignition_location, env_index, wind, plant_tree_proportion, tree_burn_time, ignition_num)

        density_values = np.linspace(0.01, 1, 100)
        
        density_results = density_simulations.run_density_simulations(density_values)

        density_simulations.plot_density_vs_burnt(density_results)


if __name__ == "__main__":
    main()
