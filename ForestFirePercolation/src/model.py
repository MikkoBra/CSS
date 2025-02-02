import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import noise

from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
from enum import IntEnum
from collections import deque
from typing import Optional, Dict, Any
from matplotlib.animation import PillowWriter

class TreeStatus(IntEnum):
    """
    Enum to represent the status of a tree in the forest.
    """
    EMPTY = 0
    TREE = 1
    PLANT = 2
    BURNING = 3
    BURNT = 4

class ForestFireModel:
    def __init__(self, 
                 size: int, 
                 forest_density: float, 
                 env_index: float, 
                 wind: bool, 
                 plant_tree_proportion: float, 
                 tree_burn_time: int, 
                 plant_burn_time: int, 
                 ignition_num: int = 0, 
                 random_seed: Optional[int] = None):
        """
        Class to model a forest fire percolation simulation.
        Attributes:
            size: size of the forest grid
            forest_density: density of trees in the forest
            env_index: probability of tree catching fire
            wind: boolean indicating if wind is present
            plant_tree_proportion: proportion of trees that are plants
            tree_burn_time: time taken for a tree to burn
            plant_burn_time: time taken for a plant to burn
            ignition_num: number of trees to ignite
            random_seed: random seed for reproducibility

            forest: 2D numpy array representing the forest
            noise_map: 2D numpy array representing a Perlin noise map used for vegetation generation
            burning_trees_queue: queue of burning trees
        Methods:
            initialize_forest: initializes the forest grid
            ignite_fire_random: ignites fire at random locations
            ignite_fire_corner: ignites fire at the corner of the forest
            ignite_fire_center: ignites fire at the center of the forest
            spread_fire: spreads the fire to neighboring trees
            no_display_single_simulation: runs a single simulation without displaying the forest
            display_current_forest_state: displays the current state of the forest
            display_single_simulation: displays a single simulation
            burns_left_to_right: checks if the fire burns from left to right

        Get Methods:
            get_num_trees: returns the number of trees in the forest
            get_num_burning: returns the number of burning trees in the forest
            get_num_burnt: returns the number of burnt trees in the forest
            get_forest_density: returns the forest density
            get_ignition_num: returns the number of trees ignited
            get_size: returns the size of the forest
            get_forest: returns the forest grid
            get_burning_trees_queue: returns the queue of burning trees
            percentage_burnt: returns the percentage of burnt trees
            percentage_burning: returns the percentage of burning trees
            percentage_trees: returns the percentage of trees
        """
        self.tree_burn_time = tree_burn_time
        self.plant_burn_time = plant_burn_time
        self.plant_tree_proportion = plant_tree_proportion
        self.size = size
        self.forest_density = forest_density
        self.env_index = env_index
        self.wind = wind
        self.ignition_num = ignition_num
        np.random.seed(random_seed)
        self.forest = np.zeros((size, size), dtype=int)
        self.noise_map = np.zeros((size, size))
        self.burning_trees_queue = deque()
        self.initialize_forest()

    """
    Initializes the forest grid.    
    """
    def initialize_forest(self):
        for i in range(self.size):
            for j in range(self.size):
                if np.random.uniform(0,1) < self.forest_density:
                    self.forest[i][j] = TreeStatus.TREE
                self.noise_map[i][j] = noise.pnoise2(i / 10, j / 10)
        
        for i in range(self.size):
            for j in range(self.size):
                if self.noise_map[i][j] < (2 * self.plant_tree_proportion - 1) and self.forest[i][j] == TreeStatus.TREE:
                    self.forest[i][j] = TreeStatus.PLANT
        
    """
    Ignites fire at random locations.
    """
    def ignite_fire_random(self):
        for _ in range(self.ignition_num):
            i, j = np.random.randint(0, self.size, size=2)
            if self.noise_map[i][j] < (2 * self.plant_tree_proportion - 1):
                self.burning_trees_queue.append((i, j, self.plant_burn_time))
            else:
                self.burning_trees_queue.append((i, j, self.tree_burn_time))
            self.forest[i][j] = TreeStatus.BURNING

    """
    Ignites fire at the corner of the forest.
    """
    def ignite_fire_corner(self):
        if self.noise_map[1][1] < (2 * self.plant_tree_proportion - 1):
            self.burning_trees_queue.append((1, 1, self.plant_burn_time))
        else:
            self.burning_trees_queue.append((1, 1, self.tree_burn_time))
        self.forest[1][1] = TreeStatus.BURNING

    """
    Ignites fire at the center of the forest.
    """
    def ignite_fire_center(self):
        if self.noise_map[self.size//2][self.size//2] < (2 * self.plant_tree_proportion - 1):
            self.burning_trees_queue.append((self.size//2, self.size//2, self.plant_burn_time))
        else:
            self.burning_trees_queue.append((self.size//2, self.size//2, self.tree_burn_time))
        self.forest[self.size//2][self.size//2] = TreeStatus.BURNING
    
    """
    Spreads the fire to neighboring trees.
    """
    def spread_fire(self):
        """
        Helper function to try to burn a tree at a given location.
        """
        def try_burn(i, j):
            # If random is below the environment index and the cell is a tree or plant, burn it
            if np.random.uniform(0, 1) < self.env_index and self.forest[i, j] in (TreeStatus.TREE, TreeStatus.PLANT):
                # Set the burn time based on the type of vegetation
                burn_time = self.tree_burn_time if self.forest[i, j] == TreeStatus.TREE else self.plant_burn_time
                # Set the cell to burning
                self.forest[i, j] = TreeStatus.BURNING
                # Add the cell to the burning queue
                self.burning_trees_queue.append((i, j, burn_time))

        # Create a copy of the burning trees queue to avoid checking newly added burning trees
        burning_trees = deque(self.burning_trees_queue)
        self.burning_trees_queue.clear()

        # While there are burning trees in the queue, spread the fire
        while burning_trees:
            i, j, burn_time = burning_trees.popleft()

            # Try to burn adjacent cells while remaining in the bounds of the forest
            if i > 0:
                try_burn(i - 1, j)
            if j > 0:
                try_burn(i, j - 1)
            if i < self.size - 1:
                try_burn(i + 1, j)
            if j < self.size - 1:
                try_burn(i, j + 1)

            # Decrement the burn time of the current cell
            burn_time -= 1

            # If the burn time is greater than 0, add the cell back to the burning queue
            if burn_time > 0:
                self.burning_trees_queue.append((i, j, burn_time))

            # Otherwise, set the cell to burnt
            else:
                self.forest[i][j] = TreeStatus.BURNT

            # If wind is present, try to burn additional adjacent cells
            if self.wind:
                if j + 1 < self.size - 1:
                    try_burn(i, j+2)
                if i < self.size - 1 and j < self.size - 1:
                    try_burn(i+1, j+1)
                if i > 0 and j < self.size - 1:
                    try_burn(i-1, j+1)

    """
    Runs a single simulation without displaying the forest.
    """
    def no_display_single_simulation(self):
        # While there are burning trees, spread the fire
        while self.get_num_burning() > 0:
            self.spread_fire()

    """
    Displays the current state of the forest.
    """
    def display_current_forest_state(self):
        # Create a colormap and norm
        cmap = ListedColormap(['white', 'green', 'orange', 'red', 'black'])
        norm = BoundaryNorm([0, 1, 2, 3, 4, 5], cmap.N)

        # Display the forest
        plt.imshow(self.forest, cmap=cmap, norm=norm, interpolation='nearest')
        plt.axis('off')
        plt.show()

    """
    Displays a single simulation.

    Optional Args:
        interval: time interval between frames in milliseconds
        save: boolean indicating if the simulation should be saved
        filename: name of the output file
    """
    def display_single_simulation(self, interval=300, save=False, filename="forest_fire_simulation.gif"):
        # Create a figure and axis
        fig, ax = plt.subplots()
        ax.axis('off')

        # Create a colormap and norm
        cmap = ListedColormap(['white', 'green', 'orange', 'red', 'black'])
        norm = BoundaryNorm([0, 1, 2, 3, 4, 5], cmap.N)

        # Display the initial forest
        im = ax.imshow(self.forest, cmap=cmap, norm=norm, interpolation='nearest')

        # Initialize saved frames if save is True
        if save:
            frames = []

        # While there are burning trees, spread the fire
        while self.get_num_burning() > 0:
            # Check if the figure is closed
            if not plt.fignum_exists(fig.number):
                break

            # Spread the fire
            self.spread_fire()

            # Update the displayed image
            im.set_array(self.forest)
            plt.draw()
            plt.pause(interval / 1000.0)

            # Save the frame if save is True
            if save:
                frames.append([plt.imshow(self.forest, cmap=cmap, norm=norm, interpolation='nearest')])

        # Save the animation if save is True
        if save:
            ani = matplotlib.animation.ArtistAnimation(fig, frames, interval=interval, blit=True)
            data_dir = os.path.join(os.path.dirname(__file__), '../Data')
            os.makedirs(data_dir, exist_ok=True)
            
            file_path = os.path.join(data_dir, filename)
            ani.save(file_path, writer=PillowWriter(fps=1000 // interval))

        # Show the animation if the figure is not closed
        if plt.fignum_exists(fig.number):
            plt.show()

    """
    Checks if the fire burns from left to right.
    """
    def burns_left_to_right(self):
        firstRow = False
        lastRow = False
        for i in range(self.size):
            if self.forest[i][0] == TreeStatus.BURNING or self.forest[i][0] == TreeStatus.BURNT:
                firstRow = True
            if self.forest[i][self.size-1] == TreeStatus.BURNING or self.forest[i][self.size-1] == TreeStatus.BURNT:
                lastRow = True
            if firstRow and lastRow:
                break
        return firstRow and lastRow

    """
    Returns the number of trees in the forest.
    """
    def get_num_trees(self):
        return np.sum(self.forest == TreeStatus.TREE)
    
    """
    Returns the number of plants in the forest.
    """
    def get_num_plants(self):
        return np.sum(self.forest == TreeStatus.PLANT)
    
    """
    Returns the number of plants and trees in the forest.
    """
    def get_num_vegetation(self):
        return np.sum(self.forest == TreeStatus.PLANT) + np.sum(self.forest == TreeStatus.TREE)
    
    """
    Returns the number of burning trees in the forest.
    """
    def get_num_burning(self):
        return np.sum(self.forest == TreeStatus.BURNING)
    
    """
    Returns the number of burnt trees in the forest.
    """
    def get_num_burnt(self):
        return np.sum(self.forest == TreeStatus.BURNT)

    """
    Returns the forest density.
    """
    def get_forest_density(self):
        return self.forest_density
    
    """
    Returns the number of trees ignited.
    """
    def get_ignition_num(self):
        return self.ignition_num
    
    """
    Returns the size of the forest.
    """
    def get_size(self):
        return self.size
    
    """
    Returns the forest grid.
    """
    def get_forest(self):
        return self.forest
    
    """
    Returns the queue of burning trees.
    """
    def get_burning_trees_queue(self):
        return self.burning_trees_queue
    
    """
    Returns the percentage of burnt trees.
    """
    def percentage_burnt(self):
        return self.get_num_burnt() / self.get_size()**2
    
    """
    Returns the percentage of burning trees.
    """
    def percentage_burning(self):
        return self.get_num_burning() / self.get_size()**2
    
    """
    Returns the percentage of trees.
    """
    def percentage_trees(self):
        return self.get_num_trees() / self.get_size()**2
