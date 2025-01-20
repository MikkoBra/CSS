import numpy as np
import matplotlib.pyplot as plt
from model import ForestFireModel

def main():
    size = int(input("Enter the size of the forest (e.g., 50 for a 50x50 grid): "))
    p = float(input("Enter forest density percentage (0 to 1): "))
    ignition_num = int(input("Enter the number of trees to ignite: "))

    model = ForestFireModel(size, p, ignition_num)
    model.initialize_forest()
    model.ignite_fire()


    #steps = int(input("Enter the number of simulation steps: "))
    #model.run_simulation(steps)

    model.display_forest()

if __name__ == "__main__":
    main()