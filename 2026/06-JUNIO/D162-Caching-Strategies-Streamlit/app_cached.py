import streamlit as st
import time
from src.data_loader import load_cached_data

st.set_page_config(
    page_title="D162 - Caché en Streamlit",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ D162: Estrategias de Caché en Streamlit")
st.markdown("Demostración práctica de optimización de rendimiento con `@st.cache_data`.")

# Sidebar de control
st.sidebar.header("Panel de Control")
rows = st.sidebar.slider("Registros a consultar", 1000, 30000, 10000, 5000)

if st.sidebar.button("🧹 Limpiar Caché"):
    load_cached_data.clear()
    st.sidebar.success("¡Caché borrada exitosamente!")

# Medición de tiempo
start = time.time()
df = load_cached_data(rows)
duration = time.time() - start

# Métricas en pantalla
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tiempo de Carga", f"{duration:.4f} s")
with col2:
    st.metric("Total Registros", len(df))
with col3:
    st.metric("Estado de Caché", "Instantánea 🚀" if duration < 0.2 else "Carga Inicial ⏳")

st.markdown("---")
st.subheader("Vista Previa de los Datos")
st.dataframe(df.head(10), use_container_width=True)