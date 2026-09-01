"""Interfaz de usuario interactiva en Streamlit para exploración analítica Text-to-SQL."""

import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from src.database_engine import ProcurementDatabaseManager
from src.text2sql_agent import ProcurementText2SQLAgent

load_dotenv()

st.set_page_config(
    page_title="Procurement Text-to-SQL Engine",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Enterprise Procurement Text-to-SQL Engine")
st.markdown("Consulta en lenguaje natural sobre **50.000 registros OpEx** procesados en tiempo real mediante **DuckDB** y **Gemini SDK**.")

if "db_manager" not in st.session_state:
    with st.spinner("Cargando motor DuckDB in-memory (50.000 filas)..."):
        st.session_state.db_manager = ProcurementDatabaseManager(record_count=50000)

db = st.session_state.db_manager

with st.sidebar:
    st.header("⚙️ Configuración del Sistema")
    api_key_input = st.text_input(
        "Gemini API Key:",
        value=os.getenv("GEMINI_API_KEY", ""),
        type="password"
    )
    
    model_name = st.selectbox(
        "Modelo de LLM:",
        ["gemini-3.6-flash", "gemini-2.5-pro", "gemini-1.5-flash"]
    )
    
    st.divider()
    st.subheader("📐 Esquema de la Base de Datos")
    st.code(db.get_schema_info(), language="sql")

queries_list = [
    "¿Cuáles son las 5 categorías con mayor gasto total en órdenes aprobadas?",
    "¿Cuál es el top 5 de proveedores con mejor rating y su total facturado?",
    "¿Cuántas órdenes hay por estado y cuál es el promedio de gasto por orden?",
    "¿Cuál es el gasto acumulado agrupado por centro de coste en órdenes de IT Hardware?"
]

st.subheader("💡 Consultas de Ejemplo")
selected_template = st.selectbox("Selecciona una pregunta predefinida:", ["-- Personalizada --"] + queries_list)

user_query = st.text_input(
    "Escribe tu pregunta de negocio en español:",
    value="" if selected_template == "-- Personalizada --" else selected_template
)

if st.button("Ejecutar Consulta Analítica", type="primary"):
    if not api_key_input:
        st.error("Por favor proporciona una GEMINI_API_KEY válida.")
    elif not user_query.strip():
        st.warning("Ingresa una pregunta válida.")
    else:
        try:
            with st.spinner("Procesando consulta con Gemini SDK y ejecutando en DuckDB..."):
                agent = ProcurementText2SQLAgent(
                    db_manager=db,
                    api_key=api_key_input,
                    model_name=model_name
                )
                sql_generated, df_result = agent.query_and_analyze(user_query)

            col1, col2 = st.columns([1, 1])

            with col1:
                st.subheader("📄 Consulta SQL Generada")
                st.code(sql_generated, language="sql")

            with col2:
                st.subheader("📊 Resultado Analítico (DuckDB)")
                st.dataframe(df_result, use_container_width=True)

            if not df_result.empty and len(df_result.columns) >= 2:
                st.divider()
                st.subheader("📈 Visualización Dinámica")
                try:
                    chart_df = df_result.copy()
                    if "supplier_name" in chart_df.columns:
                        chart_df = chart_df.set_index("supplier_name")
                    elif "category" in chart_df.columns:
                        chart_df = chart_df.set_index("category")
                    else:
                        chart_df[chart_df.columns[0]] = chart_df[chart_df.columns[0]].astype(str)
                        chart_df = chart_df.set_index(chart_df.columns[0])
                    
                    numeric_cols = chart_df.select_dtypes(include=["number"]).columns
                    if len(numeric_cols) > 0:
                        st.bar_chart(chart_df[numeric_cols[-1]])
                except Exception as chart_err:
                    st.warning(f"No se pudo renderizar el gráfico dinámico: {chart_err}")

        except Exception as err:
            st.error(f"Error en el procesamiento: {str(err)}")