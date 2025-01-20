import numpy as np
import matplotlib.pyplot as plt


class ForestFireModel:
    def __init__(self, size, forest_density, ignition_num):
        self.size = size
        self.forest_density = forest_density
        self.ignition_num = ignition_num
        self.forest = np.zeros((size, size))



    def initialize_forest(self):
        for i in range(self.size):
            for j in range(self.size):
                if np.random.random() < self.forest_density:
                    self.forest[i][j] = 1

    def ignite_fire(self):
        for _ in range(self.ignition_num):
            i, j = np.random.randint(0, self.size, size=2)
            self.forest[i][j] = 2

    def spread_fire(self):
        return self.forest

    def run_simulation(self, steps):
        for _ in range(steps):
            self.spread_fire()

    def get_forest(self):
        return self.forest
    

    def display_forest(self):
        plt.imshow(self.forest, cmap='Greens', interpolation='nearest')
        plt.axis('off')
        plt.show()