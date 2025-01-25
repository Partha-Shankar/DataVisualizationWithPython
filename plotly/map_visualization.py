import plotly.express as px
import pandas as pd

# Create a sample dataset with geographical coordinates and additional data
data = {
    'City': ['Bengaluru', 'Hyderabad', 'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Hubli', 'London', 'Tokyo'],
    'Latitude': [12.971599, 17.387140, 40.7128, 34.0522, 41.8781, 29.7604, 33.4484, 15.364708, 51.5074, 35.6762],
    'Longitude': [77.594566, 78.491684, -74.0060, -118.2437, -87.6298, -95.3698, -112.0740, 75.123955, -0.1278, 139.6503],
    'Population': [25000000, 8419600, 3980400, 2716000, 2328000, 1690000, 23000000, 15000000, 8982000, 37400068],
    'Region': ['Asia', 'Asia', 'North America', 'North America', 'North America', 'North America', 'North America', 'Asia', 'Europe', 'Asia']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter map with enhanced customization
map_fig = px.scatter_geo(
    df,
    lat='Latitude',
    lon='Longitude',
    text='City',  # Text to display on hover
    size='Population',  # Size of markers based on population
    color='Population',  # Color markers based on population
    color_continuous_scale='Viridis',  # Use a continuous color scale
    hover_name='City',  # Display city name on hover
    hover_data={'Latitude': False, 'Longitude': False, 'Population': True, 'Region': True},  # Display population and region on hover
    projection='orthographic',  # Change map projection to 'orthographic'
    title='City Populations Around the World',
    template='plotly_dark',  # Use a dark-themed template
    scope='world',  # Set the map scope to the entire world
)

# Add a custom marker style
map_fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')),  # Outline of markers
                     selector=dict(mode='markers'))

# Customize layout with additional map options
map_fig.update_layout(
    geo=dict(
        showcoastlines=True,
        coastlinecolor='Black',
        coastlinewidth=2,
        projection_type='natural earth',  # Set the projection type
        landcolor='lightgray',  # Land color
        showland=True,  # Display land
        showocean=True,  # Display ocean
        oceancolor='lightblue',  # Ocean color
    ),
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
    font=dict(size=12),  # Font size for labels
)

# Show the map
map_fig.show()
