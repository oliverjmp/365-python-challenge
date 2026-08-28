import streamlit as st
import numpy as np
from src.shared_mem_core import SharedMemoryManagerEngine

st.set_page_config(
    page_title="D225 - Shared Memory Manager Enterprise",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 D225: Panel de Memoria Compartida Interprocesos (Zero-Copy)")
st.markdown("""
Demostración de intercambio de matrices de gran tamaño entre procesos mediante **`multiprocessing.shared_memory`**. 
Al compartir un segmento de memoria física del sistema operativo, se elimina por completo la penalización de rendimiento (*overhead*) 
asociada a la serialización por *pickle* e IPC tradicional.
""")

st.sidebar.header("Configuración de Matriz")
row_val = st.sidebar.slider("Filas de la Matriz", min_value=2, max_value=5, value=3)
col_val = st.sidebar.slider("Columnas de la Matriz", min_value=2, max_value=5, value=3)

if st.button("🚀 Ejecutar Computación en Memoria Compartida", type="primary"):
    initial_matrix = np.arange(1, row_val * col_val + 1, dtype=np.int64).reshape((row_val, col_val))
    
    engine = SharedMemoryManagerEngine()
    with st.spinner("Asignando bloque en memoria compartida y ejecutando proceso hijo..."):
        summary = engine.execute_shared_computation(initial_matrix)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Matriz Inicial (Padre)")
        st.write(initial_matrix)
    with col2:
        st.subheader("Matriz Modificada (Hijo - In-place x2)")
        st.write(np.array(summary["modified_data"]))

    st.success("¡Matriz procesada exitosamente mediante memoria compartida sin copias redundantes!")
    st.metric("Suma Total de Elementos (Procesada)", summary["computation_result"]["sum"])
else:
    st.info("Ajusta las dimensiones de la matriz en el panel lateral y haz clic en **Ejecutar Computación en Memoria Compartida**.")