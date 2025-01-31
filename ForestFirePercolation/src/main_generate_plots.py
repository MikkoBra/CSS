from ForestFirePercolation.src.plots.plot_generator import PlotGenerator

if __name__ == "__main__":
    generator = PlotGenerator("Snellius_Data_Full.csv")
    generator.generate_base_experiment_plots()
    generator.generate_wind_experiment_plots()
    generator.generate_env_index_experiment_plots()
    generator.generate_env_index_050_and_wind_experiment_plots()
    generator.generate_plant_experiment_plots()
    generator.generate_base_SOC_plots()
    generator.generate_wind_SOC_plots()
    generator.generate_env_wind_SOC_plots()
    generator.generate_plant_SOC_plots()
    generator.generate_env_index_SOC_plots()
