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

    def test_add_results(self):
        result = init_result()
        test_plot = PercolationPlot([])
        self.assertEqual(0, len(test_plot.results))
        test_plot.add_results(result)
        self.assertEqual(1, len(test_plot.results))

    def test_add_multiple_results(self):
        result = init_results()
        test_plot = PercolationPlot([])
        self.assertEqual(0, len(test_plot.results))
        test_plot.add_multiple_results(result)
        self.assertEqual(2, len(test_plot.results))

    def test_get_result(self):
        test_plot = PercolationPlot(init_results())
        self.assertEqual(2, len(test_plot.results))
        test_result = test_plot.get_result(0)
        self.assertEqual(100, test_result.system_size)

    def test_clear_results(self):
        test_plot = PercolationPlot(init_results())
        self.assertEqual(2, len(test_plot.results))
        test_plot.clear_results()
        self.assertEqual(0, len(test_plot.results))


if __name__ == '__main__':
    unittest.main()
