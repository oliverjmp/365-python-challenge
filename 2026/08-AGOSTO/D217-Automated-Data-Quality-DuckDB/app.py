import streamlit as st
import pandas as pd
from src.data_validator import DataQualityEngine

st.set_page_config(page_title="D217 - Data Quality Dashboard", layout="wide")

st.title("🛡️ D217: Dashboard de Calidad de Datos y Restricciones SQL (DuckDB)")
st.markdown("Auditoría en tiempo real de integridad referencial, restricciones de dominio y aserciones analíticas.")

uploaded_file = st.sidebar.file_uploader("Cargar dataset de transacciones (CSV o Parquet)", type=["csv", "parquet"])

@st.cache_data
def get_default_dataset():
    return pd.DataFrame({
        "transaction_id": [1001, 1002, 1003, 1004],
        "customer_id": [201, 202, 203, 204],
        "amount": [450.00, 1250.50, 300.00, 7500.25],
        "status": ["COMPLETED", "PENDING", "COMPLETED", "FAILED"],
        "event_date": ["2026-08-25", "2026-08-26", "2026-08-27", "2026-08-28"]
    })

if uploaded_file is not None:
    df_input = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_parquet(uploaded_file)
else:
    df_input = get_default_dataset()

st.subheader("📋 Dataset de Entrada")
st.dataframe(df_input, width="stretch")

st.subheader("🔍 Resultados de Aserciones y Calidad")
try:
    engine = DataQualityEngine()
    engine.create_validated_table(df_input, "web_audit_table")
    metrics = engine.run_data_assertions("web_audit_table")
    engine.close()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Registros Válidos", metrics["total_valid_rows"])
    col2.metric("Nulos en Clientes", metrics["null_customers"])
    col3.metric("Nulos en Montos", metrics["null_amounts"])
    col4.metric("Outliers (>50k)", metrics["high_amount_outliers"])
    
    st.success("¡Validación de integridad superada exitosamente bajo los estándares de restricciones DuckDB!")
except Exception as e:
    st.error(f"❌ Error de Validación de Calidad (Violación de Constraints): {e}")