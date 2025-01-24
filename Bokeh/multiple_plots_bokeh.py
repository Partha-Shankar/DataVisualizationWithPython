from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot
import numpy as np
import pandas as pd

# Set up the output file
output_file("bokeh_enhanced_plots.html")

# Generate sample data
np.random.seed(42)
x = np.linspace(1, 10, 100)
y = 2 * x + 1 + np.random.normal(scale=1, size=x.shape)
categories = np.random.choice(['A', 'B'], size=x.shape)
data = pd.DataFrame({'x': x, 'y': y, 'category': categories})

# Create a line plot
line_plot = figure(title="Line Plot Example", x_axis_label='X Values', y_axis_label='Y Values')
line_plot.line(x, y, legend_label="Line", line_width=2, color='blue')

# Create a scatter plot
scatter_plot = figure(title="Scatter Plot Example", x_axis_label='X Values', y_axis_label='Y Values')
scatter_plot.scatter('x', 'y', source=data, color='red', legend_label="Scatter", size=15, marker='diamond')

# Create a histogram
data_hist = np.random.normal(0, 1, 2500)
hist, edges = np.histogram(data_hist, density=True, bins=20)
hist_plot = figure(title="Histogram Example", x_axis_label='X Values', y_axis_label='Frequency')
hist_plot.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color='green', line_color='black')

# Overlay a probability density function on histogram
x_pdf = np.linspace(-4.0, 4.0, 1000)
pdf = np.exp(-0.5 * x_pdf ** 2) / np.sqrt(2.0 * np.pi)
hist_plot.line(x_pdf, pdf, line_width=2, line_color="navy", legend_label="PDF")

# Customize legend styles
for p in [line_plot, scatter_plot, hist_plot]:
    p.legend.title = "Legend"
    p.legend.label_text_font = "times"
    p.legend.label_text_font_style = "italic"
    p.legend.label_text_color = "navy"
    p.legend.border_line_width = 2
    p.legend.border_line_color = "black"

# Arrange plots in a grid layout
layout = gridplot([[line_plot, None], [hist_plot, scatter_plot]], width=700, height=500)

# Show the plots
show(layout)
