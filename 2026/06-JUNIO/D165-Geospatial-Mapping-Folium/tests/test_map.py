import pandas as pd
import folium
from src.map_builder import create_operations_map

def test_create_operations_map():
    data = {
        "location_name": ["Test Point"],
        "latitude": [40.4],
        "longitude": [-3.7],
        "category": ["Test"]
    }
    df = pd.DataFrame(data)
    m = create_operations_map(df)
    
    assert isinstance(m, folium.Map)