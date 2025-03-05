import numpy as np

def score_locations(population_density, traffic_volume, existing_stations):
    """
    Score potential locations based on input parameters
    Returns list of (location, score) tuples
    """
    # Mock locations for demonstration
    locations = [
        "Downtown",
        "Shopping District",
        "Business Park",
        "Residential Area",
        "Highway Junction",
        "University Campus",
        "Industrial Zone",
        "Sports Complex"
    ]
    
    scores = []
    for location in locations:
        # Calculate base score
        base_score = np.random.uniform(0.5, 1.0)
        
        # Apply weights to different factors
        population_score = min(population_density / 10000, 1.0) * 0.4
        traffic_score = min(traffic_volume / 50000, 1.0) * 0.4
        station_density_score = max(1 - (existing_stations / 100), 0.1) * 0.2
        
        # Calculate final score
        final_score = base_score * (population_score + traffic_score + station_density_score)
        
        scores.append((location, final_score))
    
    # Sort by score descending
    return sorted(scores, key=lambda x: x[1], reverse=True)
