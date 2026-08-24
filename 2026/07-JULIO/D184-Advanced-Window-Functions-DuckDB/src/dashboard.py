import streamlit as st
import plotly.express as px
from window_analytics_engine import AdvancedWindowAnalyticsEngine

st.set_page_config(
    page_title="Executive Analytics Dashboard - D184",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Dashboard Ejecutivo de Crecimiento Financiero (D184)")
st.markdown("Analítica avanzada en tiempo real sobre **DuckDB + Parquet** mediante **Window Functions (MoM & Running Totals)**.")

parquet_path = "data_lake/historico_financiero.parquet"
engine = AdvancedWindowAnalyticsEngine()

# Cargar/Generar datos
engine.generar_dataset_financiero(parquet_path)
resultado = engine.calcular_metricas_financieras(parquet_path)
df = resultado["dataframe_resultados"]

# Filtros laterales
st.sidebar.header("Filtros del Dashboard")
lineas_seleccionadas = st.sidebar.multiselect(
    "Selecciona Líneas de Negocio:",
    options=df["linea_negocio"].unique(),
    default=df["linea_negocio"].unique()
)

df_filtrado = df[df["linea_negocio"].isin(lineas_seleccionadas)]

# Métricas Top Level
kpi1, kpi2, kpi3 = st.columns(3)
total_ingresos = df_filtrado["ingresos_mensuales"].sum()
promedio_mom = df_filtrado["variacion_mom_pct"].mean()

kpi1.metric("Ingresos Totales Registrados", f"${total_ingresos:,.2f}")
kpi2.metric("Promedio de Variación MoM", f"{promedio_mom:.2f}%")
kpi3.metric("Latencia de Consulta SQL", f"{resultado['latencia_ms']} ms")

st.markdown("---")

# Gráficos de Negocio
col1, col2 = st.columns(2)

with col1:
    st.subheader("Evolución de Ingresos Acumulados (Running Total)")
    fig_acumulado = px.line(
        df_filtrado,
        x="mes",
        y="ingresos_acumulados_anio",
        color="linea_negocio",
        facet_col="anio",
        title="Ingresos Acumulados Anuales por Mes"
    )
    st.plotly_chart(fig_acumulado, use_container_width=True)

with col2:
    st.subheader("Variación Mensual MoM (%)")
    fig_mom = px.bar(
        df_filtrado,
        x="mes",
        y="variacion_mom_pct",
        color="linea_negocio",
        barmode="group",
        title="Crecimiento MoM por Mes"
    )
    st.plotly_chart(fig_mom, use_container_width=True)

# Tabla de Datos
st.subheader("Tabla Analítica Consolidada")
st.dataframe(df_filtrado, use_container_width=True)

engine.cerrar_conexion()