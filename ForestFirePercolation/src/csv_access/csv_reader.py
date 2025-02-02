import os
import csv

from ForestFirePercolation.src.results.result import Result

def read_percolation_csv(file_name):
    """
        Returns the results per run as a Result object, sectioned into system sizes in a dictionary.
        ex: {'50': [Result1, Result2], '100': [Result1, Result2]}

    :return:
    """
    file_path = os.path.join('ForestFirePercolation', 'data', file_name)
    with open(file_path, mode='r') as file:
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