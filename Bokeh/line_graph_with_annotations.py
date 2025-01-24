from bokeh.plotting import figure, show, output_file
from bokeh.models import Label, Arrow, NormalHead
import numpy as np

# Output file
output_file("bokeh_enhanced_line_graph.html")

# Prepare some data
x = np.linspace(10, 100, 100)
y1 = np.sin(x / 10) * 2
y2 = np.cos(x / 10) * 2

# Create a new plot with a title and axis labels
p = figure(title="Enhanced Line Graph with Annotations", x_axis_label="X Axis", y_axis_label="Y Axis")

# Add multiple line renderers with legends
p.line(x, y1, legend_label="Sine Wave", line_width=3, color="blue")
p.line(x, y2, legend_label="Cosine Wave", line_width=3, color="red", line_dash="dashed")

# Adding annotations (Label and Arrow)
label = Label(x=50, y=1.5, text="Peak Point", text_font_size="12pt", text_color="black")
p.add_layout(label)

arrow = Arrow(end=NormalHead(size=10), x_start=50, y_start=1.5, x_end=50, y_end=1.0)
p.add_layout(arrow)

# Styling the legend
p.legend.title = "Legend"
p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"
p.legend.label_text_color = "navy"
p.legend.border_line_width = 2
p.legend.border_line_color = "black"
p.legend.border_line_alpha = 0.8
p.legend.background_fill_color = "lightgray"
p.legend.background_fill_alpha = 0.3

# Show the results
show(p)
