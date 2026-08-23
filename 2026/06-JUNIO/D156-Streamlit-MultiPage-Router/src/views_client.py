import streamlit as st

def render_client_view() -> None:
    """Renderiza el portal de autoservicio para clientes finales."""
    st.header("Portal de Clientes y Reportes")
    st.write("Consulte el estado de sus solicitudes y métricas personalizadas.")
    
    st.info("No hay nuevas notificaciones en su bandeja de entrada.")
    selected_option = st.selectbox("Seleccione su categoría de interés:", ["Facturación", "Soporte Técnico", "Garantías"])
    st.write(f"Mostrando información detallada para: **{selected_option}**")