import streamlit as st
from src.git_automator import GitMilestoneManager

st.set_page_config(
    page_title="D200 - Mid-Year Architecture Milestone",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Hito de Mitad de Año: Git Automation & Architecture")
st.markdown("Panel de control y etiquetado automatizado para la consolidación del portafolio de ingeniería de datos.")

try:
    manager = GitMilestoneManager()
    estado = manager.obtener_estado_actual()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Rama Activa", estado["branch_activa"])
    with col2:
        st.metric("Último Commit", estado["commit_reciente"])

    st.subheader("📋 Estado del Repositorio")
    st.write(f"**Mensaje del Commit:** `{estado['mensaje_commit']}`")
    st.write(f"**Tags Registrados:** {estado['tags_existentes']}")

    st.divider()

    st.subheader("🏷️ Creación de Tag de Hito (Milestone)")
    tag_name = st.text_input("Nombre del Tag (Ej: v200-midyear-milestone):", value="v200-midyear-milestone")
    tag_message = st.text_area("Mensaje descriptivo del Tag:", value="Consolidación de arquitectura de mitad de año - D200")

    if st.button("🚀 Crear Tag en el Repositorio"):
        try:
            respuesta = manager.crear_tag_hito(tag_name, tag_message)
            st.success(f"¡Éxito! {respuesta}")
        except ValueError as ve:
            st.warning(f"⚠️ {ve}")
        except Exception as e:
            st.error(f"❌ Error inesperado: {e}")

except Exception as e:
    st.error(f"❌ No se pudo inicializar el gestor de Git: {e}")