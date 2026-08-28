import asyncio
import streamlit as st
from src.queue_core import AsyncQueueManager

st.set_page_config(
    page_title="D223 - Async Queue Producer-Consumer",
    page_icon="🔄",
    layout="wide"
)

st.title("🔄 D223: Panel de Procesamiento Desacoplado (Productor-Consumidor)")
st.markdown("""
Demostración interactiva del patrón **Productor-Consumidor** mediante buffers acotados en memoria (`asyncio.Queue`), 
permitiendo un desacoplamiento eficiente entre la generación de tareas y su procesamiento concurrente.
""")

st.sidebar.header("Parámetros del Pipeline")
num_items = st.sidebar.slider("Cantidad de elementos a procesar", min_value=5, max_value=50, value=15, step=5)
num_consumers = st.sidebar.slider("Número de consumidores concurrentes", min_value=1, max_value=8, value=3, step=1)
queue_capacity = st.sidebar.slider("Capacidad máxima de la cola (maxsize)", min_value=1, max_value=20, value=5, step=1)

if st.button("🚀 Ejecutar Pipeline Asíncrono", type="primary"):
    manager = AsyncQueueManager(maxsize=queue_capacity)
    items = [f"Item-{i}" for i in range(1, num_items + 1)]
    
    with st.spinner(f"Procesando {num_items} elementos con {num_consumers} consumidores..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        summary = loop.run_until_complete(manager.run_pipeline(items, num_consumers=num_consumers))
        loop.close()

    col1, col2, col3 = st.columns(3)
    col1.metric("Producidos", summary["total_produced"])
    col2.metric("Consumidos", summary["total_consumed"])
    col3.metric("Consumidores Activos", summary["consumers_count"])

    st.success("¡Pipeline ejecutado con éxito bajo desacoplamiento asíncrono!")
    with st.expander("🔍 Ver traza de eventos de los consumidores"):
        st.dataframe(summary["results"], use_container_width=True)
else:
    st.info("Configura los parámetros en el panel lateral y haz clic en **Ejecutar Pipeline Asíncrono**.")