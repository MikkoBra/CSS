import os
import csv
import gc
from model import ForestFireModel
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed

"""
Helper function to run a single simulation.

Parameters:
    size (int): The size of the forest.
    density (float): The density of the forest.
    wind (bool): Whether the wind is on or off.
    env_index (float): The environmental index.
    plant_tree_proportion (float): The proportion of trees to plant.
    tree_burn_time (int): The time it takes for a tree to burn down.
    plant_burn_time (int): The time it takes for a plant to burn down.

Returns:
    List: A list of simulation results.
"""
def run_simulation(size, density, wind, env_index, 
                   plant_tree_proportion, tree_burn_time, 
                   plant_burn_time):
    # Create a forest fire model
    model = ForestFireModel(size, density, env_index, wind, plant_tree_proportion, tree_burn_time, plant_burn_time)
    
    # Get the initial total number of trees
    num_trees_total = model.get_num_vegetation()

    # Ignite the fire
    model.ignite_fire_center()

    # Run the simulation
    model.no_display_single_simulation()

    # Get the percolation and percentage burnt down
    percolation = model.burns_left_to_right()
    num_burnt = model.get_num_burnt()
    burnt_perc = num_burnt / num_trees_total if num_trees_total > 0 else 0

    return [size, density, wind, env_index, 
            plant_tree_proportion, tree_burn_time, 
            plant_burn_time, percolation, burnt_perc]

"""
Function to run many simulations in parallel with a range of parameters
and save the results to a CSV file.

Parameters:
    sizes (List[int]): The range of sizes to simulate.
    densities (List[float]): The range of densities to simulate.
    test_wind (str): The wind condition to simulate.
    env_indixes (List[float]): The range of environmental indexes to simulate.
    plant_tree_proportions (List[float]): The range of plant tree proportions to simulate.
    tree_burn_times (List[int]): The range of tree burn times to simulate.
    file_name (str): The name of the output CSV file.
    num_simulations_per_setting (int): The number of simulations to run for each parameter setting.
    batch_size (int): The number of simulations to write to the CSV file at a time.
"""
def simulation_to_csv_parallel(sizes, densities, test_wind, env_indixes, 
                               plant_tree_proportions,  tree_burn_times, 
                               file_name, num_simulations_per_setting=1,
                               batch_size=1000):
    # Field names for the CSV file
    fields = ['size', 'density', 'wind', 'env_index', 'plant_tree_proportion', 'tree_burn_time', 'plant_burn_time', 'percolation', 'percentage burnt down']
    
    # List to store rows of data
    rows = []

    # Simulation count
    simulation_count = 0

    # Default plant burn time
    plant_burn_time = 1

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
                         num_simulations_per_setting)

    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor: # Uses ThreadPoolExecutor to run simulations in parallel
        # List to store futures
        futures = []
        with tqdm(total=total_simulations, desc="Simulations") as pbar: # Uses tqdm to display a progress bar
            for size in sizes:
                for density in densities:
                    for wind in winds:
                        for env_index in env_indixes:
                            for plant_tree_proportion in plant_tree_proportions:
                                for tree_burn_time in tree_burn_times:
                                    for _ in range(num_simulations_per_setting):
                                        # Submit a new simulation to the executor and store the future
                                        futures.append(
                                            executor.submit(
                                                run_simulation, 
                                                size, 
                                                density, 
                                                wind, 
                                                env_index, 
                                                plant_tree_proportion, 
                                                tree_burn_time, 
                                                plant_burn_time
                                            )
                                        )

            # Iterate over the futures as they are completed
            for future in as_completed(futures):
                # Appends results of future to data row
                rows.append(future.result())

                # Updates simulation count and loading bar
                simulation_count += 1
                pbar.update(1)

                # Batch csv write and garbage collection
                if simulation_count % batch_size == 0:
                    write_to_csv(file_name, fields, rows, simulation_count == batch_size)
                    rows.clear()
                    gc.collect()

        # Write remaining rows to CSV file
        if rows:
            write_to_csv(file_name, fields, rows, simulation_count <= batch_size)

        gc.collect()

"""
Helper function to write rows to a CSV file.

Parameters:
    file_name: Name of the CSV file.
    fields: List of field names.
    rows: List of rows to write.
    write_header: Boolean indicating whether to write the header.
"""
def write_to_csv(file_name, fields, rows, write_header):
    # Create the Data directory if it does not exist
    data_dir = os.path.join(os.path.dirname(__file__), '../Data')
    os.makedirs(data_dir, exist_ok=True)
    
    # Write to CSV file in the Data directory
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, mode='a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if write_header:
            csvwriter.writerow(fields)
        csvwriter.writerows(rows)