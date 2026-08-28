import asyncio
import time
import streamlit as st
from src.async_core import AsyncEventLoopCore

st.set_page_config(
    page_title="D221 - Asyncio Event Loop Visualizer",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ D221: Panel de Control del Bucle de Eventos Asíncrono")
st.markdown("""
Esta aplicación web interactiva demuestra la **gestión de tareas concurrentes de alta densidad** 
utilizando el núcleo asíncrono de Python (`asyncio`). Ajusta los parámetros y observa el rendimiento en tiempo real.
""")

# Panel lateral de control
st.sidebar.header("Parámetros del Workload")
task_count = st.sidebar.slider("Número de tareas concurrentes (I/O)", min_value=1, max_value=500, value=50, step=10)
base_delay = st.sidebar.slider("Retardo simulado por tarea (segundos)", min_value=0.01, max_value=0.5, value=0.05, step=0.01)

if st.button("🚀 Ejecutar Workload Asíncrono", type="primary"):
    core = AsyncEventLoopCore()
    
    with st.spinner(f"Procesando {task_count} tareas de manera concurrente..."):
        start_time = time.perf_counter()
        
        # Ejecución del bucle de eventos asíncrono dentro de Streamlit
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        workload_summary = loop.run_until_complete(
            core.execute_concurrent_workload(task_count=task_count, base_delay=base_delay)
        )
        loop.close()
        
        total_time = time.perf_counter() - start_time

    # Métricas principales en pantalla
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Tareas", workload_summary["total_tasks"])
    col2.metric("Duración Global Real", f"{workload_summary['total_duration']} s")
    col3.metric("Tiempo Total de UI", f"{round(total_time, 4)} s")

    st.success("¡Carga concurrente procesada exitosamente sin bloquear el hilo principal!")

    # Visualización de resultados detallados en tabla
    with st.expander("🔍 Ver detalle de las tareas ejecutadas"):
        st.dataframe(workload_summary["results"], use_container_width=True)
else:
    st.info("Configura los parámetros en el panel izquierdo y haz clic en **Ejecutar Workload Asíncrono** para visualizar el comportamiento del sistema.")  