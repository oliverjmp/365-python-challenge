import streamlit as st
import pandas as pd
from src.analytics_engine import DuckDBAnalyticsEngine

st.set_page_config(
    page_title="D195 - Streamlit DuckDB Analytics App",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Tablero Analítico de Alto Rendimiento (D195)")
st.markdown("Visualización de métricas de negocio en tiempo real impulsada por **DuckDB** y **Streamlit**.")

engine = DuckDBAnalyticsEngine()
metricas = engine.obtener_metricas_globales()

# Panel de Métricas Globales
st.sidebar.header("🎛️ Filtros de Control")
st.sidebar.success("Motor DuckDB Conectado al Data Lake.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Transacciones Totales", metricas["total_transacciones"])
with col2:
    st.metric("Ventas Totales ($)", f"${metricas['monto_total']:,.2f}")
with col3:
    st.metric("Ticket Promedio ($)", f"${metricas['ticket_promedio']:,.2f}")

st.markdown("---")
st.subheader("📈 Resumen de Ventas por Categoría (Motor DuckDB)")

df_resumen = engine.ejecutar_consulta_resumen()
st.dataframe(df_resumen, use_container_width=True)

st.bar_chart(df_resumen.set_index("categoria")["ventas_totales"])

st.markdown("---")
st.info("💡 Este tablero demuestra la capacidad de DuckDB para realizar agregaciones analíticas instantáneas directamente sobre el Data Lake corporativo.")