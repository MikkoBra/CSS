import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

# Read the data
df = pd.read_csv('ForestFirePercolation/data/Snellius_Data_Full.csv')

# Define the sizes to analyze
sizes = [100, 250, 500, 750, 1000]
colors = ['b', 'orange', 'g', 'r', 'purple', 'brown']  # Different colors for each size

# Create a single figure with subplots
fig, axes = plt.subplots(2, 3, figsize=(14, 7))
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

    density_max = variance_burnt_percentage.idxmax()
    print(density_max)
    
    # Find the first and last nonzero values in variance
    nonzero_variance = variance_burnt_percentage[variance_burnt_percentage > 0.0001]
    if not nonzero_variance.empty:
        x_min = max(nonzero_variance.index.min() - 0.05, 0)  # Ensure x_min is not negative
        x_max = min(nonzero_variance.index.max() + 0.05, 1)  # Ensure x_max does not exceed 1
    else:
        x_min, x_max = 0.4, 1  # Default range if no nonzero values exist

    critical_density = variance_burnt_percentage.idxmax()  # Density where variance peaks
    ax.axvline(critical_density, color='k', linestyle='--', label=f'Critical Density: {critical_density:.2f}')
    
    # Plot the variance for the current size in the corresponding subplot
    ax.plot(variance_burnt_percentage.index, variance_burnt_percentage, label=f'Size {size}', color=color)
    ax.set_xlabel('Density')
    ax.set_ylabel('Variance of Burnt Percentage')
    ax.set_title(f'Size {size}')
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0, variance_burnt_percentage.max())
    ax.legend()
    ax.grid()

print('Critical densities for each size:')
display(pd.DataFrame({'Size': sizes, 'Critical Density': [axes[i].lines[-1].get_xdata()[0] for i in range(len(sizes))]}))

# Display the plot
plt.tight_layout()
plt.show()