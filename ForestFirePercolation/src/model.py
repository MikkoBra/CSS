import os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import noise
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
from enum import IntEnum
from collections import deque
from typing import Optional, Dict, Any
from matplotlib.animation import PillowWriter

class TreeStatus(IntEnum):
    EMPTY = 0
    TREE = 1
    PLANT = 2
    BURNING = 3
    BURNT = 4


class ForestFireModel:
    def __init__(self, size: int, forest_density: float, env_index: float, 
                 wind: bool, plant_tree_proportion: float, tree_burn_time: int, 
                 plant_burn_time: int, ignition_num: int = 0, random_seed: Optional[int] = None):
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
        
    def ignite_fire_random(self):
        for _ in range(self.ignition_num):
            i, j = np.random.randint(0, self.size, size=2)
            if np.random.uniform(0,1) < self.plant_tree_proportion:
                self.burning_trees_queue.append((i, j, self.plant_burn_time))
            else:
                self.burning_trees_queue.append((i, j, self.tree_burn_time))
            self.forest[i][j] = TreeStatus.BURNING

    def ignite_fire_corner(self):
        if np.random.uniform(0,1) < self.plant_tree_proportion:
            self.burning_trees_queue.append((1, 1, self.plant_burn_time))
        else:
            self.burning_trees_queue.append((1, 1, self.tree_burn_time))
        self.forest[1][1] = TreeStatus.BURNING

    def ignite_fire_center(self):
        if np.random.uniform(0,1) < self.plant_tree_proportion:
            self.burning_trees_queue.append((self.size//2, self.size//2, self.plant_burn_time))
        else:
            self.burning_trees_queue.append((self.size//2, self.size//2, self.tree_burn_time))
        self.forest[self.size//2][self.size//2] = TreeStatus.BURNING
            
    def spread_fire(self):
        def try_burn(i, j):
            if np.random.uniform(0, 1) < self.env_index and self.forest[i, j] in (TreeStatus.TREE, TreeStatus.PLANT):
                self.forest[i, j] = TreeStatus.BURNING
                burn_time = self.tree_burn_time if self.forest[i, j] == TreeStatus.TREE else self.plant_burn_time
                self.burning_trees_queue.append((i, j, burn_time))

        burning_trees = deque(self.burning_trees_queue)
        self.burning_trees_queue.clear()
        while burning_trees:
            i, j, burn_time = burning_trees.popleft()
            if i > 0:
                try_burn(i - 1, j)
            if j > 0:
                try_burn(i - 1, j)
            if i < self.size - 1:
                try_burn(i + 1, j)
            if j < self.size - 1:
                try_burn(i, j + 1)

            burn_time -= 1
            if burn_time > 0:
                self.burning_trees_queue.append((i, j, burn_time))
            else:
                self.forest[i][j] = TreeStatus.BURNT

            if self.wind:
                if j + 1 < self.size - 1:
                    try_burn(i, j+2)
                if i < self.size - 1 and j < self.size - 1:
                    try_burn(i+1, j+1)
                if i > 0 and j < self.size - 1:
                    try_burn(i-1, j+1)


    def no_display_single_simulation(self):
        while self.get_num_burning() > 0:
            self.spread_fire()

    
    def display_current_forest_state(self):
        cmap = ListedColormap(['white', 'green', 'orange', 'red', 'black'])
        norm = BoundaryNorm([0, 1, 2, 3, 4, 5], cmap.N)
        plt.imshow(self.forest, cmap=cmap, norm=norm, interpolation='nearest')
        plt.axis('off')
        plt.show()

    def display_single_simulation(self, interval=300, save=True, filename="forest_fire_simulation.gif"):
        fig, ax = plt.subplots()
        ax.axis('off')
        cmap = ListedColormap(['white', 'green', 'orange', 'red', 'black'])
        norm = BoundaryNorm([0, 1, 2, 3, 4, 5], cmap.N)
        im = ax.imshow(self.forest, cmap=cmap, norm=norm, interpolation='nearest')

        if save:
            frames = []

        while self.get_num_burning() > 0:
            if not plt.fignum_exists(fig.number):
                break
            self.spread_fire()
            im.set_array(self.forest)
            plt.draw()
            plt.pause(interval / 1000.0)

            if save:
                frames.append([plt.imshow(self.forest, cmap=cmap, norm=norm, interpolation='nearest')])

        if save:
            ani = matplotlib.animation.ArtistAnimation(fig, frames, interval=interval, blit=True)
            data_dir = os.path.join(os.path.dirname(__file__), '../Data')
            os.makedirs(data_dir, exist_ok=True)
            
            file_path = os.path.join(data_dir, filename)
            ani.save(file_path, writer=PillowWriter(fps=1000 // interval))

        if plt.fignum_exists(fig.number):
            plt.show()

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

    def get_num_trees(self):
        return np.sum(self.forest == TreeStatus.TREE)
    
    def get_num_burning(self):
        return np.sum(self.forest == TreeStatus.BURNING)
    
    def get_num_burnt(self):
        return np.sum(self.forest == TreeStatus.BURNT)

    def get_forest_density(self):
        return self.forest_density
    
    def get_ignition_num(self):
        return self.ignition_num
    
    def get_size(self):
        return self.size
    
    def get_forest(self):
        return self.forest
    
    def get_burning_trees_queue(self):
        return self.burning_trees_queue
    
    def percentage_burnt(self):
        return self.get_num_burnt() / self.get_size()**2
    
    def percentage_burning(self):
        return self.get_num_burning() / self.get_size()**2
    
    def percentage_trees(self):
        return self.get_num_trees() / self.get_size()**2
