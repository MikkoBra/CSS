from csv_writer_parallel import simulation_to_csv_parallel

def main():
    size = [100,200,300,400,500,600,700,800,900,1000]
    density = [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.75,0.8,0.85,0.9,0.95,1.0]
    test_wind = "No Wind"
    env_indices = [1.0]
    plant_tree_proporitons = [0.0]
    tree_burn_times = [1]
    file_name = "Simulation_data_snellius.csv"
    num_simulations_per_setting = 100

    simulation_to_csv_parallel(size, density, test_wind, env_indices, plant_tree_proporitons, tree_burn_times, file_name, num_simulations_per_setting)

if __name__ == "__main__":
    main()