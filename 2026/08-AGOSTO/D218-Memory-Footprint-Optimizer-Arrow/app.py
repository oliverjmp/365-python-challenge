import streamlit as st
import pandas as pd
from src.memory_optimizer import ArrowMemoryOptimizer

st.set_page_config(page_title="D218 - PyArrow Memory Pools", layout="wide")

st.title("🧠 D218: Monitor y Optimización de Footprint de Memoria (PyArrow)")
st.markdown("Gestión avanzada de asignadores de memoria para evitar la fragmentación en RAM durante el procesamiento analítico masivo.")

st.sidebar.header("⚙️ Configuración del Dataset")
num_rows = st.sidebar.slider("Número de filas a simular en RAM", 10000, 1000000, 100000, step=10000)

# Mostrar estadísticas del Pool actual
stats = ArrowMemoryOptimizer.get_memory_pool_stats()

col1, col2, col3 = st.columns(3)
col1.metric("Backend de Memoria", stats["backend_name"].upper())
col2.metric("Memoria Actual Asignada", f"{stats['bytes_allocated'] / (1024*1024):.2f} MB")
col3.metric("Pico Máximo de Memoria", f"{stats['max_memory'] / (1024*1024):.2f} MB")

st.markdown("---")
if st.button("🚀 Ejecutar Procesamiento Masivo en Memoria Columnar"):
    with st.spinner("Procesando bloques de datos bajo la piscina de Arrow..."):
        df_sim = pd.DataFrame({
            "id": range(1, num_rows + 1),
            "valor_numerico": [float(i) * 3.14 for i in range(1, num_rows + 1)],
            "categoria": ["Enterprise_Data"] * num_rows
        })
        df_res, metrics = ArrowMemoryOptimizer.process_large_dataset_with_pool(df_sim)
        
    st.success(f"¡Procesados {metrics['rows_processed']:,} registros exitosamente!")
    st.json(metrics)