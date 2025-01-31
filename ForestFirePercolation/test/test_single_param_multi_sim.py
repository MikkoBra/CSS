import unittest

from ForestFirePercolation.src.single_param_multi_sim import SingleParamMultiSim

class TestForestFireModel(unittest.TestCase):
    def setUp(self):
        self.size = 10
        self.forest_density = 1.0
        self.env_index = 1.0
        self.wind = False
        self.plant_tree_proportion = 0.0
        self.tree_burn_time = 1
        self.plant_burn_time = 1
        self.ignition_num = 10
        self.random_seed = 42
        self.num_simulations = 10

    def test_run_simulations(self):
        sim = SingleParamMultiSim(
            size=self.size,
            forest_density=self.forest_density,
            num_simulations=self.num_simulations,
            ignition_location='random',
            env_index=self.env_index,
            wind=self.wind,
            plant_tree_proportion=self.plant_tree_proportion,
            tree_burn_time=self.tree_burn_time,
            plant_burn_time=self.plant_burn_time,
            ignition_num=self.ignition_num,
            random_seed=self.random_seed
        )
        sim.run_simulations()
        self.assertEqual(len(sim.results), self.num_simulations)
        for result in sim.results:
            self.assertIn('percentage_burnt', result)
            self.assertIn('percentage_burning', result)
            self.assertIn('percentage_trees', result)
            self.assertIn('burns_left_to_right', result)
            self.assertIsInstance(result['percentage_burnt'], float)
            self.assertIsInstance(result['percentage_burning'], float)
            self.assertIsInstance(result['percentage_trees'], float)
            self.assertIsInstance(result['burns_left_to_right'], bool)


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()