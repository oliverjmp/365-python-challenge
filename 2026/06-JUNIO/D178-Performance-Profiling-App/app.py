import streamlit as st
from src.profiler_engine import simulate_heavy_computation, profile_function

st.set_page_config(
    page_title="D178 - Performance Profiling App",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Diagnóstico de Rendimiento con cProfile (D178)")
st.markdown("Herramienta analítica para medir tiempos de respuesta y detectar cuellos de botella en la interfaz.")

st.sidebar.header("Parámetros de Prueba")
delay_time = st.sidebar.slider("Simular retardo de procesamiento (s):", 0.1, 2.0, 0.5)

if st.button("Ejecutar Diagnóstico de Rendimiento"):
    with st.spinner("Ejecutando perfilado de código con cProfile..."):
        df_result, profile_report = profile_function(simulate_heavy_computation, delay=delay_time)
        
    st.success("¡Perfilado completado con éxito!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Datos Procesados")
        st.dataframe(df_result.head(10), use_container_width=True)
        
    with col2:
        st.subheader("🔍 Reporte de cProfile")
        st.text(profile_report)