import unittest
from test_helper import init_result, init_results
from ForestFirePercolation.src.plots.percolation_plot import PercolationPlot


class TestPercolationPlot(unittest.TestCase):
    def test_init(self):
        test_plot = PercolationPlot([])
        self.assertEqual(0, len(test_plot.results))

    def test_init_with_results(self):
        results = init_results()
        test_plot = PercolationPlot(results)
        self.assertEqual(2, len(test_plot.results))


if __name__ == '__main__':
    unittest.main()
