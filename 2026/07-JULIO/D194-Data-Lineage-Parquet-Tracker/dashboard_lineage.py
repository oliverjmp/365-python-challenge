import streamlit as st
import pandas as pd
from src.lineage_engine import DataLineageTracker # Nota: Ajustar import según ruta de src

st.set_page_config(
    page_title="D194 - Data Lineage Parquet Tracker",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Panel de Gobernanza y Linaje de Datos (D194)")
st.markdown("Sistema de rastreo automatizado de dependencias y transformaciones sobre ficheros **Parquet** en el Data Lake.")

tracker = DataLineageTracker()
lineage_data = tracker.obtener_linaje()

st.sidebar.header("🎛️ Opciones de Auditoría")
st.sidebar.success("Motor de Linaje Conectado al Data Lake.")

# Métricas Globales
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Artefactos Monitoreados", len(lineage_data["nodes"]))
with col2:
    st.metric("Relaciones de Linaje", len(lineage_data["edges"]))
with col3:
    st.metric("Última Actualización", lineage_data["last_updated"].split(".")[0])

st.markdown("---")
st.subheader("📦 Inventario de Datasets en el Data Lake (Nodos)")
df_nodes = pd.DataFrame(lineage_data["nodes"])
st.dataframe(df_nodes, use_container_width=True)

st.markdown("---")
st.subheader("🔗 Mapa de Dependencias y Transformaciones (Edges)")
df_edges = pd.DataFrame(lineage_data["edges"])
st.dataframe(df_edges, use_container_width=True)

st.markdown("---")
st.info("💡 Este panel permite certificar el flujo de linaje de datos garantizando la trazabilidad corporativa ante auditorías de cumplimiento.")