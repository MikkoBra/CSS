from ForestFirePercolation.src.csvs.csv_reader import read_percolation_csv
from ForestFirePercolation.src.results.result_filter import ResultFilter
import numpy as np


def output_critical_densities(file_name):
    results = read_percolation_csv(file_name)
    result_filter = ResultFilter()
    base_results = result_filter.no_wind_filter(results)
    wind_results = result_filter.wind_filter(results)
    env_results = result_filter.env_075_filter(results)
    env_wind_results = result_filter.env_wind_filter(results)
    plant_results = result_filter.plant_filter(results)
    return {
        'base': output_critical_densities_per_experiment(base_results),
        'wind': output_critical_densities_per_experiment(wind_results),
        'env_index': output_critical_densities_per_experiment(env_results),
        'env_wind': output_critical_densities_per_experiment(env_wind_results),
        'plant': output_critical_densities_per_experiment(plant_results)
    }


def output_critical_densities_per_experiment(results):
    critical_values = []
    for system_size in results:
        critical_value = find_critical(results[system_size])
        critical_values.append(critical_value)
    return critical_values


def find_critical(results):
    """
    Computes the percolation probability per density, and saves the results in the PercolationPlot object's
     "densities" and "probabilities" arrays.
    """
    densities = []
    probabilities = []
    percolation_probability = {}
    # Fill dictionary with total number of results and number of results with percolation = True per density
    for result in results:
        density = result.density
        if density in percolation_probability:
            percolation_probability[density][0] += 1.0
        else:
            percolation_probability[density] = [1, 0]
        if result.percolation:
            percolation_probability[density][1] += 1.0
    # Save (number percolated/total number) per density
    sorted_probabilities = dict(sorted(percolation_probability.items()))
    for density in sorted_probabilities:
        densities.append(density)
        probability = sorted_probabilities[density][1]/sorted_probabilities[density][0]
        probabilities.append(probability)
    critical_index = np.searchsorted(probabilities, 0.5)
    print(densities)
    return densities[critical_index]


output_critical_densities('../Data/Simulation_data_critpoints.csv')
