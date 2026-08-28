import streamlit as st
from src.cpu_core import MultiprocessingCPUBoundManager
import time

st.set_page_config(
    page_title="D224 - Multiprocessing CPU-Bound Enterprise",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ D224: Panel de Procesamiento Numérico Paralelo (Superando el GIL)")
st.markdown("""
Demostración de computación intensiva de CPU mediante **`multiprocessing`** y `ProcessPoolExecutor`. 
Al utilizar procesos independientes en lugar de hilos (*threads*), se evita por completo la restricción del GIL (*Global Interpreter Lock*), 
aprovechando al 100% los núcleos físicos del procesador.
""")

st.sidebar.header("Parámetros de Computación")
input_numbers = st.sidebar.text_input("Números a calcular (separados por comas)", value="1000, 2000, 3000, 4000")
max_workers = st.sidebar.slider("Número de Procesos Paralelos (Workers)", min_value=1, max_value=8, value=4, step=1)

if st.button("🚀 Iniciar Procesamiento Paralelo", type="primary"):
    try:
        numbers = [int(n.strip()) for n in input_numbers.split(",") if n.strip()]
    except ValueError:
        numbers = []

    if not numbers:
        st.warning("Por favor introduce una lista válida de números enteros separados por comas.")
    else:
        manager = MultiprocessingCPUBoundManager()
        with st.spinner(f"Ejecutando cálculos pesados en {max_workers} procesos paralelos..."):
            start_time = time.perf_counter()
            summary = manager.compute_batch(numbers, max_workers=max_workers)
            total_duration = time.perf_counter() - start_time

        col1, col2, col3 = st.columns(3)
        col1.metric("Operaciones Realizadas", summary["total_computations"])
        col2.metric("Procesos Utilizados", summary["max_workers_used"])
        col3.metric("Tiempo de Ejecución Global", f"{round(total_duration, 4)} s")

        st.success("¡Carga pesada de CPU procesada en paralelo exitosamente!")
        with st.expander("🔍 Ver resultados detallados por proceso"):
            st.dataframe(summary["results"], use_container_width=True)
else:
    st.info("Configura los valores numéricos y el número de workers en el panel lateral y haz clic en **Iniciar Procesamiento Paralelo**.")