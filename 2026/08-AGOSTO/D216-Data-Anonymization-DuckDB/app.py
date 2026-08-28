import streamlit as st
import pandas as pd
import tempfile
import os
from src.anonymizer import DuckDBAnonymizer

st.set_page_config(page_title="D216 - DuckDB PII Anonymizer", layout="wide")

st.title("🔒 D216: Pipeline de Enmascaramiento y Anonimización de PII con DuckDB")
st.markdown("Herramienta interactiva para auditar y anonimizar datos sensibles de clientes mediante consultas SQL in-memory.")

# Sección lateral para carga de ficheros o datos de demostración
st.sidebar.header("📁 Origen de Datos")
uploaded_file = st.sidebar.file_uploader("Sube tu fichero fuente (CSV o Parquet)", type=["csv", "parquet"])

@st.cache_data
def load_default_data():
    return pd.DataFrame({
        "id": [101, 102, 103, 104, 105],
        "nombre": ["Carlos Pérez", "Ana Gómez", "Luis Martínez", "Sofía Ruiz", "Pedro Alonso"],
        "tarjeta_credito": ["4532-1111-2222-3333", "5412-7777-8888-9999", "3782-4444-5555-6666", "4000-1234-5678-9010", "4111-2222-3333-4444"],
        "email": ["carlos.perez@empresa.com", "ana.gomez@empresa.com", "luis.m@corp.net", "sofia.ruiz@test.org", "pedro.a@domain.es"],
        "pais": ["España", "México", "Argentina", "Colombia", "Chile"],
        "monto": [150.50, 300.00, 1250.75, 89.90, 450.00]
    })

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df_source = pd.read_csv(uploaded_file)
    else:
        df_source = pd.read_parquet(uploaded_file)
    st.sidebar.success(f"Fichero '{uploaded_file.name}' cargado exitosamente.")
else:
    st.sidebar.info("Usando dataset de demostración simulado (puedes subir tu propio CSV o Parquet).")
    df_source = load_default_data()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Datos Originales (Con PII Expuesta)")
    st.dataframe(df_source, width="stretch")

# Procesamiento con DuckDB
anonymizer = DuckDBAnonymizer()
anonymizer.load_dataframe_as_table(df_source, "source_table")
df_anonymized = anonymizer.anonymize_pii("source_table")
anonymizer.close()

with col2:
    st.subheader("🛡️ Datos Anonimizados (SQL Pipeline)")
    st.dataframe(df_anonymized, width="stretch")

# Botón de exportación del resultado anonimizado
st.markdown("---")
st.subheader("📥 Exportar Dataset Anonimizado")

export_format = st.radio("Selecciona formato de salida:", ["CSV", "Parquet"], horizontal=True)

if export_format == "CSV":
    csv_data = df_anonymized.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar CSV Anonimizado",
        data=csv_data,
        file_name="clientes_anonimizados.csv",
        mime="text/csv"
    )
else:
    tmp_parquet = tempfile.NamedTemporaryFile(delete=False, suffix=".parquet")
    df_anonymized.to_parquet(tmp_parquet.name, index=False)
    with open(tmp_parquet.name, "rb") as f:
        parquet_bytes = f.read()
    os.unlink(tmp_parquet.name)
    
    st.download_button(
        label="Descargar Parquet Anonimizado",
        data=parquet_bytes,
        file_name="clientes_anonimizados.parquet",
        mime="application/octet-stream"
    )