import streamlit as st
from src.db_connector import fetch_bi_data

st.set_page_config(
    page_title="D173 - Docker Compose BI Stack",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Panel de Business Intelligence con PostgreSQL (D173)")
st.markdown("Stack analítico conectado a una base de datos relacional orquestada por Docker Compose.")

st.sidebar.subheader("⚙️ Configuración de Datos")
query_input = st.sidebar.text_area(
    "Consulta SQL", 
    value="SELECT id, categoria, valor, fecha FROM kpis_operativos;",
    height=100
)

if st.button("🔄 Consultar Base de Datos", type="primary"):
    with st.spinner("Conectando a PostgreSQL..."):
        df_result = fetch_bi_data(query_input)
    
    if df_result.empty:
        st.warning("No se pudieron recuperar datos. Verifica que el contenedor de PostgreSQL esté activo y la tabla exista.")
    else:
        st.success(f"¡Datos obtenidos con éxito! ({len(df_result)} registros)")
        st.dataframe(df_result, use_container_width=True)
else:
    st.info("Haz clic en el botón para cargar los datos desde la base de datos orquestada.")