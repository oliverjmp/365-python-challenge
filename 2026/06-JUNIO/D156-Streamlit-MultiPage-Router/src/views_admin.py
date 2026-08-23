import streamlit as st

def render_admin_view() -> None:
    """Renderiza el panel exclusivo para administradores de sistema."""
    st.header("Panel de Administración Global")
    st.write("Bienvenido al núcleo de control y auditoría de perfiles empresariales.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Usuarios Activos", "1,245", "+12%")
    col2.metric("Carga del Servidor", "42%", "-3%")
    col3.metric("Incidentes Críticos", "0", "Estable")