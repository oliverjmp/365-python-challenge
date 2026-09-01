import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.registry_manager import ModelRegistryManager

st.set_page_config(
    page_title="D233 - MLflow Model Registry Dashboard",
    page_icon="🗃️",
    layout="wide"
)

st.title("🗃️ D233: Gestión del Model Registry (MLflow)")
st.markdown("""
Panel interactivo para registrar modelos de Machine Learning, versionarlos y gestionar sus etapas operativas en el ciclo de vida (*Staging*, *Production*).
""")

manager = ModelRegistryManager()

st.sidebar.header("⚙️ Operaciones del Registry")
model_name = st.sidebar.text_input("Nombre del Modelo Registrado", value="EnterprisePredictor")

if st.sidebar.button("🚀 Entrenar y Registrar Nueva Versión", type="primary"):
    try:
        result = manager.train_and_register_model(model_name=model_name)
        st.success(f"¡Modelo registrado con éxito! Versión creada: {result['version']}")
        st.json(result)
    except Exception as e:
        st.error(f"Error al registrar el modelo: {e}")

st.markdown("---")
st.subheader("🔄 Transición de Etapas (Lifecycle Stage)")

col1, col2, col3 = st.columns(3)
target_version = col1.text_input("Versión del Modelo", value="1")
target_stage = col2.selectbox("Nueva Etapa", ["Staging", "Production", "Archived"])

if col3.button("Actualizar Etapa del Modelo"):
    try:
        transition_result = manager.transition_model_stage(
            model_name=model_name,
            version=target_version,
            stage=target_stage
        )
        st.success(f"¡Modelo actualizado a etapa **{target_stage}** con éxito!")
        st.json(transition_result)
    except Exception as e:
        st.error(f"Error al transicionar etapa: {e}")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Nota técnica")
st.sidebar.text("Ejecuta `mlflow ui` en tu terminal\npara visualizar el repositorio completo.")