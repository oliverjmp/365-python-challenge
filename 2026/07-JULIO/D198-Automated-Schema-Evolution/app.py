import streamlit as st
import pandas as pd
import os
from src.schema_evolution import SchemaEvolutionManager

st.set_page_config(
    page_title="D198 - PyArrow Schema Evolution Dashboard",
    page_icon="📊",
    layout="wide"
)

manager = SchemaEvolutionManager()

st.title("📊 Pipeline de Evolución Automática de Esquemas")
st.markdown("Demostración interactiva de cómo **PyArrow Datasets** unifica dinámicamente archivos Parquet con esquemas dispares.")

st.sidebar.header("⚙️ Control de Datos")
if st.sidebar.button("🔄 Generar / Reiniciar Lotes de Prueba"):
    manager.guardar_lote_inicial()
    manager.guardar_lote_evolucionado()
    st.sidebar.success("¡Lotes V1 y V2 generados con éxito!")

try:
    tabla_unificada = manager.leer_dataset_unificado()
    df = tabla_unificada.to_pandas()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Registros", df.shape[0])
    with col2:
        st.metric("Total de Columnas", df.shape[1])
    with col3:
        st.metric("Archivos en Dataset", len(os.listdir(manager.dataset_dir)) if os.path.exists(manager.dataset_dir) else 0)

    st.divider()

    st.subheader("🛠️ Auditoría de Esquema PyArrow")
    schema_info = [{"Columna": field.name, "Tipo de Dato": str(field.type)} for field in tabla_unificada.schema]
    st.table(pd.DataFrame(schema_info))

    st.divider()

    st.subheader("📋 Datos Tabulares Consolidados")
    segmento_filtro = st.selectbox("Filtrar por Segmento", ["Todos"] + list(df["segmento"].dropna().unique()))
    
    if segmento_filtro != "Todos":
        df_filtrado = df[df["segmento"] == segmento_filtro]
    else:
        df_filtrado = df

    st.dataframe(df_filtrado, use_container_width=True)

except FileNotFoundError:
    st.warning("⚠️ No se encontraron datos en el Data Lake. Haz clic en el botón **'Generar / Reiniciar Lotes de Prueba'** en la barra lateral.")