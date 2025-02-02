import os
import matplotlib.pyplot as plt
import pandas as pd

# Read the data
file_path = os.path.join('ForestFirePercolation', 'data', 'Snellius_Data_Full.csv')
df = pd.read_csv(file_path)

conditions = (
        (df['wind'] == False) &
        (df['size'].astype(int) == 100) &
        (df['plant_tree_proportion'].astype(int) == 0) & 
        (df['env_index'].astype(int) == 1) &
        (df['tree_burn_time'].astype(int) == 1) &
        (df['plant_burn_time'].astype(int) == 1)  
    )

# Filter the data based on the conditions
filtered_df = df[conditions]

# Group by 'density' and calculate the variance of the percentage burnt down area
variance_df = filtered_df.groupby('density')['percentage burnt down'].var().reset_index()

# Find the density with the highest variance
max_var_index = variance_df['percentage burnt down'].idxmax()
max_var_density = variance_df.loc[max_var_index, 'density']
max_variance = variance_df.loc[max_var_index, 'percentage burnt down']

# Plot the variance over density
plt.figure(figsize=(10, 6))
plt.plot(variance_df['density'], variance_df['percentage burnt down'], marker='o', linestyle='-', label='Variance of Burnt Area')
plt.scatter(max_var_density, max_variance, color='red', label=f'Max Variance at {max_var_density:.4f}')
plt.xlabel('Tree Probability')
plt.ylabel('Variance of Burnt Area')
plt.title('Variance of Burnt Area vs. Tree Probability for Grid Size 100')
plt.legend()
plt.grid(True)
plt.show()

print(f"The density with the highest variance is at density = {max_var_density:.4f}, with variance = {max_variance:.4f}")