import streamlit as st
from src.app_core import StreamlitCoreManager

# Configuración de página responsiva
st.set_page_config(
    page_title="D151 - Streamlit Core Architecture",
    page_icon="🚀",
    layout="wide"
)

manager = StreamlitCoreManager()

# Inicializar estado de sesión en Streamlit
manager.initialize_state(st.session_state)

# Panel Lateral (Sidebar)
st.sidebar.title("⚙️ Configuración")
st.sidebar.info("Hito D151: Gestión de estado y arquitectura base.")

new_name = st.sidebar.text_input("Ingrese su nombre:", value=st.session_state["user_name"])
if new_name != st.session_state["user_name"]:
    manager.update_user_name(st.session_state, new_name)

# Cuerpo Principal
st.title("🚀 Aplicación Base con Streamlit y State Management")
st.markdown(f"¡Bienvenido, **{st.session_state['user_name']}**! Esta interfaz demuestra la persistencia de estado nativa en Streamlit.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Contador Interactivo")
    st.write(f"Valor actual del contador: **{st.session_state['counter']}**")
    if st.button("Incrementar Contador ➕"):
        manager.increment_counter(st.session_state)
        st.rerun()

with col2:
    st.subheader("Estado de Sesión Actual")
    st.json(dict(st.session_state))