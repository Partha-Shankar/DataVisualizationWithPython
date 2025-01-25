import plotly.graph_objects as go
import numpy as np

# Generate sample data for 3D scatter plot
np.random.seed(42)
x = np.random.rand(200)
y = np.random.rand(200)
z = np.random.rand(200)
colors = np.random.rand(200)

# Create a 3D scatter plot with varying colors
scatter_plot = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=7,
        color=colors,
        colorscale='viridis',
        opacity=0.85,
        symbol='circle'
    )
)])

# Customize the layout for the scatter plot
scatter_plot.update_layout(
    title='3D Scatter Plot with Color Mapping',
    scene=dict(
        xaxis_title='X Frequencies',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis',
        xaxis=dict(showgrid=True, gridcolor='gray'),
        yaxis=dict(showgrid=True, gridcolor='gray'),
        zaxis=dict(showgrid=True, gridcolor='gray')
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    template='plotly_dark'
)

# Show the scatter plot
scatter_plot.show()

# Generate sample data for 3D surface plot
x_surf = np.linspace(-5, 5, 150)
y_surf = np.linspace(-5, 5, 150)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)
z_surf = np.sin(np.sqrt(x_surf ** 2 + y_surf ** 2)) + np.cos(np.sqrt(x_surf ** 2 + y_surf ** 2))

# Create a 3D surface plot with enhanced colorscale
surface_plot = go.Figure(data=[go.Surface(
    z=z_surf,
    x=x_surf,
    y=y_surf,
    colorscale='plasma',  # Available options: sunset, rainbow, reds, redor, agsunset, plasma
    showscale=True,
    contours_z=dict(show=True, usecolormap=True, highlightcolor="lime", project_z=True)
)])

# Customize the layout for the surface plot
surface_plot.update_layout(
    title='Enhanced 3D Surface Plot with Contours',
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis',
        camera=dict(eye=dict(x=2, y=2, z=1.5)),
        xaxis=dict(showgrid=True, gridcolor='gray'),
        yaxis=dict(showgrid=True, gridcolor='gray'),
        zaxis=dict(showgrid=True, gridcolor='gray')
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    template='plotly_dark'
)

# Show the surface plot
surface_plot.show()
