import gc

from ForestFirePercolation.src.model import ForestFireModel
from tqdm import tqdm
from ForestFirePercolation.src.csv_access.csv_writer import write_to_csv

def multi_param_multi_sim(sizes, 
                          densities, 
                          test_wind, 
                          env_indixes, 
                          plant_tree_proportions,  
                          tree_burn_times, 
                          plant_burn_times,
                          file_name, 
                          num_simulations_per_setting=1,
                          batch_size=1000):
    """
    Function to run simulations and write the results to a CSV file.

    Parameters:
        sizes (List[int]): List of sizes to simulate.
        densities (List[float]): List of densities to simulate.
        test_wind (str): The wind condition to simulate.
        env_indixes (List[float]): List of environmental indexes to simulate.
        plant_tree_proportions (List[float]): List of plant tree proportions to simulate.
        tree_burn_times (List[int]): List of tree burn times to simulate.
        file_name (str): The name of the output CSV file.
        num_simulations_per_setting (int): The number of simulations to run for each parameter setting.
        batch_size (int): The number of simulations to write to the CSV file at a time.
    """
    
    # Field names for the CSV file
    fields = ['size', 'density', 'wind', 'env_index', 'plant_tree_proportion', 'tree_burn_time', 'plant_burn_time', 'percolation', 'percentage burnt down']
    
    # List to store rows of data
    rows = []

    # Simulation count
    simulation_count = 0

    # Set wind conditions
    if test_wind == "Wind":
        winds = [True]
    if test_wind == "No Wind":
        winds = [False]
    elif test_wind == "Both":
        winds = [False, True]

    # Total number of simulations
    total_simulations = (len(sizes) * 
                         len(densities) * 
                         len(winds) * 
                         len(env_indixes) * 
                         len(plant_tree_proportions) * 
                         len(tree_burn_times) * 
                         len(plant_burn_times) *
                         num_simulations_per_setting)

    with tqdm(total=total_simulations, desc="Simulations") as pbar: # Uses tqdm to display a progress bar
        for size in sizes:
            for density in densities:
                for wind in winds:
                    for env_index in env_indixes:
                        for plant_tree_proportion in plant_tree_proportions:
                            for tree_burn_time in tree_burn_times:
                                for plant_burn_time in plant_burn_times:
                                    for _ in range(num_simulations_per_setting):
                                        # Create a new model
                                        model = ForestFireModel(size, 
                                                                density, 
                                                                env_index, 
                                                                wind, 
                                                                plant_tree_proportion, 
                                                                tree_burn_time, 
                                                                plant_burn_time)

                                        # Get the initial total number of trees
                                        num_trees_total = model.get_num_vegetation()

                                        # Ignite the fire
                                        model.ignite_fire_center()

                                        # Run the simulation without displaying it
                                        model.no_display_single_simulation()

                                        # Get the percolation and percentage burnt down
                                        percolation = model.burns_left_to_right()
                                        num_burnt = model.get_num_burnt()
                                        burnt_perc = num_burnt / num_trees_total if num_trees_total > 0 else 0

                                        # Append the results to the rows list
                                        rows.append([size, 
                                                     density, 
                                                     wind, 
                                                     env_index, 
                                                     plant_tree_proportion, 
                                                     tree_burn_time, 
                                                     plant_burn_time, 
                                                     percolation, 
                                                     burnt_perc])

                                        simulation_count += 1

                                        # Update the progress bar
                                        pbar.update(1)

                                        # Batch csv write and garbage collection
                                        if simulation_count % batch_size == 0:
                                            write_to_csv(file_name, 
                                                         fields, rows, 
                                                         simulation_count == batch_size)
                                            rows.clear()
                                            gc.collect()

        # Write remaining rows to CSV file
        if rows:
            write_to_csv(file_name, fields, rows, simulation_count <= batch_size)

        # Final garbage collection
        gc.collect()