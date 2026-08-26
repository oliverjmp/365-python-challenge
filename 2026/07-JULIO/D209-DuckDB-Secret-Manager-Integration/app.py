import streamlit as st
import os
from src.secret_manager import SecretManager

st.set_page_config(page_title="D209 - DuckDB Secret Manager", layout="wide")

st.title("🔐 D209: Panel de Control y Auditoría de Secret Manager")
st.markdown("Gestión segura de credenciales, variables de entorno y rutas de almacenamiento remoto para el Data Lake analítico.")

with st.sidebar:
    st.header("⚙️ Configuración de Entorno")
    env_user = st.text_input("DUCKDB_USER", value=os.getenv("DUCKDB_USER", "admin_analitica"))
    env_bucket = st.text_input("DUCKDB_STORAGE_BUCKET", value=os.getenv("DUCKDB_STORAGE_BUCKET", "s3://enterprise-data-lake-raw"))
    
    if st.button("Aplicar Variables de Entorno"):
        os.environ["DUCKDB_USER"] = env_user
        os.environ["DUCKDB_STORAGE_BUCKET"] = env_bucket
        st.success("¡Variables actualizadas en runtime!")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Estado de Credenciales Actuales")
    try:
        manager = SecretManager()
        credenciales = manager.validar_credenciales()
        st.json(credenciales)
        st.success("Estado del Sistema: SEGURO Y OPERATIVO")
    except Exception as e:
        st.error(f"Error de Configuración Detectado: {e}")

with col2:
    st.subheader("🔑 Generador Criptográfico de Tokens")
    if st.button("Generar Token Temporal de Sesión"):
        manager = SecretManager()
        token = manager.generar_token_seguro()
        st.code(token, language="text")
        st.info("Token generado de forma segura mediante criptografía estándar (`secrets`).")