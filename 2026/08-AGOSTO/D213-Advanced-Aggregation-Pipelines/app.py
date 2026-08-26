import streamlit as st
import pandas as pd
from src.aggregation_manager import AdvancedAggregationManager

st.set_page_config(page_title="D213 - Advanced Aggregation Pipelines", layout="wide")

st.title("⚡ D213: Panel de Agregaciones Multidimensionales (CUBE / ROLLUP)")
st.markdown("Ejecución de consultas analíticas avanzadas en una sola pasada utilizando DuckDB.")

df_demo = pd.DataFrame({
    "region": ["Norte", "Norte", "Sur", "Sur", "Este", "Este"],
    "canal": "Online",
    "categoria": ["A", "B", "A", "B", "A", "B"],
    "monto": [500.0, 300.0, 700.0, 200.0, 400.0, 600.0]
})

st.subheader("📊 Dataset Base Analítico")
st.dataframe(df_demo, width="stretch")

manager = AdvancedAggregationManager(":memory:")
manager.load_dataset("ventas_demo", df_demo)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Resultado ROLLUP (Jerárquico)")
    df_rollup = manager.execute_rollup("ventas_demo", "region", "categoria", "monto")
    st.dataframe(df_rollup, width="stretch")

with col2:
    st.subheader("🧊 Resultado CUBE (Multidimensional)")
    df_cube = manager.execute_cube("ventas_demo", "region", "categoria", "monto")
    st.dataframe(df_cube, width="stretch")

manager.close()