import csv
from ForestFirePercolation.src.results.result import Result
from ForestFirePercolation.src.plots.percolation_plot import PercolationPlot


def read_percolation_csv():
    """
        Returns the results per run as a Result object, sectioned into system sizes in a dictionary.
        ex: {'50': [Result1, Result2], '100': [Result1, Result2]}

    :return:
    """
    with open('../Simulation_data_test_criticalp.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
        result_dict = {}
        for result in data:
            size = result['size']
            result_obj = Result()
            result_obj.dict_to_result(result)
            if size in result_dict:
                result_dict[size].append(result_obj)
            else:
                result_dict[size] = [result_obj]
        return result_dict

results_per_system_size = read_percolation_csv()
plot = PercolationPlot()
for system_size in results_per_system_size:
    plot.plot_percolation(results_per_system_size[system_size], system_size)
