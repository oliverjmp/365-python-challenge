import streamlit as st
import plotly.express as px
from arrow_bridge_engine import PandasDuckDBBridgeEngine

st.set_page_config(
    page_title="Pandas DuckDB Bridge Dashboard - D185",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Dashboard de Intercambio Vectorial Zero-Copy (D185)")
st.markdown("Integración de alto rendimiento entre **Pandas, Apache Arrow y DuckDB** para analítica corporativa instantánea.")

engine = PandasDuckDBBridgeEngine()

# Carga de datos vectoriales
table_arrow = engine.generar_dataset_vectorial(150000)
resultado = engine.ejecutar_analitica_bridge(table_arrow)
df = resultado["dataframe_resultados"]

# Métricas Top Level
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Registros Procesados (Arrow)", "150,000")
kpi2.metric("Latencia de Consulta Zero-Copy", f"{resultado['latencia_ms']} ms")
kpi3.metric("Motor de Intercambio", "Apache Arrow Bridge")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Monto Total por Departamento y País")
    fig_monto = px.bar(
        df,
        x="departamento",
        y="monto_total",
        color="pais",
        barmode="group",
        title="Ingresos Completados por Departamento"
    )
    st.plotly_chart(fig_monto, use_container_width=True)

with col2:
    st.subheader("Promedio de Transacción por Área")
    fig_avg = px.box(
        df,
        x="departamento",
        y="monto_promedio",
        color="pais",
        title="Distribución de Tickets Promedio"
    )
    st.plotly_chart(fig_avg, use_container_width=True)

st.subheader("Tabla Analítica Consolidada (Zero-Copy Dataframe)")
st.dataframe(df, use_container_width=True)

engine.cerrar_conexion()