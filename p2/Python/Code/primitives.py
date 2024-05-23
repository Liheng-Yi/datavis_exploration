import pyvista as pv
import numpy as np
import pandas as pd

# Data from the provided source
data = {
    "Source": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5],
    "Target": [6, 7, 8, 9, 10, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10],
    "Weight": [72.5, 25, 86, 85, 144, 73.0, 23, 82, 72, 117, 94.1, 58, 50, 39, 93, 80.5, 20, 68, 52, 109, 88.2, 41, 47, 67, 88]
}

df = pd.DataFrame(data)

# Create a plotter
p = pv.Plotter()

# Define the base points for the vectors
base_points = [(source * 2, target * 2, 0) for source, target in zip(df['Source'], df['Target'])]

# Add cones and arrows as glyphs with varying sizes
for index, row in df.iterrows():
    source = row['Source']
    target = row['Target']
    weight = row['Weight'] / 4

    # Define the position and direction
    position = np.array([source * 2, target * 2, 0])
    # Creating a random direction vector for each arrow
    direction = np.random.randn(3)
    direction /= np.linalg.norm(direction)  # Normalize to get a unit vector

    # Define varying sizes
    cone_radius = 0.5
    cone_height = weight / 10  # Scaling down the height

    # Randomize opacity to increase fuzziness
    opacity = np.random.uniform(0.3, 0.7)

    # Create and add cone
    cone = pv.Cone(center=position, direction=[0, 0, 1], radius=cone_radius, height=cone_height)
    # Randomly make some cones half visible
    if np.random.rand() > 0.5:
        p.add_mesh(cone, color="tan", opacity=opacity, smooth_shading=True)  # Add smooth shading and adjust opacity
    else:
        p.add_mesh(cone, color="tan", opacity=opacity * 0.5, smooth_shading=True)  # Half visible cones

    # Create and add arrow
    arrow_start = position + np.array([0, 0, cone_height])  # Move the arrow starting point to the tip of the cone
    arrow = pv.Arrow(start=arrow_start, direction=direction, tip_length=cone_height * 0.3, tip_radius=cone_radius * 0.3, shaft_radius=cone_radius * 0.1)
    p.add_mesh(arrow, color="blue", opacity=opacity, smooth_shading=True)  # Add smooth shading and adjust opacity

# Add axes for reference
p.show_grid()

# Render the plot
p.show()
