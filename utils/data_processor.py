import pandas as pd
import numpy as np
from io import StringIO

def process_city_data(city, population_density, traffic_volume, existing_stations):
    """
    Process city data and generate a report in CSV format
    """
    # Create a buffer for CSV data
    output = StringIO()
    
    # Generate mock data for the report
    data = {
        'Location': [f'Location {i}' for i in range(1, 11)],
        'Latitude': np.random.uniform(30, 45, 10),
        'Longitude': np.random.uniform(-120, -70, 10),
        'Population_Density': np.random.normal(population_density, 1000, 10),
        'Traffic_Volume': np.random.normal(traffic_volume, 5000, 10),
        'Distance_to_Existing': np.random.uniform(0.1, 5.0, 10),
        'Score': np.random.uniform(0.5, 1.0, 10)
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Sort by score
    df = df.sort_values('Score', ascending=False)
    
    # Write to CSV
    df.to_csv(output, index=False)
    
    return output.getvalue()

def load_sample_data():
    """
    Generate sample data for visualization
    """
    data = {
        'latitude': np.random.uniform(30, 45, 50),
        'longitude': np.random.uniform(-120, -70, 50),
        'usage_rate': np.random.uniform(0, 1, 50),
        'capacity': np.random.uniform(10, 50, 50)
    }
    return pd.DataFrame(data)
