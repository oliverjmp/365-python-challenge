import streamlit as st
import pandas as pd
from src.benchmark_runner import BenchmarkRunner

st.set_page_config(
    page_title="D202 - Performance Benchmark Engine",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Benchmark de Rendimiento: Pandas vs DuckDB")
st.markdown("Comparativa de velocidad en operaciones analíticas de agregación con volúmenes de datos escalables.")

num_filas = st.slider("Selecciona el número de registros para el test:", min_value=10_000, max_value=1_000_000, step=50_000, value=100_000)

if st.button("🚀 Ejecutar Benchmark"):
    with st.spinner("Ejecutando pruebas de rendimiento..."):
        runner = BenchmarkRunner(num_filas=num_filas)
        res = runner.ejecutar_comparativa()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Pandas (Tiempo)", f"{res['pandas_segundos']:.4f} s")
        with col2:
            st.metric("DuckDB (Tiempo)", f"{res['duckdb_segundos']:.4f} s")
        with col3:
            st.metric("Aceleración", f"{res['mejora_x']}x")
            
        chart_data = pd.DataFrame({
            "Motor": ["Pandas", "DuckDB"],
            "Segundos": [res["pandas_segundos"], res["duckdb_segundos"]]
        })
        
        st.subheader("📊 Gráfica Comparativa de Tiempos (Menor es mejor)")
        st.bar_chart(chart_data.set_index("Motor"))