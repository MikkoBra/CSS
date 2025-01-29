# Team 10:  Fire Fire Fire/Hot To Go
#### Mikko Brandon, Victoria Peterson, Yoad van Praag, Rinske Oskamp

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

## Research questions and hypotheses
### Questions:
Do forest fires exhibit SOC?


How does introducing wind into the system affect the SOC and percolation of forest fires?


How do environmental influences affect the SOC and percolation of forest fires?


How does a combination of a variety of burnable vegetation and environmental influences affect the SOC and percolation of forest fires?

### Hypotheses:
We expect to find a critical point at which the probability of forest fire percolation follows a power law distribution, which would indicate the presence of SOC.


We expect the SOC to disappear with the introduction of wind directions, due to the sensitivity of SOC to the system’s conditions. We expect percolation to depend on wind direction, with tailwind increasing percolation, and headwind decreasing it.


We expect the SOC to be exhibited by a small range of environmental influence values, due to the sensitivity of SOC to the system’s conditions. We expect percolation to have a sudden increase around a specific environmental influence value, as the value simply influences the percolation probability as a scalar.


We expect the SOC to … We expect the percolation probabilities to be closer to the base model than when only varying the environmental influences. Plants burn for longer, so vegetation around the plants have longer to catch fire. This effectively counteracts the lower chance of burning due to environmental influences.


## Implementation
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





#### Brainstorming
Forestfires - Percolation
- Map of LA area and tree density mapsExample forest fire
- Weather
- Prevention
- Intervention
Image denoising (CA)
Mycology Percolation/Cellular Automota


#### Instructor Questions

Ask about emergent behaviour and what in our research could be considered this.
What is the critical point we want to measure? Significant damage in area percentage)or connectivity of one side to the other side of the grid. 
How feasible is it to do this in 2 weeks? (Gather data, use it to simulate to effectively model what happened in LA, or keep it more generalised). Will incorporating the windy condition comparison be manageable?
Exact analytical solutions for percolation thresholds only exist in some low-dimensional cases (like 1D), while for higher dimensions (2D, 3D, etc.), we rely on numerical simulations. How will this affect our research and is there a way ofr us to generate some hypothesis / computation to measure risk or will this all be data oriented.

Look at SOC property  and whether it is still holds in different scenarios.
The emergent behavior is considered the SOC and percolation.

How does the exponent depend on parameter like vegetation growth windy conditions, 


So check for different sizes of the system whether the same pattern holds (regarding emergent properties affected by environmental behaviour). See what happens if system size were to approach infinity and whether we observe unique convergent behaviour (e.g. bifurcation diagram showing critical points diverging by changing variable).



Measurement
Criticality (critical point, p_c)
Spreading one corner to the other → percentage of simulations, probability distribution
Distribution of Fire percolation


### References
Forest Density Data
https://oehha.ca.gov/climate-change/epic-2022/impacts-vegetation-and-wildlife/subalpine-forest-density
Forest Fire Data
https://www.fire.ca.gov/incidents


Weather conditions
https://www.sciencedirect.com/science/article/pii/S1574954124000736
https://pubs.cif-ifc.org/doi/pdf/10.5558/tfc65450-6
https://www.pnas.org/doi/10.1073/pnas.2111875118#executive-summary-abstract
https://fireecology.springeropen.com/articles/10.1186/s42408-024-00254-2#:~:text=Temperature%20fluctuations%20influence%20the%20duration,in%20turn%2C%20influence%20fire%20spread.


Implementation
https://codingandmore.home.blog/2020/01/06/forest-fires-and-percolation/
https://gitlab.com/stunderline/forestfire/tree/master

