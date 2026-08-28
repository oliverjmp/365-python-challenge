import streamlit as st
from src.tasks import heavy_background_computation

st.set_page_config(
    page_title="D226 - Celery & Redis Task Queue Enterprise",
    page_icon="📨",
    layout="wide"
)

st.title("📨 D226: Panel de Gestión de Tareas Distribuidas (Celery + Redis)")
st.markdown("""
Demostración de arquitectura de colas de mensajes distribuidas para la ejecución asíncrona de tareas en segundo plano. 
Utiliza **Redis** como intermediario (*broker*) de alta velocidad y **Celery** para el despacho, enrutamiento y escalado de workers.
""")

st.sidebar.header("Parámetros de la Tarea")
task_label = st.sidebar.text_input("Nombre de la Tarea", value="ReportGeneration-Q3")
task_duration = st.sidebar.slider("Duración simulada (segundos)", min_value=1, max_value=10, value=3)

# Inicializar memoria de sesión para persistir el resultado en pantalla
if "task_result" not in st.session_state:
    st.session_state.task_result = None

if st.button("🚀 Encolar Tarea en Segundo Plano", type="primary"):
    try:
        # Intento de despacho real a Celery / Redis
        task = heavy_background_computation.delay(duration=task_duration, task_name=task_label)
        st.session_state.task_result = {
            "type": "celery",
            "id": task.id,
            "message": "¡Tarea despachada correctamente al broker Redis!"
        }
    except Exception as e:
        # Respaldo sorn / síncrono si Redis no está activo en local
        res = heavy_background_computation.run(duration=task_duration, task_name=task_label)
        st.session_state.task_result = {
            "type": "fallback",
            "data": res,
            "message": f"Aviso: No se detectó Redis activo ({e}). Ejecución local síncrona completada."
        }

# Mostrar el resultado guardado en sesión de forma persistente
if st.session_state.task_result:
    res_info = st.session_state.task_result
    if res_info["type"] == "celery":
        st.success(res_info["message"])
        st.metric("ID de Tarea en Celery", res_info["id"])
        st.info("💡 Para procesar esta tarea en tiempo real, recuerda levantar tu worker en la terminal con: `celery -A src.celery_app.celery_app worker --loglevel=info`")
    else:
        st.warning(res_info["message"])
        st.json(res_info["data"])
else:
    st.info("Configura los detalles de la tarea en el panel lateral y haz clic en **Encolar Tarea en Segundo Plano**.")