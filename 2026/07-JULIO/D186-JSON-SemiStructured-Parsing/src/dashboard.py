import streamlit as st
import plotly.express as px
from json_parsing_engine import JSONSemiStructuredEngine

st.set_page_config(
    page_title="JSON SemiStructured Parsing Dashboard - D186",
    page_icon="🧩",
    layout="wide"
)

st.title("🧩 Dashboard Analítico de Datos Semi-estructurados (D186)")
st.markdown("Extracción, aplanamiento y analítica de cargas útiles **JSON anidadas** mediante **DuckDB JSON Functions** sobre almacenamiento Parquet.")

parquet_path = "data_lake/eventos_semi_estructurados.parquet"
engine = JSONSemiStructuredEngine()

engine.generar_dataset_json(parquet_path)
resultado = engine.consultar_datos_json(parquet_path)
df = resultado["dataframe_resultados"]

# Métricas Top Level
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total de Agrupaciones Analizadas", f"{len(df):,}")
kpi2.metric("Latencia de Extracción JSON (SQL)", f"{resultado['latencia_ms']} ms")
kpi3.metric("Motor Analítico", "DuckDB In-Process")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Ocurrencias por Tipo de Evento y Plataforma")
    fig_eventos = px.bar(
        df,
        x="tipo_evento",
        y="total_ocurrencias",
        color="plataforma",
        barmode="group",
        title="Volumen de Eventos por Dispositivo"
    )
    st.plotly_chart(fig_eventos, use_container_width=True)

with col2:
    st.subheader("Latencia Promedio de Red (ms) por Evento")
    fig_latencia = px.box(
        df,
        x="tipo_evento",
        y="latencia_promedio_ms",
        color="plataforma",
        title="Distribución de Latencias"
    )
    st.plotly_chart(fig_latencia, use_container_width=True)

st.subheader("Tabla Analítica de Datos Extraídos del JSON")
st.dataframe(df, use_container_width=True)

engine.cerrar_conexion()