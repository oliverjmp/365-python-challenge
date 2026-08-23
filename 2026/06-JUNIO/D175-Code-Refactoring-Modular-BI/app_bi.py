import streamlit as st
from controllers.kpi_controller import load_kpi_data

st.set_page_config(page_title="BI Dashboard - MVC", page_icon="📊", layout="wide")

st.title("📊 Panel de Business Intelligence (Patrón MVC)")
st.writ("Refactorización estructural del código base aplicando Modelo-Vista-Controlador.")

# Configuración en la barra lateral
st.sidebar.header("Configuración de Datos")
default_query = "SELECT id, categoria, valor, fecha FROM kpis_operativos;"
query = st.sidebar.text_area("Consulta SQL", value=default_query, height=150)

if st.button("Consultar Base de Datos"):
    df, success = load_kpi_data(query)
    if success:
        st.success(f"¡Datos obtenidos con éxito! ({len(df)} registros)")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No se pudieron recuperar datos. Verifica la conexión o la tabla.")
    