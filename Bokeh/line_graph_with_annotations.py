from bokeh.plotting import figure, show, output_file
import numpy as np

# Output file
output_file("bokeh_basic_line_graph.html")

# Prepare some data
x = np.linspace(10, 100, 100)
y = np.sin(x / 10) * 2

# Create a new plot with a title and axis labels
p = figure(title="Basic Line Graph", x_axis_label="X Axis", y_axis_label="Y Axis")

# Add line renderer with legend
p.line(x, y, legend_label="Sine Wave", line_width=3, color="blue")

# Show the results
show(p)
