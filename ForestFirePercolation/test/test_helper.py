import numpy as np
from ForestFirePercolation.src.results import Results


def init_result():
    density = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    p_perc1 = np.array([0.0, 0.2, 0.4, 0.6, 0.4, 0.2])
    return [Results(density, p_perc1, 100)]


def init_results():
    results = init_result()
    density = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    p_perc2 = np.array([0.0, 0.1, 0.2, 0.3, 0.2, 0.1])
    result2 = Results(density, p_perc2, 200)
    results.append(result2)
    return results
