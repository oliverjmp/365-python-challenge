import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
from src.map_builder import create_operations_map

st.set_page_config(
    page_title="D165 - Geospatial Mapping",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ D165: Mapa Interactivo de Operaciones con Folium")
st.markdown("Visualización geoespacial de sucursales, centros logísticos y densidad de operaciones.")

# Datos simulados de ubicaciones (ejemplo con coordenadas de Madrid)
data = {
    "location_name": ["Oficina Central", "Centro Logístico Norte", "Hub Tecnológico Sur"],
    "latitude": [40.4168, 40.4500, 40.3800],
    "longitude": [-3.7038, -3.6800, -3.7200],
    "category": ["Corporativo", "Logística", "Innovación"]
}
df_locs = pd.DataFrame(data)

st.subheader("📊 Datos de Ubicaciones Registradas")
st.dataframe(df_locs, use_container_width=True)

# Generar e integrar el mapa
st.subheader("📍 Mapa Geoespacial Interactivo")
interactive_map = create_operations_map(df_locs)
st_folium(interactive_map, width=700, height=500)