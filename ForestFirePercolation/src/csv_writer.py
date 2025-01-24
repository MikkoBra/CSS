import os
import csv
from model import ForestFireModel

def simulation_to_csv(sizes, densities, test_wind, env_indixes, plant_tree_proportions,  tree_burn_times, file_name, num_simulations_per_setting=1):
    fields = ['size', 'density', 'wind', 'env_index', 'plant_tree_proportion', 'tree_burn_time', 'plant_burn_time', 'percolation', 'percentage burnt down']
    rows = []

    plant_burn_time = 1

    if test_wind:
        winds = [False, True]
    else:
        winds = [False]

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
                                print('start sim')
                                model.no_display_single_simulation()#(env_index, wind)
                                # Extract the result
                                percolation = model.burns_left_to_right()
                                burnt_perc = model.get_num_burnt()/num_trees_total
                                # Add the data
                                rows.append([size, density, wind, env_index, plant_tree_proportion, tree_burn_time,plant_burn_time, percolation, burnt_perc])

    data_dir = os.path.join(os.path.dirname(__file__), '../Data')
    os.makedirs(data_dir, exist_ok=True)
    
    # Write to CSV file in the Data directory
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

"""
sizes = [50, 100]
densities = [0.5, 0.8]
env_indixes = [0.5, 1]
test_wind = True
plant_tree_proportions = [0.0]#[0.0, 0.5]
tree_burn_times = [1]#[1, 3, 5, 10]
file_name = 'Simulation_data_test_criticalp.csv'

simulation_to_csv(sizes, densities, test_wind, env_indixes, plant_tree_proportions, tree_burn_times, file_name, num_simulations_per_setting=1)

"""