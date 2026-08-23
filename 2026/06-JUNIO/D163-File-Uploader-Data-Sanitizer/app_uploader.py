import streamlit as st
import pandas as pd
from src.sanitizer import sanitize_and_validate_dataframe

st.set_page_config(
    page_title="D163 - File Uploader & Sanitizer",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ D163: Validador y Sanitizador de Ficheros en Caliente")
st.markdown("Sube un archivo CSV con columnas `id`, `name`, `score` y `active` para validar su esquema mediante Pydantic.")

uploaded_file = st.file_uploader("Selecciona un fichero CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df_raw = pd.read_csv(uploaded_file, sep=";", encoding="utf-8")
        st.subheader("📊 Datos Originales Cargados")
        st.dataframe(df_raw, use_container_width=True)

        if st.button("🚀 Ejecutar Validación Estricta"):
            df_valid, errors = sanitize_and_validate_dataframe(df_raw)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Registros Válidos", len(df_valid))
            with col2:
                st.metric("Errores Encontrados", len(errors))

            if not df_valid.empty:
                st.subheader("✅ Registros Sanitizados y Válidos")
                st.dataframe(df_valid, use_container_width=True)

            if errors:
                st.subheader("❌ Reporte de Errores de Validación")
                df_errors = pd.DataFrame(errors)
                st.dataframe(df_errors, use_container_width=True)

    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")