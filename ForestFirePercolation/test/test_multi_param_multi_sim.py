import unittest

from unittest.mock import patch, call, MagicMock
from ForestFirePercolation.src.multi_param_multi_sim import multi_param_multi_sim

class TestMultiParamMultiSim(unittest.TestCase):
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

    @patch('ForestFirePercolation.src.multi_param_multi_sim.ForestFireModel')
    def test_multi_param_multi_sim(self, MockForestFireModel):
        mock_model_instance = MagicMock()
        MockForestFireModel.return_value = mock_model_instance
        mock_model_instance.get_num_vegetation.return_value = 100
        mock_model_instance.get_num_burnt.return_value = 50
        mock_model_instance.burns_left_to_right.return_value = True
        mock_model_instance.percolation.return_value = True
        mock_model_instance.percentage_burnt_down.return_value = 0.5


        
        multi_param_multi_sim(
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

        expected_calls = []
        for size in self.sizes:
            for density in self.densities:
                for wind in self.winds:
                    for env_index in self.env_indixes:
                        for plant_tree_proportion in self.plant_tree_proportions:
                            for tree_burn_time in self.tree_burn_times:
                                for plant_burn_time in self.plant_burn_times:
                                    for _ in range(self.num_simulations_per_setting):
                                        expected_calls.append(
                                            call(size, 
                                                 density, 
                                                 env_index, 
                                                 wind, 
                                                 plant_tree_proportion, 
                                                 tree_burn_time, 
                                                 plant_burn_time
                                            )
                                        )

        MockForestFireModel.assert_has_calls(expected_calls, any_order=True)

    @patch('ForestFirePercolation.src.multi_param_multi_sim.write_to_csv')
    @patch('ForestFirePercolation.src.multi_param_multi_sim.ForestFireModel')
    def test_csv_writing(self, MockForestFireModel, mock_write_to_csv):
        self.sizes = [10]
        self.densities = [1.0]
        self.test_wind = "No Wind"
        self.env_indixes = [1.0]
        self.plant_tree_proportions = [0.0]
        self.tree_burn_times = [1]
        self.plant_burn_times = [1]
        self.file_name = "test.csv"
        self.num_simulations_per_setting = 1
        self.batch_size = 10
        self.winds = [False]


        mock_model_instance = MagicMock()
        MockForestFireModel.return_value = mock_model_instance
        mock_model_instance.percolation.return_value = True
        mock_model_instance.get_num_vegetation.return_value = 100
        mock_model_instance.get_num_burnt.return_value = 100
        mock_model_instance.burns_left_to_right.return_value = True
        mock_model_instance.percentage_burnt_down.return_value = 1.0
        

        multi_param_multi_sim(
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
        

        mock_write_to_csv.assert_called_once_with(
            self.file_name,
            ['size', 'density', 'wind', 'env_index', 'plant_tree_proportion', 'tree_burn_time', 'plant_burn_time', 'percolation', 'percentage burnt down'],
            [[10, 1.0, False, 1.0, 0.0, 1, 1, True, 1.0]],
            True
        )

    @patch('ForestFirePercolation.src.multi_param_multi_sim.tqdm')
    @patch('ForestFirePercolation.src.multi_param_multi_sim.ForestFireModel')
    def test_progress_bar(self, MockForestFireModel, mock_tqdm):
        mock_model_instance = MagicMock()
        MockForestFireModel.return_value = mock_model_instance
        mock_model_instance.get_num_vegetation.return_value = 100
        mock_model_instance.get_num_burnt.return_value = 50
        mock_model_instance.burns_left_to_right.return_value = True

        mock_tqdm_instance = MagicMock()
        mock_tqdm.return_value = mock_tqdm_instance

        multi_param_multi_sim(
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

    @patch('ForestFirePercolation.src.multi_param_multi_sim.gc.collect')
    def test_garbage_collection(self, mock_gc_collect):
        multi_param_multi_sim(
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