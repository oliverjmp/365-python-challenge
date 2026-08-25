import streamlit as st
import pandas as pd
from src.spatial_runner import SpatialQueryRunner

st.set_page_config(
    page_title="D201 - DuckDB Spatial & Geospatial",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Laboratorio Geoespacial con DuckDB Spatial")
st.markdown("Visualización y transformación de coordenadas geográficas mediante la extensión espacial de DuckDB.")

try:
    runner = SpatialQueryRunner()
    datos = runner.ejecutar_consulta_espacial()
    
    df = pd.DataFrame(datos, columns=["ID", "Nombre", "Latitud", "Longitud", "Geometría WKT"])
    
    st.subheader("📋 Tabla de Puntos de Interés y Geometrías WKT")
    st.dataframe(df, use_container_width=True)
    
    st.subheader("📍 Mapa de Localización")
    # Streamlit soporta mapas nativos si se pasan columnas 'lat' y 'lon'
    map_df = df.rename(columns={"Latitud": "lat", "Longitud": "lon"})
    st.map(map_df[['lat', 'lon']])

except Exception as e:
    st.error(f"❌ Error al procesar el motor espacial: {e}")