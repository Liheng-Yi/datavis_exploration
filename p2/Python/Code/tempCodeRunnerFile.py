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

# Unique sources and targets
sources = df['Source'].unique()
targets = df['Target'].unique()

# Create a plotter
p = pv.Plotter()

# Create a grid of bars
for index, row in df.iterrows():
    source = row['Source']
    target = row['Target']
    weight = row['Weight']
    
    # Create a bar
    position = (source * 2, target * 2, 0)
    bar = pv.Cube(center=position, x_length=1, y_length=1, z_length=weight / 10)  # Scaling down the height
    
    # Add the bar to the plotter
    p.add_mesh(bar, color="tan", show_edges=True)

# Add axes for reference
p.show_grid()

# Render the plot
p.show()
