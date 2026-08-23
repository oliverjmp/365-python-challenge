import streamlit as st
import pandas as pd
from src.data_processor import process_analytics_data

st.set_page_config(
    page_title="D172 - Dockerized Streamlit App",
    page_icon="🐳",
    layout="wide"
)

st.title("🐳 Panel Analítico Contenedorizado (D172)")
st.markdown("Aplicación de Streamlit empaquetada mediante Docker optimizado para entornos de producción.")

# Generar datos de muestra para el panel
data = {
    "Categoria": ["A", "B", "C", "D"],
    "Metrica_1": [120, 450, 300, 520],
    "Metrica_2": [85, 310, 240, 410]
}
df_raw = pd.DataFrame(data)

st.subheader("📊 Datos Procesados por el Módulo")
df_processed = process_analytics_data(df_raw)
st.dataframe(df_processed, use_container_width=True)

st.success("✨ Contenedor Docker ejecutándose de forma estable y portable.")