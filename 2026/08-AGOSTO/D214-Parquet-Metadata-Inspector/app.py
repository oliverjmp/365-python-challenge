import streamlit as st
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import tempfile
import os
from src.parquet_inspector import ParquetMetadataInspector

st.set_page_config(page_title="D214 - Parquet Metadata Inspector", layout="wide")

st.title("🔍 D214: Inspector de Metadatos de Ficheros Parquet")
st.markdown("Inspección programática de esquemas, metadatos y estadísticas internas usando PyArrow.")

# Generar archivo de demostración por defecto de forma segura
default_df = pd.DataFrame({
    "transaccion_id": [101, 102, 103, 104],
    "cliente": ["Empresa A", "Empresa B", "Empresa C", "Empresa D"],
    "monto": [1500.50, 3200.00, 450.25, 8900.00],
    "completado": [True, True, False, True]
})

# Creamos un archivo temporal asegurando que el descriptor de Windows se cierre bien
with tempfile.NamedTemporaryFile(delete=False, suffix=".parquet") as tmp:
    tmp_path = tmp.name

pq.write_table(pa.Table.from_pandas(default_df), tmp_path)

# Instanciamos el inspector
inspector = ParquetMetadataInspector(tmp_path)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Esquema de Columnas")
    schema_df = pd.DataFrame(inspector.get_schema_info())
    st.dataframe(schema_df, width="stretch")

with col2:
    st.subheader("📊 Metadatos Generales del Archivo")
    meta_dict = inspector.get_file_metadata()
    st.json(meta_dict)

st.subheader("📦 Estadísticas por Grupo de Filas (Row Groups)")
stats_df = pd.DataFrame(inspector.get_row_group_statistics())
st.dataframe(stats_df, width="stretch")

# Eliminamos la llamada directa a os.unlink() al final del script principal 
# para prevenir el conflicto de bloqueo de procesos en Windows. El sistema operativo 
# se encargará de limpiar el archivo temporal del directorio temp oportunamente.