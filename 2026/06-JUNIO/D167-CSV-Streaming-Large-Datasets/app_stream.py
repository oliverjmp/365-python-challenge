import streamlit as st
import pandas as pd
import numpy as np
import os
from src.streamer import stream_csv_chunks, calculate_streaming_metrics

st.set_page_config(
    page_title="D167 - CSV Streaming Datasets",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 D167: Generador y Procesador de Datasets Masivos")
st.markdown("Genera un fichero CSV grande en caliente, descárgalo a tu CPU y procésalo mediante streaming para proteger la memoria RAM.")

# Función para generar y descargar un archivo CSV grande
@st.cache_data
def generate_large_csv_file(num_rows: int = 50000) -> bytes:
    np.random.seed(42)
    df_large = pd.DataFrame({
        "id": range(1, num_rows + 1),
        "category": np.random.choice(["Finance", "Operations", "Tech", "HR", "Sales"], num_rows),
        "value": np.random.uniform(50.0, 1000.0, num_rows),
        "active": np.random.choice([True, False], num_rows)
    })
    return df_large.to_csv(index=False).encode('utf-8')

# Sección de descarga en la barra lateral
st.sidebar.header("📥 Descarga de Dataset Masivo")
num_rows_to_generate = st.sidebar.slider("Número de filas del CSV", 10000, 200000, 50000, 10000)

csv_bytes = generate_large_csv_file(num_rows_to_generate)

st.sidebar.download_button(
    label="💾 Descargar CSV Masivo a CPU",
    data=csv_bytes,
    file_name=f"dataset_masivo_{num_rows_to_generate}_filas.csv",
    mime="text/csv"
)

# Ruta local temporal para procesar por streaming en la app
sample_path = "temp_large_dataset.csv"
with open(sample_path, "wb") as f:
    f.write(csv_bytes)

st.sidebar.markdown("---")
st.sidebar.header("⚙️ Configuración de Streaming")
chunk_size = st.sidebar.slider("Tamaño del Bloque (Chunk Size)", 1000, 10000, 5000, 1000)

if st.button("🚀 Procesar Dataset en Streaming desde Memoria"):
    with st.spinner("Procesando bloques de datos en streaming optimizado..."):
        metrics = calculate_streaming_metrics(sample_path, chunk_size)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Registros Procesados", f"{metrics['total_rows']:,}")
        with col2:
            st.metric("Suma Total Acumulada", f"${metrics['total_value']:,.2f}")
        with col3:
            st.metric("Promedio General", f"${metrics['avg_value']:,.2f}")
            
        st.markdown("---")
        st.subheader("🔍 Visualización del Primer Bloque (Chunk)")
        first_chunk = next(stream_csv_chunks(sample_path, chunk_size))
        st.dataframe(first_chunk.head(10), use_container_width=True)