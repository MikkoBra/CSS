import os
import csv
import gc
from model import ForestFireModel
from tqdm import tqdm

def simulation_to_csv(sizes, densities, test_wind, env_indixes, 
                      plant_tree_proportions,  tree_burn_times, 
                      file_name, num_simulations_per_setting=1,
                      batch_size=1000):
    fields = ['size', 'density', 'wind', 'env_index', 'plant_tree_proportion', 'tree_burn_time', 'plant_burn_time', 'percolation', 'percentage burnt down']
    rows = []

    plant_burn_time = 1

    if test_wind == "Wind":
        winds = [True]
    if test_wind == "No Wind":
        winds = [False]
    elif test_wind == "Both":
        winds = [False, True]

    simulation_count = 0

    total_simulations = len(sizes) * len(densities) * len(winds) * len(env_indixes) * len(plant_tree_proportions) * len(tree_burn_times) * num_simulations_per_setting

    # Initialize the progress bar
    with tqdm(total=total_simulations, desc="Simulations") as pbar:
        for size in sizes:
            for density in densities:
                for wind in winds:
                    for env_index in env_indixes:
                        for plant_tree_proportion in plant_tree_proportions:
                            for tree_burn_time in tree_burn_times:
                                for _ in range(num_simulations_per_setting):
                                    model = ForestFireModel(size, density, env_index, wind, plant_tree_proportion, tree_burn_time, plant_burn_time)
                                    # Number of trees at the beginning
                                    num_trees_total = model.get_num_trees()
                                    # Run the model
                                    model.ignite_fire_center()
                                    model.no_display_single_simulation()
                                    # Extract the result
                                    percolation = model.burns_left_to_right()
                                    num_burnt = model.get_num_burnt()
                                    burnt_perc = num_burnt / num_trees_total if num_trees_total > 0 else 0
                                    # Add the data
                                    rows.append([size, density, wind, env_index, plant_tree_proportion, tree_burn_time, plant_burn_time, percolation, burnt_perc])

                                    simulation_count += 1

                                    # Update the progress bar
                                    pbar.update(1)

                                    # Batch processing and garbage collection
                                    if simulation_count % batch_size == 0:
                                        write_to_csv(file_name, fields, rows, simulation_count == batch_size)
                                        rows.clear()
                                        gc.collect()

        # Write remaining rows to CSV file
        if rows:
            write_to_csv(file_name, fields, rows, simulation_count <= batch_size)

        # Final garbage collection
        gc.collect()

def write_to_csv(file_name, fields, rows, write_header):
    data_dir = os.path.join(os.path.dirname(__file__), '../Data')
    os.makedirs(data_dir, exist_ok=True)
    
    # Write to CSV file in the Data directory
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, mode='a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if write_header:
            csvwriter.writerow(fields)  # Write header only once
        csvwriter.writerows(rows)