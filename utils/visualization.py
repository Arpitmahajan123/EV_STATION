import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def create_heatmap(city):
    """
    Create population density heatmap
    """
    # Generate mock data
    x = np.linspace(0, 10, 20)
    y = np.linspace(0, 10, 20)
    X, Y = np.meshgrid(x, y)
    Z = np.random.normal(5, 2, (20, 20))
    
    fig = go.Figure(data=go.Heatmap(
        z=Z,
        colorscale='Viridis',
        showscale=True
    ))
    
    fig.update_layout(
        title=f'Population Density Heatmap - {city}',
        xaxis_title='Longitude',
        yaxis_title='Latitude'
    )
    
    return fig

def create_traffic_flow(city):
    """
    Create traffic flow visualization
    """
    # Generate mock data
    hours = list(range(24))
    traffic = np.random.normal(1000, 200, 24)
    
    fig = go.Figure(data=go.Scatter(
        x=hours,
        y=traffic,
        mode='lines+markers',
        line=dict(color='#1f77b4', width=2),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title=f'Daily Traffic Flow - {city}',
        xaxis_title='Hour of Day',
        yaxis_title='Traffic Volume'
    )
    
    return fig
