import sys
from csv_writer_parallel import simulation_to_csv_parallel

def main():

    size = [100,250,500,750,1000]
    density = [0.594,0.595,0.596,0.597,0.598,0.599,0.600,0.601,0.602,0.603,0.604]
    test_wind = "Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_All_true_075_05_3_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,250,500,750,1000]
    density = [0.594,0.595,0.596,0.597,0.598,0.599,0.600,0.601,0.602,0.603,0.604]
    test_wind = "No Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex1_false_1_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    size = [100,250,500,750,1000]
    density = [0.545, 0.546, 0.547, 0.548, 0.549, 0.550, 0.551, 0.552, 0.553, 0.554,0.555,0.556,0.557,0.558,0.559,0.560,0.561,0.562,0.563,0.564,0.565]
    test_wind = "Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex1_true_1_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    '''
    size = [100,250,500,750,1000]
    density = [0.73, 0.731,0.732, 0.733, 0.734, 0.735, 0.736, 0.737, 0.7375, 0.738, 0.739, 0.740, 0.741, 0.742,0.743,0.744,0.745]
    test_wind = "No Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex075_false_0.75_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,250,500,750,1000]
    density = [0.655,0.656, 0.657, 0.658, 0.659, 0.660, 0.661, 0.662, 0.663, 0.664, 0.665, 0.666,0.667,0.668,0.669,0.67]
    test_wind = "No Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_plants_false_0.75_05_3_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    size = [100,250,500,750,1000]
    density = [0.87,0.871,0.872,0.873,0.874,0.875,0.876,0.877,0.878, 0.879, 0.880, 0.881, 0.882, 0.883, 0.884, 0.885, 0.886, 0.887, 0.888, 0.889, 0.89]
    test_wind = "Wind"
    env_indices = [0.5]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_windenvind05_true_0.5_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    size = [250]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "No Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "false_1_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [250]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_All_true_075_05_3_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [250]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "No Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex1_false_1_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    size = [250]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex1_true_1_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    size = [250]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "No Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex075_false_0.75_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [250]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "No Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_plants_false_0.75_05_3_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    size = [250]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "Wind"
    env_indices = [0.5]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_windenvind05_true_0.5_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    """
    size = [100,250,500,750,1000]
    density = [0.604]
    test_wind = "Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex1_false_1_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,250,500,750,1000]
    density = [0.596]
    test_wind = "No Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex1_false_1_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    size = [100,250,500,750,1000]
    density = [0.549]
    test_wind = "Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex1_true_1_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    size = [100,250,500,750,1000]
    density = [0.7375]
    test_wind = "No Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_envindex075_false_0.75_0_1_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)
    
    size = [100,250,500,750,1000]
    density = [0.661]
    test_wind = "No Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_plants_false_0.75_05_3_1.csv"
    num_simulations_per_setting = 1000

    simulation_to_csv_parallel(size, 
                               density, 
                               test_wind, 
                               env_indices, 
                               plant_tree_proporitons, 
                               tree_burn_times, 
                               file_name, 
                               num_simulations_per_setting)

    size = [100,250,500,750,1000]
    density = [0.883]
    test_wind = "Wind"
    env_indices = [0.5]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "SOC_windenvind05_true_0.5_0_1_1.csv"
    num_simulations_per_setting = 1000

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
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "true_075_05_3_1.csv"
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
    test_wind = "No Wind"
    env_indices = [0.75]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "false_075_05_3_1.csv"
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
    env_indices = [0.5]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "true_05_05_3_1.csv"
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
    test_wind = "No Wind"
    env_indices = [0.5]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "false_05_05_3_1.csv"
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
    env_indices = [0.25]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
    file_name = sys.argv[1] if len(sys.argv) > 1 else "true_025_05_3_1.csv"
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
    test_wind = "No Wind"
    env_indices = [0.25]
    plant_tree_proporitons = [0.5]
    tree_burn_times = [3]
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
                               """
                               '''

if __name__ == "__main__":
    main()