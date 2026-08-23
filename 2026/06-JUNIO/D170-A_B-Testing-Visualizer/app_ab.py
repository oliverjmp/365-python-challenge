import streamlit as st
import plotly.graph_objects as go
from src.stats_analyzer import calculate_ab_test

st.set_page_config(
    page_title="D170 - A/B Testing Visualizer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Dashboard Analítico de Pruebas A/B (D170)")
st.markdown("Evalúa la significancia estadística y el impacto de tus variantes de diseño o producto.")

st.sidebar.header("⚙️ Parámetros de la Prueba")
st.sidebar.subheader("Grupo A (Control)")
visitors_a = st.sidebar.number_input("Visitantes A", min_value=10, value=1000, step=100)
conversions_a = st.sidebar.number_input("Conversiones A", min_value=0, value=120, step=10)

st.sidebar.subheader("Grupo B (Variante)")
visitors_b = st.sidebar.number_input("Visitantes B", min_value=10, value=1000, step=100)
conversions_b = st.sidebar.number_input("Conversiones B", min_value=0, value=150, step=10)

# Procesar resultados
results = calculate_ab_test(visitors_a, conversions_a, visitors_b, conversions_b)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tasa Grupo A", f"{results['rate_a']:.2%}")
with col2:
    st.metric("Tasa Grupo B", f"{results['rate_b']:.2%}", delta=f"{results['lift']:.2f}%")
with col3:
    st.metric("Valor p (p-value)", f"{results['p_value']:.4f}", 
              delta="Significativo" if results['significant'] else "No Significativo",
              delta_color="normal" if results['significant'] else "off")

st.markdown("---")
st.subheader("📊 Comparativa Visual de Tasas de Conversión")

fig = go.Figure(data=[
    go.Bar(name='Control (A)', x=['Grupo A'], y=[results['rate_a'] * 100], marker_color='#636efa'),
    go.Bar(name='Variante (B)', x=['Grupo B'], y=[results['rate_b'] * 100], marker_color='#ef553b')
])
fig.update_layout(yaxis_title="Tasa de Conversión (%)", barmode='group', template='plotly_white')
st.plotly_chart(fig, use_container_width=True)