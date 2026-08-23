import folium
import pandas as pd

def create_operations_map(df_locations: pd.DataFrame) -> folium.Map:
    """
    Construye un mapa interactivo de Folium centrado en base a un DataFrame de ubicaciones.
    """
    # Centro inicial predeterminado (ejemplo: Madrid o coordenadas generales)
    center_lat = df_locations["latitude"].mean() if not df_locations.empty else 40.4168
    center_lon = df_locations["longitude"].mean() if not df_locations.empty else -3.7038

    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    for _, row in df_locations.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row.get("location_name", "Operación"),
            tooltip=row.get("category", "Punto de interés"),
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    return m