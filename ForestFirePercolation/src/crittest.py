import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

# Read the data
df = pd.read_csv('/Users/yoad/Desktop/CLS year 1/ComplexSystems/ComplexCode/CSS/ForestFirePercolation/Data/Snellius/Snellius_Data_Full.csv')

# Apply filtering conditions
conditions = (
    (df['wind'] == True) &
    (df['size'].astype(int) == 100) &
    (df['plant_tree_proportion'].astype(int) == 0) & 
    (df['env_index'].astype(int) == 1) &
    (df['tree_burn_time'].astype(int) == 1) &
    (df['plant_burn_time'].astype(int) == 1)  
)

df_new = df[conditions]

# Group by density and calculate variance of burnt percentage
density_groups = df_new.groupby('density')['percentage burnt down']

variance_burnt_percentage = density_groups.var()  # Variance of burnt percentage for each density

max_index = np.argmax(variance_burnt_percentage)
max_x = variance_burnt_percentage.index[max_index]
print(max_x)

# Plotting the variance
fig, ax = plt.subplots(figsize=(10, 6))

# Plot variance
ax.plot(variance_burnt_percentage.index, variance_burnt_percentage, label='Variance', color='r', linestyle='--')

# Labeling the axes and title
ax.set_xlabel('Density')
ax.set_ylabel('Variance of Burnt Percentage')
ax.set_title('Variance of Burnt Percentage Over Different Densities')
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()

