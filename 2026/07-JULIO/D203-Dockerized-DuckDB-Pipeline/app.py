import streamlit as st
from src.pipeline_runner import DockerDuckDBPipeline

st.set_page_config(
    page_title="D203 - Dockerized DuckDB Pipeline",
    page_icon="🐳",
    layout="wide"
)

st.title("🐳 Dashboard Analítico Contenerizado")
st.markdown("Visualización de resultados del pipeline de DuckDB ejecutándose bajo arquitectura de contenedor.")

try:
    pipeline = DockerDuckDBPipeline()
    df = pipeline.ejecutar_proceso()
    
    st.subheader("📋 Resumen de Transacciones Agrupadas")
    st.dataframe(df, use_container_width=True)
    
    st.success("✅ Motor analítico operando correctamente en memoria.")
except Exception as e:
    st.error(f"❌ Error al ejecutar el pipeline: {e}")