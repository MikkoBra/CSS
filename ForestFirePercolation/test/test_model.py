import unittest
import numpy as np
import noise
import logging

from ForestFirePercolation.src.model import ForestFireModel
from ForestFirePercolation.src.model import TreeStatus

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

    
    def test_initialization(self):
        size = 10
        forest_density = 0.6
        env_index = 0.5
        wind = True
        plant_tree_proportion = 0.3
        tree_burn_time = 5
        plant_burn_time = 3
        ignition_num = 2
        random_seed = 42

        forest = np.zeros((size, size), dtype=int)
        noise_map = np.zeros((size, size))

        np.random.seed(random_seed)

        model = ForestFireModel(size, forest_density, env_index, wind, plant_tree_proportion, tree_burn_time, plant_burn_time, ignition_num, random_seed)

        self.assertEqual(model.size, size)
        self.assertEqual(model.forest_density, forest_density)
        self.assertEqual(model.env_index, env_index)
        self.assertEqual(model.wind, wind)
        self.assertEqual(model.plant_tree_proportion, plant_tree_proportion)
        self.assertEqual(model.tree_burn_time, tree_burn_time)
        self.assertEqual(model.plant_burn_time, plant_burn_time)
        self.assertEqual(model.ignition_num, ignition_num)
        
        np.random.seed(random_seed) # Reset the random seed

        for i in range(size):
            for j in range(size):
                if np.random.uniform(0,1) < forest_density:
                    forest[i][j] = 1
                noise_map[i][j] = noise.pnoise2(i / 10, j / 10)

        logging.info(model.forest)
        logging.info(forest)
        print(noise_map)
        print(model.noise_map)
        self.assertTrue(np.array_equal(model.forest, forest))
        self.assertTrue(np.array_equal(model.noise_map, noise_map))
        self.assertEqual(len(model.burning_trees_queue), 0)

    def test_initialize_forest(self):
        size = 10
        forest_density = 0.6
        plant_tree_proportion = 0.3
        random_seed = 42

        model = ForestFireModel(size, forest_density, 0.5, True, plant_tree_proportion, 5, 3, 2, random_seed)
        model.initialize_forest()

        tree_count = np.sum(model.forest == TreeStatus.TREE)
        plant_count = np.sum(model.forest == TreeStatus.PLANT)
        self.assertGreater(tree_count + plant_count, 0)
        self.assertLessEqual(plant_count, tree_count)

    def test_ignite_fire_random(self):
        size = 10
        forest_density = 1.0
        env_index = 1.0
        wind = False
        plant_tree_proportion = 0.5
        tree_burn_time = 5
        plant_burn_time = 3
        ignition_num = 10
        random_seed = 42

        np.random.seed(random_seed)
        
        model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, ignition_num, random_seed)
        
        np.random.seed(random_seed)

        no_fire_model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, ignition_num, random_seed)
        
        model.ignite_fire_random()

        logging.info(model.burning_trees_queue)
        logging.info(model.burning_trees_queue)
        # Test initial burn count
        burning_count = np.sum(model.forest == TreeStatus.BURNING)
        self.assertEqual(burning_count, ignition_num)

        # Test for burning tree queue entries are equal to the initial ignition num
        self.assertEqual(len(model.burning_trees_queue), ignition_num)

        # Ensure that the cells in the queue are burning
        for i, j, _ in model.burning_trees_queue:
            self.assertIn(model.forest[i, j], [TreeStatus.BURNING])

        # Ensure that the burning trees in the queue have the correct burn time
        for i, j, burn_time in model.burning_trees_queue:
            if no_fire_model.forest[i, j] == TreeStatus.TREE:
                expected_burn_time = model.tree_burn_time
                self.assertEqual(burn_time, expected_burn_time)
            elif no_fire_model.forest[i, j] == TreeStatus.PLANT:
                expected_burn_time = model.plant_burn_time
                self.assertEqual(burn_time, expected_burn_time)

    def test_ignite_fire_center(self):
        size = 10
        forest_density = 1.0
        env_index = 1.0
        wind = False
        plant_tree_proportion = 0.5
        tree_burn_time = 5
        plant_burn_time = 3
        random_seed = 42

        np.random.seed(random_seed)
        
        model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, random_seed=random_seed)
        
        np.random.seed(random_seed)

        no_fire_model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, random_seed=random_seed)
        
        model.ignite_fire_center()

        print(model.burning_trees_queue)

        # Test initial burn count
        burning_count = np.sum(model.forest == TreeStatus.BURNING)
        self.assertEqual(burning_count, 1)

        # Test for burning tree queue entries are equal to 1
        self.assertEqual(len(model.burning_trees_queue), 1)

        for i, j, _ in model.burning_trees_queue:
            # Ensure that the cells in the queue are burning
            self.assertIn(model.forest[i, j], [TreeStatus.BURNING])

            # Ensure the burning cell is in the center
            self.assertEqual(i, size // 2)
            self.assertEqual(j, size // 2)

        # Ensure that the burning trees in the queue have the correct burn time
        for i, j, burn_time in model.burning_trees_queue:
            if no_fire_model.forest[i, j] == TreeStatus.TREE:
                expected_burn_time = model.tree_burn_time
                self.assertEqual(burn_time, expected_burn_time)
            elif no_fire_model.forest[i, j] == TreeStatus.PLANT:
                expected_burn_time = model.plant_burn_time
                self.assertEqual(burn_time, expected_burn_time)
    
    def test_ignite_fire_corner(self):
        size = 10
        forest_density = 1.0
        env_index = 1.0
        wind = False
        plant_tree_proportion = 0.5
        tree_burn_time = 5
        plant_burn_time = 3
        random_seed = 42

        np.random.seed(random_seed)
        
        model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, random_seed=random_seed)
        
        np.random.seed(random_seed)

        no_fire_model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, random_seed=random_seed)
        
        model.ignite_fire_corner()

        # Test initial burn count
        burning_count = np.sum(model.forest == TreeStatus.BURNING)
        self.assertEqual(burning_count, 1)

        # Test for burning tree queue entries are equal to 1
        self.assertEqual(len(model.burning_trees_queue), 1)

        # Ensure that the cells in the queue are burning
        for i, j, _ in model.burning_trees_queue:
            # Ensure that the cells in the queue are burning
            self.assertIn(model.forest[i, j], [TreeStatus.BURNING])

            # Ensure the burning cell is in the center
            self.assertEqual(i, 1)
            self.assertEqual(j, 1)

        # Ensure that the burning trees in the queue have the correct burn time
        for i, j, burn_time in model.burning_trees_queue:
            if no_fire_model.forest[i, j] == TreeStatus.TREE:
                expected_burn_time = model.tree_burn_time
                self.assertEqual(burn_time, expected_burn_time)
            elif no_fire_model.forest[i, j] == TreeStatus.PLANT:
                expected_burn_time = model.plant_burn_time
                self.assertEqual(burn_time, expected_burn_time)

    def test_spread_fire_no_wind(self):
        size = 5
        forest_density = 1.0
        env_index = 1.0
        wind = False
        plant_tree_proportion = 0.0
        tree_burn_time = 1
        plant_burn_time = 1
        ignition_num = 1
        random_seed = 42

        np.random.seed(random_seed)

        model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, ignition_num, random_seed=random_seed)
        
        model.ignite_fire_center()
        initial_burning_count = np.sum(model.forest == TreeStatus.BURNING)
        model.spread_fire()
        new_burning_count = np.sum(model.forest == TreeStatus.BURNING)

        self.assertGreater(new_burning_count, initial_burning_count)
        self.assertEqual(np.sum(model.forest == TreeStatus.BURNT), 1)

    def test_spread_fire_with_wind(self):
        size = 5
        forest_density = 1.0
        env_index = 1.0
        wind = True
        plant_tree_proportion = 0.0
        tree_burn_time = 1
        plant_burn_time = 1
        ignition_num = 1
        random_seed = 42

        np.random.seed(random_seed)

        model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, ignition_num, random_seed=random_seed)
        
        model.ignite_fire_center()
        initial_burning_count = np.sum(model.forest == TreeStatus.BURNING)
        model.spread_fire()
        new_burning_count = np.sum(model.forest == TreeStatus.BURNING)

        self.assertGreater(new_burning_count, initial_burning_count)
        self.assertEqual(np.sum(model.forest == TreeStatus.BURNT), 1)

    def test_spread_fire_with_plants(self):
        size = 5
        forest_density = 1.0
        env_index = 1.0
        wind = False
        plant_tree_proportion = 0.5
        tree_burn_time = 1
        plant_burn_time = 1
        ignition_num = 1
        random_seed = 42

        np.random.seed(random_seed)

        model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, ignition_num, random_seed=random_seed)
        
        model.ignite_fire_center()
        initial_burning_count = np.sum(model.forest == TreeStatus.BURNING)
        model.spread_fire()
        new_burning_count = np.sum(model.forest == TreeStatus.BURNING)

        self.assertGreater(new_burning_count, initial_burning_count)
        self.assertEqual(np.sum(model.forest == TreeStatus.BURNT), 1)
    
    def test_no_display_single_simulation(self):
        size = 5
        forest_density = 1.0
        env_index = 1.0
        wind = False
        plant_tree_proportion = 0.0
        tree_burn_time = 1
        plant_burn_time = 1
        ignition_num = 1
        random_seed = 42

        np.random.seed(random_seed)

        model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, ignition_num, random_seed=random_seed)
        
        model.ignite_fire_center()
        model.no_display_single_simulation()

        self.assertEqual(model.get_num_burning(), 0)
        self.assertGreater(model.get_num_burnt(), 0)

    def test_burns_left_to_right(self):
        size = 5
        forest_density = 1.0
        env_index = 1.0
        wind = False
        plant_tree_proportion = 0.0
        tree_burn_time = 1
        plant_burn_time = 1
        ignition_num = 1
        random_seed = 42

        np.random.seed(random_seed)

        model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, ignition_num, random_seed=random_seed)
        
        model.ignite_fire_center()
        model.no_display_single_simulation()

        self.assertTrue(model.burns_left_to_right())

    def test_getters(self):
        size = 5
        forest_density = 1.0
        env_index = 1.0
        wind = False
        plant_tree_proportion = 0.0
        tree_burn_time = 1
        plant_burn_time = 1
        ignition_num = 1
        random_seed = 42

        np.random.seed(random_seed)

        model = ForestFireModel(size, forest_density, env_index, wind, 
                                plant_tree_proportion, tree_burn_time, 
                                plant_burn_time, ignition_num, random_seed=random_seed)
        
        self.assertEqual(model.get_size(), size)
        self.assertEqual(model.get_forest_density(), forest_density)
        self.assertEqual(model.get_ignition_num(), ignition_num)
        self.assertEqual(model.get_num_trees(), np.sum(model.forest == TreeStatus.TREE))
        self.assertEqual(model.get_num_burning(), np.sum(model.forest == TreeStatus.BURNING))
        self.assertEqual(model.get_num_burnt(), np.sum(model.forest == TreeStatus.BURNT))
        self.assertEqual(model.get_burning_trees_queue(), model.burning_trees_queue)
        self.assertAlmostEqual(model.percentage_burnt(), model.get_num_burnt() / size**2)
        self.assertAlmostEqual(model.percentage_burning(), model.get_num_burning() / size**2)
        self.assertAlmostEqual(model.percentage_trees(), model.get_num_trees() / size**2)

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()