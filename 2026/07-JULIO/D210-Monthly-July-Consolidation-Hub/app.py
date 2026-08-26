import streamlit as st
import duckdb
from src.consolidation_hub import JulyConsolidationHub

st.set_page_config(page_title="D210 - Monthly July Consolidation Hub", layout="wide")

st.title("🌟 D210: Hub de Consolidación Mensual (Bloque Julio)")
st.markdown("Portal ejecutivo centralizado para la auditoría estructural, cumplimiento de cobertura y limpieza de deuda técnica del mes.")

# Conexión DuckDB in-memory para el dashboard
conn = duckdb.connect(database=":memory:")
hub = JulyConsolidationHub(conn)

kpis = hub.calcular_kpis_globales()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Hitos Desarrollados", kpis["total_hitos_completados"])
with col2:
    st.metric("Cobertura Global Promedio", f"{kpis['cobertura_promedio_global']}%")
with col3:
    st.metric("Hitos Óptimos", kpis["hitos_en_estado_optimo"])
with col4:
    st.metric("Deuda Técnica", f"{kpis['deuda_tecnica_pendiente']}%")

st.divider()

st.subheader("📊 Reporte Consolidado de Hitos del Mes de Julio")
df_reporte = hub.generar_reporte_consolidado_julio()
st.dataframe(df_reporte, use_container_width=True)

st.success("¡Bloque de Julio consolidado exitosamente bajo estándares estrictos de ingeniería de datos!")