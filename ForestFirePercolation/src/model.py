class ForestFireModel:
    def __init__(self, size, ignition_prob, growth_prob):
        self.size = size
        self.ignition_prob = ignition_prob
        self.growth_prob = growth_prob
        self.forest = self.initialize_forest()

    def initialize_forest(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]

    def ignite_fire(self):
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < self.ignition_prob:
                    self.forest[i][j] = 1  # Tree catches fire

    def spread_fire(self):
        new_forest = [row[:] for row in self.forest]
        for i in range(self.size):
            for j in range(self.size):
                if self.forest[i][j] == 1:  # If tree is burning
                    new_forest[i][j] = 2  # Tree is burned
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < self.size and 0 <= nj < self.size:
                            if self.forest[ni][nj] == 0 and random.random() < self.growth_prob:
                                new_forest[ni][nj] = 1  # New fire ignites
        self.forest = new_forest

    def run_simulation(self, steps):
        for _ in range(steps):
            self.spread_fire()

    def get_forest(self):
        return self.forest