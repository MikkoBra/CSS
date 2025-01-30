import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

# Read the data
df = pd.read_csv('/Users/yoad/Desktop/CLS year 1/ComplexSystems/ComplexCode/CSS/ForestFirePercolation/Data/Snellius/Snellius_Data_Full.csv')

# Define the sizes to analyze
sizes = [100, 250, 300, 500, 750, 1000]
colors = ['b', 'orange', 'g', 'r', 'purple', 'brown']  # Different colors for each size

# Create a single figure with subplots
fig, axes = plt.subplots(2,3, figsize=(10, 8))
axes = axes.flatten()

# Loop through each size and corresponding subplot
for size, color, ax in zip(sizes, colors, axes):
    # Apply filtering conditions for the current size
    conditions = (
        (df['wind'] == False) &
        (df['size'].astype(int) == size) &
        (df['plant_tree_proportion'].astype(int) == 0) & 
        (df['env_index'].astype(int) == 1) &
        (df['tree_burn_time'].astype(int) == 1) &
        (df['plant_burn_time'].astype(int) == 1)  
    )
    
    df_filtered = df[conditions]
    
    # Group by density and calculate variance of burnt percentage
    density_groups = df_filtered.groupby('density')['percentage burnt down']
    variance_burnt_percentage = density_groups.var()  # Variance of burnt percentage for each density
    
    # Plot the variance for the current size in the corresponding subplot
    ax.plot(variance_burnt_percentage.index, variance_burnt_percentage, label=f'Size {size}', color=color, linestyle='--')
    ax.set_xlabel('Density')
    ax.set_ylabel('Variance of Burnt Percentage')
    ax.set_title(f'Size {size}')
    ax.legend()
    ax.grid()

# Display the plot
plt.tight_layout()
plt.show()