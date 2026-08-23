import streamlit as st
from src.components import render_kpi_card, format_currency_metric

st.set_page_config(
    page_title="D164 - KPI Component Library",
    page_icon="📊",
    layout="wide"
)

st.title("📊 D164: Biblioteca de Componentes KPI para Streamlit")
st.markdown("Visualización ejecutiva mediante tarjetas de métricas reutilizables y modulares.")

# Panel superior con componentes KPI personalizados
col1, col2, col3 = st.columns(3)

with col1:
    formatted_rev = format_currency_metric(125430.50)
    render_kpi_card("Ingresos Totales", formatted_rev, delta="+12.4%", delta_color="inverse")

with col2:
    render_kpi_card("Usuarios Activos", "8,432", delta="+5.1%")

with col3:
    render_kpi_card("Tasa de Conversión", "3.45%", delta="-0.8%")

st.markdown("---")
st.success("✨ Componentes cargados exitosamente desde la biblioteca modular `src/components.py`.")