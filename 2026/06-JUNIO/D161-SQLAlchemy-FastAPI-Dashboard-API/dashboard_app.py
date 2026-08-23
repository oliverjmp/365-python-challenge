import streamlit as __streamlit
import requests as __requests
import pandas as __pandas

__streamlit.set_page_config(
    page_title="Dashboard Analítico - FastAPI & Streamlit",
    page_icon="📊",
    layout="wide"
)

__streamlit.title("📊 Tablero de Control Analítico (D161)")
__streamlit.markdown("Microservicio backend con FastAPI conectado a una interfaz visual en Streamlit.")

API_URL = "http://127.0.0.1:8000/analytics/"
SUMMARY_URL = "http://127.0.0.1:8000/analytics/summary/"

# --- Barra lateral para insertar datos ---
__streamlit.sidebar.header("Registrar Nueva Métrica")
with __streamlit.sidebar.form("metric_form"):
    metric_name = __streamlit.text_input("Nombre de la Métrica", "Conversión Web")
    category = __streamlit.selectbox("Categoría", ["Digital", "Retail", "Finanzas", "Operaciones"])
    value = __streamlit.number_input("Valor Numérico", value=10.5, step=0.1)
    submit_button = __streamlit.form_submit_button(label="Guardar Métrica")

    if submit_button:
        payload = {"metric_name": metric_name, "category": category, "value": value}
        try:
            response = __requests.post(API_URL, json=payload)
            if response.status_code == 201:
                __streamlit.sidebar.success("¡Métrica registrada con éxito!")
            else:
                __streamlit.sidebar.error("Error al registrar la métrica en el backend.")
        except Exception as e:
            __streamlit.sidebar.error(f"No se pudo conectar con la API: {e}")

# --- Sección Principal: Métricas Resumen ---
__streamlit.subheader("Resumen Ejecutivo")
try:
    summary_resp = __requests.get(SUMMARY_URL)
    if summary_resp.status_code == 200:
        summary_data = summary_resp.json()
        
        col1, col2, col3 = __streamlit.columns(3)
        with col1:
            __streamlit.metric("Total de Registros", summary_data.get("total_records", 0))
        with col2:
            __streamlit.metric("Valor Promedio", summary_data.get("average_value", 0.0))
        with col3:
            __streamlit.metric("Categorías Únicas", len(summary_data.get("categories", [])))
    else:
        __streamlit.warning("Aún no hay datos de resumen disponibles.")
except Exception:
    __streamlit.error("Asegúrate de que el servidor Uvicorn de FastAPI esté ejecutándose en http://127.0.0.1:8000")

__streamlit.markdown("---")

# --- Sección de Datos Detallados ---
__streamlit.subheader("Historial de Registros Analíticos")
try:
    records_resp = __requests.get(API_URL)
    if records_resp.status_code == 200:
        records = records_resp.json()
        if records:
            df = __pandas.DataFrame(records)
            __streamlit.dataframe(df, use_container_width=True)
            
            # Gráfico rápido de valores por categoría
            if "category" in df.columns and "value" in df.columns:
                __streamlit.subheader("Visualización Gráfica por Categoría")
                chart_data = df.groupby("category")["value"].mean()
                __streamlit.bar_chart(chart_data)
        else:
            __streamlit.info("No hay registros en la base de datos todavía. Utiliza el panel izquierdo para añadir algunos.")
except Exception:
    __streamlit.info("Esperando conexión con el backend...")