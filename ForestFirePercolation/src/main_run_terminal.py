from ForestFirePercolation.src.model import ForestFireModel
from ForestFirePercolation.src.single_param_multi_sim import SingleParamMultiSim
from ForestFirePercolation.src.multi_param_multi_sim_parallel import multi_param_multi_sim_parallel
from ForestFirePercolation.src.multi_param_multi_sim import multi_param_multi_sim

"""
Main function to run the Forest Fire Percolation model in the terminal.
"""
def main():
    # Get user input for simulation type
    while True:
        try:
            simulation_type = input("Run a a single simulation for a single parameter set, multiple sims for a single parameter set, or multiple sims for a range of parameters? (single, multiple, range): ").lower()
            if simulation_type not in ["single", "multiple", "range"]:
                raise ValueError("Invalid input. Please enter 'single', 'multiple', or 'range'.")
            break
        except ValueError as e:
            print(e)


    # Get parameter inputs for range of parameters simulation
    if simulation_type == "range":
        print("Separate values with commas for range inputs.")
        while True:
            try:
                size_range = input("Enter a range of sizes for the forest grid (comma separated): ")
                size_range = [int(size) for size in size_range.split(',')]
                for size in size_range:
                    if size < 1:
                        raise ValueError("Invalid input. Please enter a list of integers greater than 0.")
                break
            except ValueError:
                print("Invalid input. Please enter a comma separated list of integers.")
        
        while True:
            try:
                density_range = input("Enter a range of forest density percentages (0.0 to 1.0): ")
                density_range = [float(p) for p in density_range.split(',')]
                for p in density_range:
                    if p < 0 or p > 1:
                        raise ValueError("Invalid input. Please enter a list of floats between 0 and 1.")
                break
            except ValueError:
                print("Invalid input. Please enter a comma separated list of floats.")
        
        while True:
            try:
                env_index = input("Enter a range of Spreading Probabilities (0.0 to 1.0): ")
                env_index = [float(p) for p in env_index.split(',')]
                for p in env_index:
                    if p < 0 or p > 1:
                        raise ValueError("Invalid input. Please enter a list of floats between 0 and 1.")
                break
            except ValueError:
                print("Invalid input. Please enter a comma separated list of floats.")

        while True:
            try:
                plant_tree_proportion = input("Enter a range of plants to trees (0.0 for all trees, 1.0 for all plants): ")
                plant_tree_proportion = [float(p) for p in plant_tree_proportion.split(',')]
                for p in plant_tree_proportion:
                    if p < 0 or p > 1:
                        raise ValueError("Invalid input. Please enter a list of floats between 0 and 1.")
                break
            except ValueError:
                print("Invalid input. Please enter a comma separated list of floats.")

        while True:
            try:
                tree_burn_time = input("Enter a range of time steps trees burn: ")
                tree_burn_time = [int(t) for t in tree_burn_time.split(',')]
                for t in tree_burn_time:
                    if t < 1:
                        raise ValueError("Invalid input. Please enter a list of integers greater than 0.")
                break
            except ValueError:
                print("Invalid input. Please enter a comma separated list of integers.")

        while True:
            try:
                plant_burn_time = input("Enter a range of time steps plants burn: ")
                plant_burn_time = [int(t) for t in plant_burn_time.split(',')]
                for t in plant_burn_time:
                    if t < 1:
                        raise ValueError("Invalid input. Please enter a list of integers greater than 0.")
                break
            except ValueError:
                print("Invalid input. Please enter a comma separated list of integers.")

        while True:
            try:
                wind = input("Simulate wind, no wind, or both? (yes/no/both): ").lower()
                if wind not in ["yes", "no", "both"]:
                    raise ValueError("Invalid input. Please enter 'yes', 'no', or 'both'.")
                if wind == "both":
                    wind = "Both"
                elif wind == "yes":
                    wind = "Wind"
                elif wind == "no":
                    wind = "No Wind"
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                num_simulations = int(input("Enter the number of simulations per parameter set: "))
                if num_simulations < 1:
                    raise ValueError("Invalid input. Please enter an integer greater than 0.")
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                file_name = input("Enter the name of the output csv file (Include .csv): ")
                if file_name[-4:] != ".csv":
                    raise ValueError("Invalid input. Please enter a valid csv file name.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid csv file name.")
        
        while True:
            try:
                parallel_option = input("Run simulations in parallel? (yes/no): ").lower()
                if parallel_option not in ["yes", "no"]:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                if parallel_option == "yes":
                    parallel_option = True
                else:
                    parallel_option = False
                break
            except ValueError:
                print("Invalid input. Please enter 'yes' or 'no'.")

    # Get parameter inputs for single parameter set simulations
    else:
        while True:
            try:
                size = int(input("Enter the size of the forest (e.g., 50 for a 50x50 grid): "))
                if size < 1:
                    raise ValueError("Invalid input. Please enter an integer greater than 0.")
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        while True:
            try:
                density = float(input("Enter the forest density percentage (0 to 1): "))
                if density < 0 or density > 1:
                    raise ValueError("Invalid input. Please enter a float between 0 and 1.")
                break
            except ValueError:
                print("Invalid input. Please enter a float.")
        while True:
            try:
                env_index = float(input("Enter the fire spreading probability (0 to 1): "))
                if env_index < 0 or env_index > 1:
                    raise ValueError("Invalid input. Please enter a float between 0 and 1.")
                break
            except ValueError:
                print("Invalid input. Please enter a float.")
        while True:
            try:
                plant_tree_proportion = float(input("Enter the proportion of plants to trees (0 to 1): "))
                if plant_tree_proportion < 0 or plant_tree_proportion > 1:
                    raise ValueError("Invalid input. Please enter a float between 0 and 1.")
                break
            except ValueError:
                print("Invalid input. Please enter a float.")
        while True:
            try:
                tree_burn_time = int(input("Enter the burn time for trees: "))
                if tree_burn_time < 1:
                    raise ValueError("Invalid input. Please enter an integer greater than 0.")
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        while True:
            try:
                plant_burn_time = int(input("Enter the burn time for plants: "))
                if plant_burn_time < 1:
                    raise ValueError("Invalid input. Please enter an integer greater than 0.")
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        while True:
            try:
                wind = input("Is there wind in the forest? (yes/no): ").lower()
                if wind not in ["yes", "no"]:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                if wind == "yes":
                    wind = True
                else:
                    wind = False
                break
            except ValueError:
                print("Invalid input. Please enter True or False.")
        # Get user input for initial ignition location
        while True:
            try:
                ignition_location = input("Enter ignition location (random, center, corner): ").lower()
                if ignition_location not in ["random", "center", "corner"]:
                    raise ValueError("Invalid input. Please enter 'random', 'center', or 'corner'.")
                break
            except ValueError as e:
                print(e)
        
        # If ignition location is random, get number of trees to ignite
        if ignition_location == "random":
            while True:
                try:
                    ignition_num = int(input("Enter the number of trees to ignite: "))
                    if ignition_num < 1:
                        raise ValueError("Invalid input. Please enter an integer greater than 0.")
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        else:
            ignition_num = 0
    
        # Number of simulations for multiple simulations and single parameter set
        if simulation_type == "multiple":
            while True:
                try:
                    num_simulations = int(input("Enter the number of simulations: "))
                    if num_simulations < 1:
                        raise ValueError("Invalid input. Please enter an integer greater than 0.")
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        elif simulation_type == "single":
            # Get user input for random seed option
            while True:
                try:
                    use_seed = input("Use a seed for random number generation? (yes/no): ").lower()
                    if use_seed not in ["yes", "no"]:
                        raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                    if use_seed == "yes":
                        use_seed = True
                    else:
                        use_seed = False
                    break
                except ValueError as e:
                    print(e)
            
            # Seed for random number generation
            if use_seed:
                while True:
                    try:
                        seed = int(input("Enter the seed for random value generation: "))
                        if seed < 0:
                            raise ValueError("Invalid input. Please enter an integer greater than 0.")
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
            else:
                seed = None


    print("Running simulations...")


    # Run Simulations with input parameters
    if simulation_type == "range":
        print("Simulation type: ", simulation_type)
        print("Size: ", size)
        print("Density: ", density_range)
        print("Spreading Probability: ", env_index)
        print("Plant to tree proportion: ", plant_tree_proportion)
        print("Tree burn time: ", tree_burn_time)
        print("Plant burn time: ", plant_burn_time)
        print("Wind: ", wind)
        print("Number of simulations: ", num_simulations)

        if parallel_option:
            simulation = multi_param_multi_sim_parallel(size_range, 
                                                        density_range,
                                                        wind, 
                                                        env_index, 
                                                        plant_tree_proportion, 
                                                        tree_burn_time, 
                                                        plant_burn_time, 
                                                        file_name, 
                                                        num_simulations)
        else:
            simulation = multi_param_multi_sim(size_range, 
                                               density_range,
                                               wind, 
                                               env_index, 
                                               plant_tree_proportion, 
                                               tree_burn_time, 
                                               plant_burn_time, 
                                               file_name, 
                                               num_simulations)
        
    elif simulation_type == "multiple":
        print("Simulation type: ", simulation_type)
        print("Ignition location: ", ignition_location)
        print("Size: ", size)
        print("Density: ", density)
        print("Spreading Probability: ", env_index)
        print("Plant to tree proportion: ", plant_tree_proportion)
        print("Tree burn time: ", tree_burn_time)
        print("Plant burn time: ", plant_burn_time)
        print("Wind: ", wind)
        print("Number of simulations: ", num_simulations)
        print("Ignition number: ", ignition_num)

        simulation = SingleParamMultiSim(size, 
                                         density,
                                         num_simulations, 
                                         ignition_location, 
                                         env_index, 
                                         wind, 
                                         plant_tree_proportion, 
                                         tree_burn_time, 
                                         plant_burn_time, 
                                         ignition_num)
        simulation.run_simulations()

        simulation.plot_burnt_distribution()
        simulation.plot_burnt_distribution_log_log()

    elif simulation_type == "single":
        print("Simulation type: ", simulation_type)
        print("Seed: ", seed)
        print("Ignition location: ", ignition_location)
        print("Size: ", size)
        print("Density: ", density)
        print("Spreading Probability: ", env_index)
        print("Plant to tree proportion: ", plant_tree_proportion)
        print("Tree burn time: ", tree_burn_time)
        print("Plant burn time: ", plant_burn_time)
        print("Wind: ", wind)
        print("Ignition number: ", ignition_num)

        while True:
            try:
                display = input("Display simulation? (yes/no): ").lower()
                if display not in ["yes", "no"]:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                break
            except ValueError as e:
                print(e)

        if display == "yes":
            while True:
                try:
                    save = input("Save simulation as a gif? (yes/no): ").lower()
                    if save not in ["yes", "no"]:
                        raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                    break
                except ValueError as e:
                    print(e)
            
            if save == "yes":
                while True:
                    try:
                        save_file = input("Enter the name of the output gif file (Include .gif): ")
                        if save_file[-4:] != ".gif":
                            raise ValueError("Invalid input. Please enter a valid gif file name.")
                        print("Wait for the simulation to finish to save the gif.")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid gif file name.")

        model = ForestFireModel(size, 
                                density,
                                env_index, 
                                wind, 
                                plant_tree_proportion, 
                                tree_burn_time, 
                                plant_burn_time, 
                                ignition_num=ignition_num,
                                random_seed=seed)
        
        if ignition_location == "random":
            model.ignite_fire_random()
        elif ignition_location == "center":
            model.ignite_fire_center()
        elif ignition_location == "corner":
            model.ignite_fire_corner()

        if display == "yes":
            if save == "yes":
                model.display_single_simulation(interval=100, save=True, filename=save_file)
            else:
                model.display_single_simulation()
        else:
            model.no_display_single_simulation()
        

        print("Number of trees: ", model.get_num_trees())
        print("Number of burning trees: ", model.get_num_burning())
        print("Number of burnt trees: ", model.get_num_burnt())
        print("Burns left to right: ", model.burns_left_to_right())

if __name__ == "__main__":
    main()
