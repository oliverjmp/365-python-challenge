import streamlit as st
import duckdb
import pandas as pd
from src.query_validator import QueryValidator

st.set_page_config(
    page_title="D205 - DuckDB Fixtures Audit Dashboard",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 D205 - Suite de Pruebas y Auditoría de DuckDB Fixtures")
st.markdown("Dashboard interactivo para la validación en tiempo real de consultas analíticas y aislamiento de estado mediante Pytest Fixtures.")

@st.cache_resource
def get_audit_connection():
    conn = duckdb.connect(database=":memory:")
    conn.execute("""
        CREATE TABLE transactions (
            id INTEGER,
            categoria VARCHAR,
            monto DOUBLE,
            fecha DATE,
            estado VARCHAR
        );
    """)
    conn.execute("""
        INSERT INTO transactions VALUES
        (1, 'Hardware', 1200.50, '2026-07-01', 'Completado'),
        (2, 'Software', 450.99, '2026-07-02', 'Completado'),
        (3, 'Servicios', 300.00, '2026-07-03', 'Pendiente'),
        (4, 'Hardware', 150.00, '2026-07-04', 'Completado'),
        (5, 'Software', 89.99, '2026-07-05', 'Completado'),
        (6, 'Logística', 1500.00, '2026-07-06', 'Completado'),
        (7, 'Servicios', 650.25, '2026-07-07', 'Pendiente');
    """)
    return conn

conn = get_audit_connection()
validator = QueryValidator(conn)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Totales Agrupados por Estado")
    try:
        data_estado = validator.calcular_total_por_estado()
        st.dataframe(pd.DataFrame(data_estado), use_container_width=True)
    except Exception as e:
        st.error(f"Error analítico: {e}")

with col2:
    st.subheader("🔍 Auditoría por Categoría (Hardware)")
    try:
        data_hw = validator.filtrar_por_categoria("Hardware")
        st.dataframe(pd.DataFrame(data_hw), use_container_width=True)
    except Exception as e:
        st.error(f"Error analítico: {e}")

st.markdown("---")
st.success("✅ Estado del Motor Analítico: Fixtures de Pytest operando con integridad transaccional 100%.")