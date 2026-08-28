import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.tracker import MLflowTracker

st.set_page_config(
    page_title="D231 - MLflow Tracking Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 D231: Panel de Trazabilidad y Experimentos (MLflow + SQLite)")
st.markdown("""
Panel interactivo para registrar hiperparámetros, métricas de modelos de Machine Learning y consultar el historial de ejecuciones.
""")

st.sidebar.header("⚙️ Configuración del Experimento")
exp_name = st.sidebar.text_input("Nombre del Experimento", value="Default-Model-Experiment")
run_name = st.sidebar.text_input("Nombre de la Ejecución (Run)", value="run-v1")

st.sidebar.subheader("🎛️ Hiperparámetros")
learning_rate = st.sidebar.number_input("Learning Rate", value=0.01, format="%.4f")
max_depth = st.sidebar.slider("Max Depth", min_value=1, max_value=10, value=3)

st.sidebar.subheader("📊 Métricas de Rendimiento")
accuracy = st.sidebar.slider("Accuracy", min_value=0.0, max_value=1.0, value=0.92)
rmse = st.sidebar.number_input("RMSE", value=0.15)

if st.button("🚀 Registrar Ejecución en MLflow", type="primary"):
    try:
        tracker = MLflowTracker()
        params = {"learning_rate": learning_rate, "max_depth": max_depth}
        metrics = {"accuracy": accuracy, "rmse": rmse}
        
        result = tracker.log_run(experiment_name=exp_name, run_name=run_name, params=params, metrics=metrics)
        
        st.success(f"¡Ejecución registrada con éxito en MLflow!")
        st.json(result)
    except Exception as e:
        st.error(f"Error al registrar en MLflow: {e}")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Nota técnica")
st.sidebar.text("Para levantar la interfaz web oficial de MLflow:\nEjecuta `mlflow ui` en tu terminal.")