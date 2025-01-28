import sys
from csv_writer_parallel import simulation_to_csv_parallel

def main():
    size = [100,300,500,750,1000]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "true_1_0_1_1.csv"
    num_simulations_per_setting = 25

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,300,500,750,1000]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "No Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "false_1_0_1_1.csv"
    num_simulations_per_setting = 25

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,300,500,750,1000]
    density = [0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1.0]
    test_wind = "Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "true_075_0_1_1.csv"
    num_simulations_per_setting = 25

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,300,500,750,1000]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1.0]
    test_wind = "No Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "false_075_0_1_1.csv"
    num_simulations_per_setting = 25

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,300,500,750,1000]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99,1.0]
    test_wind = "Wind"
    env_indices = [0.5]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "true_05_0_1_1.csv"
    num_simulations_per_setting = 25

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,300,500,750,1000]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99,1.0]
    test_wind = "No Wind"
    env_indices = [0.5]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "false_05_0_1_1.csv"
    num_simulations_per_setting = 25

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,300,500,750,1000]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,0.96,0.97,0.98,0.99,1.0]
    test_wind = "Wind"
    env_indices = [0.25]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "true_025_0_1_1.csv"
    num_simulations_per_setting = 25

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,300,500,750,1000]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,0.96,0.97,0.98,0.99,1.0]
    test_wind = "No Wind"
    env_indices = [0.25]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "false_025_0_1_1.csv"
    num_simulations_per_setting = 25

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

if __name__ == "__main__":
    main()