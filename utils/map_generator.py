import folium
import numpy as np

def create_map(city):
    """
    Create an interactive map with city data
    """
    # City coordinates (Indian cities)
    city_coords = {
        "Mumbai": (19.0760, 72.8777),
        "Delhi": (28.6139, 77.2090),
        "Bangalore": (12.9716, 77.5946),
        "Hyderabad": (17.3850, 78.4867),
        "Chennai": (13.0827, 80.2707),
        "Kolkata": (22.5726, 88.3639),
        "Pune": (18.5204, 73.8567),
        "Ahmedabad": (23.0225, 72.5714)
    }

    # Create base map
    m = folium.Map(
        location=city_coords.get(city, (28.6139, 77.2090)),  # Default to Delhi
        zoom_start=12,
        tiles='cartodbpositron'
    )

    # Add existing stations (mock data)
    for _ in range(10):
        lat = city_coords[city][0] + np.random.uniform(-0.05, 0.05)
        lon = city_coords[city][1] + np.random.uniform(-0.05, 0.05)

        folium.CircleMarker(
            location=[lat, lon],
            radius=8,
            color='blue',
            fill=True,
            popup='Existing Station'
        ).add_to(m)

    # Add suggested locations (mock data)
    for _ in range(5):
        lat = city_coords[city][0] + np.random.uniform(-0.05, 0.05)
        lon = city_coords[city][1] + np.random.uniform(-0.05, 0.05)

        folium.CircleMarker(
            location=[lat, lon],
            radius=8,
            color='green',
            fill=True,
            popup='Suggested Location'
        ).add_to(m)

    return m