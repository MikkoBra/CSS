import os
import csv
import gc
from model import ForestFireModel
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_simulation(size, density, wind, env_index, plant_tree_proportion, tree_burn_time, plant_burn_time):
    model = ForestFireModel(size, density, env_index, wind, plant_tree_proportion, tree_burn_time, plant_burn_time)
    num_trees_total = model.get_num_trees()
    model.ignite_fire_center()
    model.no_display_single_simulation()
    percolation = model.burns_left_to_right()
    num_burnt = model.get_num_burnt()
    burnt_perc = num_burnt / num_trees_total if num_trees_total > 0 else 0
    return [size, density, wind, env_index, plant_tree_proportion, tree_burn_time, plant_burn_time, percolation, burnt_perc]

def simulation_to_csv_GPU(sizes, densities, test_wind, env_indixes, 
                      plant_tree_proportions,  tree_burn_times, 
                      file_name, num_simulations_per_setting=1,
                      batch_size=1000):
    fields = ['size', 'density', 'wind', 'env_index', 'plant_tree_proportion', 'tree_burn_time', 'plant_burn_time', 'percolation', 'percentage burnt down']
    rows = []

    plant_burn_time = 1

    if test_wind:
        winds = [False, True]
    else:
        winds = [False]

    simulation_count = 0

    total_simulations = len(sizes) * len(densities) * len(winds) * len(env_indixes) * len(plant_tree_proportions) * len(tree_burn_times) * num_simulations_per_setting

    with ThreadPoolExecutor() as executor:
        futures = []
        with tqdm(total=total_simulations, desc="Simulations") as pbar:
            for size in sizes:
                for density in densities:
                    for wind in winds:
                        for env_index in env_indixes:
                            for plant_tree_proportion in plant_tree_proportions:
                                for tree_burn_time in tree_burn_times:
                                    for _ in range(num_simulations_per_setting):
                                        futures.append(executor.submit(run_simulation, size, density, wind, env_index, plant_tree_proportion, tree_burn_time, plant_burn_time))

            for future in as_completed(futures):
                rows.append(future.result())
                simulation_count += 1
                pbar.update(1)

                if simulation_count % batch_size == 0:
                    write_to_csv(file_name, fields, rows, simulation_count == batch_size)
                    rows.clear()
                    gc.collect()

        if rows:
            write_to_csv(file_name, fields, rows, simulation_count <= batch_size)

        gc.collect()

def write_to_csv(file_name, fields, rows, write_header):
    data_dir = os.path.join(os.path.dirname(__file__), '../Data')
    os.makedirs(data_dir, exist_ok=True)
    
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, mode='a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if write_header:
            csvwriter.writerow(fields)
        csvwriter.writerows(rows)