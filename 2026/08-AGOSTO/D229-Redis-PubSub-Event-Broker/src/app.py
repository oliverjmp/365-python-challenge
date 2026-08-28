import streamlit as st
import json
from src.publisher import EventPublisher
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import json
from src.publisher import EventPublisher

st.set_page_config(
    page_title="D229 - Redis Pub/Sub Dashboard",
    page_icon="📡",
    layout="wide"
)

st.title("📡 D229: Panel de Mensajería en Tiempo Real (Redis Pub/Sub)")
st.markdown("""
Simulación interactiva de una **Arquitectura Orientada a Eventos (EDA)**. Publica mensajes a canales específicos 
y observa cómo los suscriptores procesan la información de manera desacoplada.
""")

if "event_log" not in st.session_state:
    st.session_state.event_log = []

st.sidebar.header("📤 Publicador de Eventos")
channel_name = st.sidebar.selectbox("Canal de Destino", ["orders", "notifications", "telemetry", "payments"])
event_type = st.sidebar.selectbox("Tipo de Evento", ["ORDER_CREATED", "USER_LOGIN", "SYSTEM_ALERT", "PAYMENT_PROCESSED"])
message_payload = st.sidebar.text_area("Payload (JSON simulado)", '{"id": 100, "user": "oliver", "amount": 150.0}')

if st.sidebar.button("🚀 Publicar Evento", type="primary"):
    try:
        publisher = EventPublisher()
        parsed_payload = json.loads(message_payload)
        receivers = publisher.publish_event(channel_name, event_type, parsed_payload)
        
        st.session_state.event_log.insert(0, {
            "channel": channel_name,
            "type": event_type,
            "payload": parsed_payload,
            "receivers": receivers,
            "status": "PUBLICADO (Real Redis)"
        })
        st.success(f"¡Evento publicado con éxito en el canal `{channel_name}`! Receptores alcanzados: {receivers}")
    except Exception as e:
        st.warning(f"Redis no disponible ({e}). Registrando en modo simulación local.")
        try:
            parsed_payload = json.loads(message_payload)
        except Exception:
            parsed_payload = {"raw": message_payload}
            
        st.session_state.event_log.insert(0, {
            "channel": channel_name,
            "type": event_type,
            "payload": parsed_payload,
            "receivers": 1,
            "status": "SIMULADO (Sin Redis activo)"
        })

st.subheader("📥 Registro de Eventos Recibidos (Subscriber Feed)")

col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🧹 Limpiar Registro"):
        st.session_state.event_log = []
        st.rerun()

if st.session_state.event_log:
    for idx, ev in enumerate(st.session_state.event_log):
        with st.container():
            st.info(f"**Canal:** `{ev['channel']}` | **Evento:** `{ev['type']}` | **Estado:** {ev['status']}")
            st.json(ev['payload'])
            st.markdown("---")
else:
    st.info("No hay eventos registrados todavía. Utiliza el panel izquierdo para publicar el primer evento.")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Nota técnica")
st.sidebar.text("Para probar con un servidor Redis real:\nEjecuta `redis-server` en tu terminal local.")