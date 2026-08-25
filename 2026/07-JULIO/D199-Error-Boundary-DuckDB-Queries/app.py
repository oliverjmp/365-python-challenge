import streamlit as st
import pandas as pd
from src.query_runner import DuckDBQueryRunner
from src.exceptions import SQLSyntaxError, QueryExecutionError

st.set_page_config(
    page_title="D199 - Error Boundary DuckDB",
    page_icon="🛡️",
    layout="wide"
)

runner = DuckDBQueryRunner()

st.title("🛡️ Sistema Centralizado de Captura de Errores (Error Boundary)")
st.markdown("Laboratorio interactivo para probar consultas SQL y validar la captura robusta mediante **Excepciones Personalizadas**.")

# Inicializar tabla de prueba por defecto
try:
    runner.ejecutar_query("CREATE TABLE IF NOT EXISTS datos_prueba (id INT, categoria VARCHAR, valor FLOAT);")
    runner.ejecutar_query("INSERT INTO datos_prueba VALUES (1, 'A', 150.5), (2, 'B', 230.0);")
except Exception:
    pass

st.subheader("✍️ Editor de Consultas SQL")
query_input = st.text_area("Introduce tu consulta SQL:", value="SELECT * FROM datos_prueba;")

if st.button("🚀 Ejecutar Consulta"):
    try:
        resultado = runner.ejecutar_query(query_input)
        st.success("¡Consulta ejecutada exitosamente!")
        st.dataframe(resultado, use_container_width=True)
    except SQLSyntaxError as e:
        st.error(f"❌ **Excepción de Sintaxis Capturada:**\n\n`{e}`")
    except QueryExecutionError as e:
        st.warning(f"⚠️ **Excepción de Ejecución Capturada:**\n\n`{e}`")
    except Exception as e:
        st.error(f"❌ Error Inesperado: {e}")