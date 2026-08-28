import streamlit as st
import pandas as pd
from src.facade import AnalyticsCoreFacade

st.set_page_config(page_title="D219 - Analytics Core Facade", layout="wide")

st.title("🏛️ D219: Refactorización de Core Analítico (Patrón Fachada)")
st.markdown("Monitorización en tiempo real del pipeline analítico desacoplado mediante la **Fachada**.")

st.sidebar.header("⚙️ Configuración del Dataset")
num_filas = st.sidebar.slider("Número de filas simuladas", 1000, 50000, 10000, step=1000)

if st.button("🚀 Ejecutar Pipeline a través de la Fachada"):
    facade = AnalyticsCoreFacade()
    
    df_input = pd.DataFrame({
        "id": range(1, num_filas + 1),
        "metrica_valor": [float(i) * 1.25 for i in range(1, num_filas + 1)]
    })
    
    with st.spinner("Procesando a través de los subsistemas internos..."):
        resultado = facade.execute_pipeline(df_input)
        
    st.success("¡Pipeline ejecutado exitosamente de manera transparente!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Métricas Analíticas")
        st.json(resultado["analytical_metrics"])
        
    with col2:
        st.subheader("🧠 Estado de Memoria Arrow")
        st.json(resultado["final_memory"])