import streamlit as st
import json
from src.webhook_client import trigger_webhook

st.set_page_config(
    page_title="D171 - Webhook Trigger Panel",
    page_icon="🔌",
    layout="wide"
)

st.title("🔌 Panel Operativo de Webhooks y Alertas (D171)")
st.markdown("Gestiona, dispara y audita webhooks hacia tus servicios externos o sistemas de mensajería.")

st.sidebar.header("⚙️ Configuración del Envío")
webhook_url = st.sidebar.text_input("URL del Webhook", value="https://httpbin.org/post")
timeout_val = st.sidebar.slider("Timeout (segundos)", min_value=1, max_value=15, value=5)

st.subheader("📦 Payload JSON")
default_payload = '{\n  "evento": "alerta_sistema",\n  "nivel": "info",\n  "mensaje": "Prueba manual de webhook desde Streamlit"\n}'
payload_text = st.text_area("Edita el payload en formato JSON", value=default_payload, height=150)

if st.button("🚀 Disparar Webhook", type="primary"):
    try:
        parsed_payload = json.loads(payload_text)
    except json.JSONDecodeError as err:
        st.error(f"Error de sintaxis en el JSON del payload: {err}")
        parsed_payload = None

    if parsed_payload is not None:
        with st.spinner("Enviando petición HTTP..."):
            result = trigger_webhook(webhook_url, parsed_payload, timeout=timeout_val)

        st.markdown("---")
        st.subheader("📋 Resultado de la Ejecución")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Código de Estado HTTP", result["status_code"])
        with col2:
            st.metric("Estado de la Operación", "Éxito" if result["success"] else "Fallo")

        st.text_area("Cuerpo de la Respuesta", value=str(result["response"]), height=200)