import os
import unittest
import pytest

from unittest.mock import patch, MagicMock, call
from ForestFirePercolation.src.multi_param_multi_sim_parallel import multi_param_multi_sim_parallel
from ForestFirePercolation.src.multi_param_multi_sim_parallel import run_simulation, multi_param_multi_sim_parallel


"""
Need to explore options for unit testing parallel code from ProcessPoolExecutor
"""
class TestMultiParamMultiSimParallel(unittest.TestCase):
    def setUp(self):
        self.sizes = [10,25]
        self.densities = [0.5, 1.0]
        self.test_wind = "Both"
        self.env_indixes = [0.75,1.0]
        self.plant_tree_proportions = [0.5,0.0]
        self.tree_burn_times = [1,3]
        self.plant_burn_times = [1,5]
        self.file_name = "test_output.csv"
        self.num_simulations_per_setting = 2
        self.batch_size = 10

        self.winds = [True,False]

    def test_run_simulation(mock_forest_fire_model):
        result = run_simulation(10, 0.5, True, 1.0, 0.3, 5, 3)

        assert isinstance(result, list)
        assert len(result) == 9  
        assert result[8] >= 0 and result[8] <= 1 

    @patch('ForestFirePercolation.src.multi_param_multi_sim_parallel.tqdm')
    @patch('ForestFirePercolation.src.multi_param_multi_sim_parallel.ForestFireModel')
    def test_progress_bar(self, MockForestFireModel, mock_tqdm):
        mock_model_instance = MagicMock()
        MockForestFireModel.return_value = mock_model_instance
        mock_model_instance.get_num_vegetation.return_value = 100
        mock_model_instance.get_num_burnt.return_value = 50
        mock_model_instance.burns_left_to_right.return_value = True

        mock_tqdm_instance = MagicMock()
        mock_tqdm.return_value = mock_tqdm_instance

        multi_param_multi_sim_parallel(
            self.sizes, 
            self.densities, 
            self.test_wind, 
            self.env_indixes,
            self.plant_tree_proportions, 
            self.tree_burn_times, 
            self.plant_burn_times,
            self.file_name,
            self.num_simulations_per_setting, 
            self.batch_size
        )

        total_simulations = (len(self.sizes) *
                            len(self.densities) *
                            len(self.winds) *
                            len(self.env_indixes) *
                            len(self.plant_tree_proportions) *
                            len(self.tree_burn_times) *
                            len(self.plant_burn_times) *
                            self.num_simulations_per_setting)

        mock_tqdm.assert_called_once_with(total=total_simulations, desc="Simulations")

        pbar = mock_tqdm_instance.__enter__.return_value
        pbar.update.assert_called()
        self.assertEqual(pbar.update.call_count, total_simulations)
        pbar.update(1)
        self.assertEqual(pbar.update.call_count, total_simulations+1)

    @patch('ForestFirePercolation.src.multi_param_multi_sim_parallel.gc.collect')
    def test_garbage_collection(self, mock_gc_collect):
        multi_param_multi_sim_parallel(
            self.sizes, 
            self.densities, 
            self.test_wind, 
            self.env_indixes,
            self.plant_tree_proportions, 
            self.tree_burn_times, 
            self.plant_burn_times,
            self.file_name,
            self.num_simulations_per_setting, 
            self.batch_size
        )

        self.assertTrue(mock_gc_collect.called)


if __name__ == '__main__':
    unittest.main()