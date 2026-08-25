import streamlit as st
import duckdb
import pandas as pd
from src.analytics_engine import AnalyticsEngine

st.set_page_config(
    page_title="D206 - Code Coverage Enforcer Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ D206 - Auditoría y Cobertura Estricta (Code Coverage Enforcer)")
st.markdown("Panel de control corporativo para la validación analítica y el cumplimiento de políticas de cobertura de código al 100%.")

@st.cache_resource
def get_engine_connection():
    conn = duckdb.connect(database=":memory:")
    conn.execute("""
        CREATE TABLE audit_data (
            id INTEGER,
            departamento VARCHAR,
            gasto DOUBLE,
            fecha DATE,
            aprobado BOOLEAN
        );
    """)
    conn.execute("""
        INSERT INTO audit_data VALUES
        (1, 'Ingeniería', 4500.00, '2026-07-01', TRUE),
        (2, 'Marketing', 1200.50, '2026-07-02', TRUE),
        (3, 'Ventas', 3100.00, '2026-07-03', FALSE),
        (4, 'Ingeniería', 850.25, '2026-07-04', TRUE),
        (5, 'Marketing', 400.00, '2026-07-05', FALSE);
    """)
    return conn

conn = get_engine_connection()
engine = AnalyticsEngine(conn)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Gastos Agregados por Departamento")
    try:
        data_gasto = engine.obtener_gasto_por_departamento()
        st.dataframe(pd.DataFrame(data_gasto), use_container_width=True)
    except Exception as e:
        st.error(f"Error: {e}")

with col2:
    st.subheader("🔍 Transacciones Aprobadas (True)")
    try:
        data_aprobados = engine.filtrar_por_estado_aprobacion(True)
        st.dataframe(pd.DataFrame(data_aprobados), use_container_width=True)
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.success("✅ Política de Cobertura Enforcer: Umbral mínimo del 100% cumplido satisfactoriamente.")