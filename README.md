# Team 10:  Forest Fire Percolation Model (Fire Fire Fire/Hot To Go)
#### Mikko Brandon, Victoria Peterson, Yoad van Praag, Rinske Oskamp

![Forest Fire with two types of vegetation](https://github.com/MikkoBra/CSS/blob/main/readme/Forest_fire_ptprop.gif)

## Table of Contents

1. [Usage and Installation](#usage-and-installation)
    - [GUI Usage](#gui-usage)
    - [Terminal Usage](#terminal-usage)
2. [Implementation](#implementation)
    - [Main Functions](#main-functions)
    - [ForestFireModel](#forestfiremodel)
    - [Simulations](#simulations)
    - [PlotGenerator](#plotgenerator)
    - [GUI Components](#gui-components)
    - [Data Access](#data-access)
3. [Contributing](#contributing)
4. [License](#license)
5. [Project Plan](#project-plan)
    - [Background and Motivation](#background-and-motivation)
    - [Short Description](#short-description)
    - [Disciplines](#disciplines)
    - [Emergence Phenomena](#emergent-phenomena)
    - [Research Questions](#research-questions)
    - [Hypotheses](#hypotheses)
    - [Planned Implementation](#planned-implementation)
    - [References](#references)


## Usage and Installation
To run the simulations and generate plots, follow these steps:

1. Clone the repository:
```sh
gh repo clone MikkoBra/CSS
```

2. Create and activate a virtual environment
``` sh
python -m venv venv
venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**: Ensure you have all the required dependencies installed. You can install them using the `requirements.txt` file:
```sh
pip install -r requirements.txt
```

4. **Run Simulations**: Use the provided scripts to run the simulations. 

    - To run using the GUI:
    ```sh
    python ForestFirePercolation/src/main_run_gui.py
    ```
    - To run using the Terminal:
    ```sh
    python ForestFirePercolation/src/main_run_terminal.py
    ```

5. **Generate Plots**: Use the provided scripts to plot the `.csv` data collected when simulating a parameter range
```sh
python ForestFirePercolation/src/main_generate_plots.py
```

### GUI Usage
1. **Run Simulations**: Use the GUI script to run simulations
```sh
python ForestFirePercolation/src/main_run_gui.py
```

2. **Select Simulation Type**: Select the type of simulation you want to complete

![Simulation Select](https://github.com/MikkoBra/CSS/blob/main/readme/sim_select.png)
- **Single Density, Single Simulation**: Run a single parameter set in a single simulation with the option to view the 2D Forest Fire Percolation grid.
- **Single Density, Multiple Simulations**: Run a single parameter set over a number of simulations to output a burnt forest percentage distribution for the parameter set.
- **Simulate Parameter Range**: Run a range of parameters over a number of simulations, outputing the resulting burnt forest percentage and whether the fire percolated from the left-most side of the grid to the right-most side of the grid.

4. **Select Input Parameters**: Each simulation type shares parameters, but also have their own unique options to specify simulation options.
**Single Density, Single Simulation**

![Single Density, Single Sim 1](https://github.com/MikkoBra/CSS/blob/main/readme/single_single_1.png)
- Size: Size of the Forest grid used for simulation (Size x Size grid)
- Forest Density Percentage: The percentage of the grid cells that contain trees.
- Probability for Fire Ignition: The likelihood that a tree will catch fire when exposed to a burning tree.
- Proportion of Plants to Trees: The ratio of plants to trees in the forest grid.
- Tree Burn Time: The duration for which a tree cell remains on fire.
- Plant Burn Time: The duration for which a plant cell remains on fire.
- Ignition Location: The starting point of the fire within the grid.
- Enable Eastward Wind: A boolean option to enable or disable wind blowing from the west to the east, affecting fire spread.
- Use Random Seed: A boolean option to enable or disable the use of a random seed for reproducibility of simulations.
  
![Single Density, Single Sim 2](https://github.com/MikkoBra/CSS/blob/main/readme/single_single_2.png)
- Random Ignition Points: Enter the number of cells to randomly ignite initially. Conditional on using the random ignition location option.
- Enter the Seed: Enter the seed value for random number generation in the simulation. Conditional on the random seed usee option.
- Display Simulation: Determine if the simulation is displayed. If the simulation is not displayed, only the simulation data will be output.
  
![Single Density, Single Sim 3](https://github.com/MikkoBra/CSS/blob/main/readme/single_single_3.png)
- Save Single Simulation: Select this option if you wish to save the simulation `.gif`. It will be saved in the `\data` directory. The animation can only be saved if the simulation is displayed.
- Name of the Output File: Enter the name of the `.gif` file to be saved if you select yes in the previous option.
    
**Single Density, Multiple Simulations**: 

![Single Density, Multi Sim 1](https://github.com/MikkoBra/CSS/blob/main/readme/Single_multi_1.png)
- Options are the same for the first *Single Density, Multiple Simulations* window, but the random seed option is removed
        
![Single Density, Multi Sim 2](https://github.com/MikkoBra/CSS/blob/main/readme/Single_multi_2.png)
- Random Ignition Points: Enter the number of cells to randomly ignite initially. Conditional on using the random ignition location option.
- Number of Simulations: Enter the number of simulations to run for the single set of parameters defined previously
    
**Simulate Parameter Range**

![Simulate Parameter Range](https://github.com/MikkoBra/CSS/blob/main/readme/multi_multi.png)
- *Size Range*: Specify the range of grid sizes for the forest simulation separated by commas. This determines the dimensions of the forest grid.
- *Forest Density Range*: Define the range of forest densities to simulate separated by commas. This is the percentage of the grid cells that contain trees.
- *Environmental Index Range*: Set the range for the environmental influence index separated by commas. This index affects the probability of fire spread.
- *Plant/Tree Proportion Range*: Specify the range for the proportion of plants to trees in the forest separated by commas. This ratio influences the fire dynamics.
- *Tree Burn Time Range*: Define the range for the burn time of tree cells separated by commas. This is the duration a tree cell remains on fire.
- *Plant Burn Time Range*: Set the range for the burn time of plant cells separated by commas. This is the duration a plant cell remains on fire.
- *Eastward Wind Options*: Choose whether to test wind, no wind, or both. Wind adds an additional cell neighbor to the right of the cell so that firest may ignite two cells to their right instead of one.
- *Number of Simulations per Parameter Set*: Enter the number of simulations to run for each parameter set (e.g., 100). This helps in obtaining statistically significant results.
- *Run the Simulations in Parallel*: Select whether to run simulations in parallel (true/false). Parallel execution can speed up the simulation process.
- *Name of the Output File*: Provide the name for the output file (e.g., results.csv). This file will store the simulation results.

5. **Generate Plots**: Use the provided scripts to plot the `.csv` data collected when simulating a parameter range
    - Make sure your `.csv` file is contained within the `ForestFirePercolation\data` directory
    - Adjust the `PlotGenerator` input to be the name of your `.csv`
    ``` python
    generator = PlotGenerator("your_data_here.csv")
    ```
    - Run the plotting script
    ```sh
    python ForestFirePercolation/src/main_generate_plots.py
    ```

## Implementation
The forest fire percolation model is implemented using Python and consists of several modules to handle different aspects of the simulation and analysis. Below is an overview of the main components:

### Main Functions
Multiple main functions are used to initialize the simulation functionality

- `main_run_gui`: Located in `src/gui/main_run_gui.py`, running this file will initialize the GUI for inputing simulation parameters and selecting options
- `main_run_terminal`: Located in `src/gui/main_run_terminal.py`, running this file will allow for simulation parameters and options in the terminal
- `main_generate_plots`: Located in `src/gui/main_generate_plots.py`, running this file will generate a number of percolation and criticality plots based on an input file located in the data/ file

### `ForestFireModel`
This modular class, located in `src/model.py`, simulates the forest fire spread on a 2D grid. It includes methods to initialize the forest, ignite fires, spread fires, and display the simulation.

### Simulations
The project includes functions and classes to simulate numerous forest fire percolation simulations over many simulations and over a range of parameters

- `SingleParamMultiSim`: Located in `src/single_param_multi_sim.py`, used to simulate a single parameter set over many simulations and plot both the linear and log/log distribution for the parameter set
- `multi_param_multi_sim`: Located in `src/multi_param_multi_sim.py`, used to simulate a an input range of parameters over many simulations, outputing a .csv file
- `multi_param_multi_sim_parallel`: Located in `src/multi_param_multi_sim_parallel.py`, used to simulate a an input range of parameters over many simulations in parallel, using all CPU cores and outputing a .csv file

### `PlotGenerator`
This class, located in src/plots/plot_generator.py, generates various plots from the simulation results. It includes methods to generate single and multiple percolation plots, critical point plots, and more.

### GUI Components
The project includes several GUI components to interact with the simulation:

- `InitialSimSelectionGUI`: Located in `src/gui/initial_sim_select_gui.py`, this class provides a GUI to select the type of simulation to run.
- `InputParameterSingleGUI`: Located in `src/gui/input_param_single_gui.py`, this class provides a GUI to input parameters for the single parameter set simulation option
- `InputParameterRangeGUI`: Located in `src/gui/input_param_range_gui.py`, this class provides a GUI to input parameters for the multiple parameter set, multiple simulation option
- `InputConditionalsGUI`: Located in `src/gui/input_conditionals_gui.py`, this class provides a GUI to input conditional parameters for the single parameter set simulation option.
- `RunSingleSimGUI`: Located in `src/gui/run_single_sim_gui.py`, this class provides a GUI to run a single simulation with specified parameters.
- `SaveSingleSimGUI`: Located in `src/gui/save_single_sim_gui.py`, this class provides a GUI to save the results of the single simulation option
- `RunRangeOfSimsGUI`: Located in `src/gui/run_range_sims_gui.py`, this class provides a GUI to run a range of parameters over a range of simulations.

### Data Access
The project includes modules to access and manipulate data:

- `csv_reader`: Located in `src/csv_access/csv_reader.py`, this module provides functions to read CSV files.
- `csv_writer`: Located in `src/csv_access/csv_writer.py`, this module provides functions to write CSV files.



## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Project Plan

## Background and Motivation
When abstracted to plots of land that either have a tree or do not have a tree, a forest can be represented on a 2D grid with tree cells and non-tree cells. Using such abstractions, forests have widely been modeled to simulate forest fire spread as a form of percolation. Due to the nature of the 2D grid, percolation theory applies to such forest fire spread, entailing that there is a critical point of tree density in an infinite-size forest at which forest fires go from never percolating to always percolating. Knowing whether this critical point applies to finite-size forests, and whether it can be influenced by external factors, could prove useful for forest fire prevention and intervention.

The frequency at which forest fires of each relative magnitude occur may also be inherent to forests as a system, not varying with system size. This would imply that forests exhibit self-organized criticality (SOC). Knowing whether this is the case, and how external factors affect the SOC property of forests, could be informative in knowing whether the same findings hold for all forest sizes.

## Short description
Our research investigates SOC and percolation in forest fires and their dependence on various environmental conditions. We model forest fires using a 2D grid with clusters of trees, simulating fire spread and measuring the frequency and size of individual fire events. The control experiment is conducted by varying the forest density to find a baseline critical point when no environmental conditions influence the spread of fire. The critical point is defined as the first density at which at least 50% of all simulations percolate. Then, we experiment with wind, implemented as a directional increase in fire spread, environmental influences, implemented as a global probability of fire spread, and variety of burnable vegetation, implemented as a proportion of burnable cells that burn longer than the remaining proportion. For these environmental factors, we assess their effect on the critical point.

Using the found critical points as baseline densities, we analyze the statistical distribution of fire sizes and assess whether it follows the same (power law) distribution when system size is extrapolated to infinity, which would indicate the presence of SOC.

### Disciplines
Environmental science, data science, physics, percolation theory

### Emergent Phenomena
Self-Organized Criticality, Percolation

### Research Questions:
Do forest fires exhibit SOC?


How does introducing wind into the system affect the SOC and percolation of forest fires?


How do environmental influences affect the SOC and percolation of forest fires?


How does a combination of a variety of burnable vegetation and environmental influences affect the SOC and percolation of forest fires?

### Hypotheses:
We expect to find a critical point at which the probability of forest fire percolation follows a power law distribution, which would indicate the presence of SOC.


We expect the SOC to disappear with the introduction of wind directions, due to the sensitivity of SOC to the system’s conditions. We expect percolation to depend on wind direction, with tailwind increasing percolation, and headwind decreasing it.


We expect the SOC to be exhibited by a small range of environmental influence values, due to the sensitivity of SOC to the system’s conditions. We expect percolation to have a sudden increase around a specific environmental influence value, as the value simply influences the percolation probability as a scalar.


We expect the SOC to … We expect the percolation probabilities to be closer to the base model than when only varying the environmental influences. Plants burn for longer, so vegetation around the plants have longer to catch fire. This effectively counteracts the lower chance of burning due to environmental influences.


## Planned Implementation
Base model:
- 2D grid
- Tree cells
- Empty/burned cells
- Fire cells
- Spread of fire cells over trees
- System size

Add after research:
- Plots/data
- Wind
- Environmental Influences

Nice to have:
- LA fire situation
- Types of vegetation
- Preventative measures


## References
#### Percolation
Beer, Tom, and I. G. Enting. "Fire spread and percolation modelling." Mathematical and Computer Modelling 13.11 (1990): 77-96.
Galeano Sancho, Daniel. "Percolation theory and fire propagation in a forest." (2015).

#### Wind/Weather
W von Niessen and A Blumen. “Dynamics of forest fires as a directed percolation model”. (1986) J. Phys. A: Math. Gen. 19 L289. 
T Ohtsuki and T Keyes. “Biased percolation: forest fires with wind”. (1986) J. Phys. A: Math. Gen. 19 L281
Duane, Andrea, Marcelo D. Miranda, and Lluís Brotons. "Forest connectivity percolation thresholds for fire spread under different weather conditions." Forest Ecology and Management 498 (2021): 119558.

#### Environmental Influences
Perestrelo, Sara Aleixo, et al. "A multi-scale network with percolation model to describe the spreading of forest fires." Mathematics 10.4 (2022): 588.

#### Percolation in real fires
Caldarelli, Guido, et al. "Percolation in real wildfires." Europhysics Letters 56.4 (2001): 510.
