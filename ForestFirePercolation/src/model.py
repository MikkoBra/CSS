import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
from enum import IntEnum

class TreeStatus(IntEnum):
    EMPTY = 0
    TREE = 1
    BURNING = 2
    BURNT = 3

class ForestFireModel:
    def __init__(self, size, forest_density, ignition_num):
        self.size = size
        self.forest_density = forest_density
        self.ignition_num = ignition_num
        self.forest = np.zeros((size, size), dtype=int)
        self.initialize_forest()

    def initialize_forest(self):
        for i in range(self.size):
            for j in range(self.size):
                if np.random.random() < self.forest_density:
                    self.forest[i][j] = TreeStatus.TREE

    def ignite_fire(self):
        for _ in range(self.ignition_num):
            i, j = np.random.randint(0, self.size, size=2)
            self.forest[i][j] = TreeStatus.BURNING

    def spread_fire(self):
        fire_copy = self.forest.copy()
        for i in range(self.size):
            for j in range(self.size):
                if fire_copy[i][j] == TreeStatus.BURNING:
                    if i > 0 and fire_copy[i-1][j] == TreeStatus.TREE:
                        self.forest[i-1][j] = TreeStatus.BURNING
                    if j > 0 and fire_copy[i][j-1] == TreeStatus.TREE:
                        self.forest[i][j-1] = TreeStatus.BURNING
                    if i < self.size - 1 and fire_copy[i+1][j] == TreeStatus.TREE:
                        self.forest[i+1][j] = TreeStatus.BURNING
                    if j < self.size - 1 and fire_copy[i][j+1] == TreeStatus.TREE:
                        self.forest[i][j+1] = TreeStatus.BURNING
                    self.forest[i][j] = TreeStatus.BURNT

    def run_simulation(self, steps):
        for _ in range(steps):
            self.spread_fire()
    
    def display_forest(self):
        cmap = ListedColormap(['white', 'green', 'red', 'black'])
        norm = BoundaryNorm([0, 1, 2, 3, 4], cmap.N)
        plt.imshow(self.forest, cmap=cmap, norm=norm, interpolation='nearest')
        plt.axis('off')
        plt.show()

    def display_simulation(self, steps, interval=400):
        fig, ax = plt.subplots()
        ax.axis('off')
        cmap = ListedColormap(['white', 'green', 'red', 'black'])
        norm = BoundaryNorm([0, 1, 2, 3, 4], cmap.N)
        im = ax.imshow(self.forest, cmap=cmap, norm=norm, interpolation='nearest')

        def update(frame):
            self.spread_fire()
            im.set_array(self.forest)
            return im,

        anim = FuncAnimation(fig, update, frames=steps, interval=interval, blit=True)
        plt.show()

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
    
    def percentage_burnt(self):
        return self.get_num_burnt() / self.get_size()**2
    
    def percentage_burning(self):
        return self.get_num_burning() / self.get_size()**2
    
    def percentage_trees(self):
        return self.get_num_trees() / self.get_size()**2
