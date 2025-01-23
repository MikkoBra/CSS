import csv
import numpy as np
import matplotlib.pyplot as plt
#import sys

import sys
# # caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.append('/Users/rmosk/Dropbox/Rinske/Computational Science/Complex system simulations/Forest fire/CSS/ForestFirePercolation/src/model')
# import ForestFireModel
from model import ForestFireModel

# from .model import ForestFireModel
# from .simulations import ForestFireSimulations


# parameters, system size, perc percolation, perc burnt down.
def simulation_to_csv(sizes, densities, env_indixes, num_simulations_per_setting=10):
    fields = ['size', 'density', 'wind', 'env_index', 'percolation', 'percentage burnt down']
    rows = []
    winds = ["False", "True"]
    for size in sizes:
        for density in densities:
            for wind in winds:
                for env_index in env_indixes:
                    for _ in range(num_simulations_per_setting):
                        model = ForestFireModel(size, density, env_index, wind)
                        # Number of trees at the beginning
                        num_trees_total = model.get_num_trees()
                        # Run the model
                        model.ignite_fire_center()
                        model.no_display_single_simulation()#(env_index, wind)
                        # Extract the result
                        percolation = model.burns_left_to_right()
                        burnt_perc = model.get_num_burnt()/num_trees_total
                        # Add the data
                        rows.append([size, density, wind, env_index, percolation, burnt_perc])
    filename = "Simulation_data_test_criticalp.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)

sizes = [100]
densities = [0.2,0.4,0.6,0.8,1]
env_indixes = [1]

simulation_to_csv(sizes, densities, env_indixes)

