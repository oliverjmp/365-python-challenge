import streamlit as st
from controllers.async_controller import run_async_query

st.set_page_config(page_title="BI Dashboard - Async Refresher", page_icon="⚡", layout="wide")

st.title("⚡ Panel de BI con Actualización Asíncrona (D176)")
st.write("Sistema de carga en segundo plano con `asyncio` sin bloquear la interfaz.")

# Barra lateral de configuración
st.sidebar.header("Configuración Asíncrona")
default_query = "SELECT id, categoria, valor, fecha FROM kpis_operativos;"
query = st.sidebar.text_area("Consulta SQL", value=default_query, height=150)

if st.button("Consultar Asíncronamente"):
    # Streamlit muestra un spinner amigable mientras el bucle asíncrono procesa en segundo plano
    with st.spinner("Actualizando datos de forma asíncrona..."):
        df, success = run_async_query(query)
        
    if success:
        st.success(f"¡Datos actualizados asíncronamente con éxito! ({len(df)} registros)")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No se pudieron recuperar datos de forma asíncrona.")