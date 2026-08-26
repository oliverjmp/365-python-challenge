import streamlit as st
import duckdb
import pandas as pd
from src.metrics_decorator import MetricsAnalyzer

st.set_page_config(
    page_title="D207 - Custom Decorator Query Metrics",
    page_icon="⏱️",
    layout="wide"
)

st.title("⏱️ D207 - Telemetría y Métricas SQL con Decoradores Avanzados")
st.markdown("Dashboard interactivo para la medición de latencias y rendimiento analítico mediante decoradores en Python.")

@st.cache_resource
def get_metrics_connection():
    conn = duckdb.connect(database=":memory:")
    conn.execute("""
        CREATE TABLE metrics_data (
            id INTEGER,
            operacion VARCHAR,
            tabla VARCHAR,
            filas_afectadas INTEGER,
            estado VARCHAR
        );
    """)
    conn.execute("""
        INSERT INTO metrics_data VALUES
        (1, 'SELECT', 'transacciones', 150, 'Exitoso'),
        (2, 'INSERT', 'transacciones', 45, 'Exitoso'),
        (3, 'UPDATE', 'logs', 12, 'Exitoso'),
        (4, 'SELECT', 'logs', 500, 'Exitoso');
    """)
    return conn

conn = get_metrics_connection()
analyzer = MetricsAnalyzer(conn)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Agregación Analítica de Operaciones")
    try:
        data_analitica = analyzer.ejecutar_consulta_analitica()
        st.dataframe(pd.DataFrame(data_analitica), use_container_width=True)
    except Exception as e:
        st.error(f"Error: {e}")

with col2:
    st.subheader("🔍 Filtrado por Operación (SELECT)")
    try:
        data_select = analyzer.filtrar_por_operacion("SELECT")
        st.dataframe(pd.DataFrame(data_select), use_container_width=True)
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.success("✅ Estado del Decorador de Telemetría: Monitoreo de latencia y recursos activo.")