from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
import numpy as np
import pandas as pd

# Set up the output file
output_file("bokeh_basic_plots.html")

# Generate sample data
np.random.seed(42)
x = np.linspace(1, 10, 100)
y = 2 * x + 1 + np.random.normal(scale=1, size=x.shape)
data = pd.DataFrame({'x': x, 'y': y})

# Create a line plot
line_plot = figure(title="Line Plot Example", x_axis_label='X Values', y_axis_label='Y Values')
line_plot.line(x, y, legend_label="Line", line_width=2, color='blue')

# Create a scatter plot
scatter_plot = figure(title="Scatter Plot Example", x_axis_label='X Values', y_axis_label='Y Values')
scatter_plot.scatter('x', 'y', source=data, color='red', legend_label="Scatter", size=10, marker='circle')

# Layout the plots
layout = column(line_plot, scatter_plot)

# Show the plots
show(layout)
