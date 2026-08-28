import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.pipeline_trainer import ModelPipelineTrainer

st.set_page_config(
    page_title="D232 - Scikit-Learn & MLflow Pipeline",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 D232: Pipeline Automatizado de ML (Scikit-Learn + MLflow)")
st.markdown("""
Panel interactivo para configurar hiperparámetros, ejecutar el entrenamiento de modelos de clasificación y registrar artefactos y métricas en tiempo real.
""")

st.sidebar.header("⚙️ Configuración del Pipeline")
exp_name = st.sidebar.text_input("Nombre del Experimento", value="Sklearn-Classification-Experiment")
n_estimators = st.sidebar.slider("N Estimators (Random Forest)", min_value=10, max_value=300, value=100, step=10)
max_depth = st.sidebar.slider("Max Depth", min_value=1, max_value=20, value=5)

if st.button("🚀 Ejecutar Entrenamiento y Registrar en MLflow", type="primary"):
    with st.spinner("Entrenando modelo y registrando artefactos..."):
        try:
            trainer = ModelPipelineTrainer()
            result = trainer.train_and_log(
                experiment_name=exp_name,
                n_estimators=n_estimators,
                max_depth=max_depth
            )
            
            st.success("¡Pipeline ejecutado y registrado con éxito en MLflow!")
            
            col1, col2 = st.columns(2)
            col1.metric("Accuracy", f"{result['metrics']['accuracy']:.4f}")
            col2.metric("Precision", f"{result['metrics']['precision']:.4f}")
            
            st.subheader("📦 Detalles de la Ejecución (Run)")
            st.json(result)
        except Exception as e:
            st.error(f"Error durante la ejecución del pipeline: {e}")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Nota técnica")
st.sidebar.text("Para explorar visualmente los modelos guardados:\nEjecuta `mlflow ui` en tu terminal.")