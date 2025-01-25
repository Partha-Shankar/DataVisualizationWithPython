import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Generate a time series dataset
np.random.seed(42)
date_range = pd.date_range(start='2023-01-01', periods=200, freq='D')
data = np.random.randn(200).cumsum()  # Cumulative sum to simulate a time series
volatility = np.random.rand(200) * 5  # Simulate volatility

# Create a DataFrame
df = pd.DataFrame({'Date': date_range, 'Value': data, 'Volatility': volatility})

# Create a time series plot
time_series_plot = go.Figure()

# Add the time series data to the plot
time_series_plot.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Value'],
    mode='lines+markers',
    name='Original Data',
    line=dict(shape='linear', color='blue'),
    marker=dict(size=5, color='red', opacity=0.7)
))

# Add volatility as a secondary y-axis representation
time_series_plot.add_trace(go.Bar(
    x=df['Date'],
    y=df['Volatility'],
    name='Volatility',
    marker=dict(color='orange', opacity=0.6)
))

# Customize the layout
time_series_plot.update_layout(
    title='Time Series Plot with Volatility',
    xaxis_title='Date',
    yaxis_title='Value',
    xaxis=dict(showgrid=True, gridcolor='lightgray', tickangle=45),
    yaxis=dict(showgrid=True, gridcolor='lightgray'),
    template='plotly_white',
    barmode='overlay'
)

# Show the plot
time_series_plot.show()
