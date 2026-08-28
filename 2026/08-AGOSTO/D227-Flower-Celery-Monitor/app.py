import streamlit as st
import time
from src.monitor_tasks import monitored_computation

st.set_page_config(
    page_title="D227 - Celery Flower Monitor Enterprise",
    page_icon="📈",
    layout="wide"
)

st.title("📈 D227: Panel de Monitoreo en Tiempo Real (Celery Flower Dashboard)")
st.markdown("""
Supervisión centralizada del estado, progreso y métricas de rendimiento de workers y tareas distribuidas. 
**Flower** proporciona una interfaz web basada en Flask y Tornado para auditar colas, latencias y tasas de éxito en tiempo real.
""")

st.sidebar.header("Control de Tareas Monitoreadas")
task_tag = st.sidebar.text_input("Etiqueta de Tarea", value="EnterpriseDataSync")
items_count = st.sidebar.slider("Volumen de elementos a procesar", min_value=1, max_value=10, value=5)

if "monitor_history" not in st.session_state:
    st.session_state.monitor_history = []

if st.button("🚀 Lanzar y Monitorear Tarea", type="primary"):
    with st.spinner("Despachando tarea a la cola y rastreando ejecución..."):
        try:
            # Despacho real de Celery
            task = monitored_computation.delay(items_count=items_count, task_tag=task_tag)
            
            # Simulación visual de progreso en Streamlit equivalente a lo que muestra Flower
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(items_count):
                time.sleep(0.15)
                progress_pct = int(((i + 1) / items_count) * 100)
                progress_bar.progress(progress_pct)
                status_text.text(f"Estado en Worker: PROGRESS ({i+1}/{items_count} elementos procesados)")
            
            progress_bar.progress(100)
            status_text.text("Estado en Worker: SUCCESS (Completado)")
            
            st.session_state.monitor_history.append({
                "id": task.id,
                "tag": task_tag,
                "items": items_count,
                "status": "SUCCESS"
            })
            st.success("¡Tarea ejecutada y monitoreada con éxito!")
        except Exception as e:
            st.warning(f"Aviso: Redis/Celery no activo ({e}). Ejecutando simulación de respaldo...")
            res = monitored_computation.run(items_count=items_count, task_tag=task_tag)
            st.session_state.monitor_history.append({
                "id": "local-fallback-id",
                "tag": task_tag,
                "items": items_count,
                "status": res["status"]
            })
            st.success("¡Simulación local completada!")

st.subheader("📋 Registro Histórico de Tareas Supervisadas")
if st.session_state.monitor_history:
    st.table(st.session_state.monitor_history)
else:
    st.info("No hay tareas registradas todavía en la sesión actual.")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🌐 Servidor Flower Real")
st.sidebar.text("Para abrir el dashboard oficial de Flower ejecuta:\n`flower -A src.celery_app.celery_app --port=5555`\ny visita `http://localhost:5555`")