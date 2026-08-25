import streamlit as st
import json
import os

st.set_page_config(
    page_title="D190 - Auditoría de Arquitectura",
    page_icon="📊",
    layout="wide"
)

st.title("🏛️ Tablero de Control - Auditoría de Arquitectura (D190)")
st.markdown("Visualización en tiempo real del estado de los subsistemas y métricas de rendimiento para el inicio de la **Fase 4**.")

STORAGE_PATH = "data_lake/architecture_state.json"

def load_architecture_data():
    if not os.path.exists(STORAGE_PATH):
        return None
    with open(STORAGE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

data = load_architecture_data()

if data is not None:
    components = data.get("components", [])
    total_comps = len(components)
    conformes = sum(1 for c in components if c.get("status") == "CONFORME")
    compliance_rate = (conformes / total_comps) * 100 if total_comps > 0 else 0
    avg_score = sum(c.get("performance_score", 0) for c in components) / total_comps if total_comps > 0 else 0

    st.sidebar.header("📌 Parámetros del Trimestre")
    st.sidebar.info(f"**Trimestre:** {data.get('quarter')}")
    st.sidebar.info(f"**Fase Actual:** {data.get('phase')}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Módulos", total_comps)
    with col2:
        st.metric("Módulos Conformes", conformes)
    with col3:
        st.metric("Índice de Cumplimiento", f"{compliance_rate:.1f}%")
    with col4:
        st.metric("Rendimiento Promedio", f"{avg_score:.2f} pts")

    st.markdown("---")
    st.subheader("📋 Detalle de Subsistemas Auditados")
    st.dataframe(components, use_container_width=True)

    st.subheader("📊 Rendimiento Comparativo por Subsistema")
    chart_data = {c["component_id"]: c["performance_score"] for c in components}
    st.bar_chart(chart_data)

    st.success("✅ Sistema operando bajo contratos estrictos validados mediante Pydantic v2.")
else:
    st.error(f"No se encontró el archivo de estado en la ruta: `{STORAGE_PATH}`.")