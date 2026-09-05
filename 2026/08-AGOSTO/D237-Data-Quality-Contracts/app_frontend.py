import streamlit as st
import pandas as pd
from src.data_contract import DataQualityValidator

st.set_page_config(page_title="D237 - Data Quality Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ Dashboard de Calidad y Contratos de Datos")
st.markdown("Certificación de datasets en tiempo real utilizando **Great Expectations**.")

st.sidebar.header("Generador de Escenarios")
scenario = st.sidebar.radio("Seleccione el dataset a evaluar:", ("Dataset Íntegro", "Dataset Corrupto (Anomalías)"))

if scenario == "Dataset Íntegro":
    df = pd.DataFrame({
        "tx_id": ["TX-01", "TX-02", "TX-03"],
        "monto": [1250.0, 450.5, 3000.0],
        "estado": ["APROBADO", "PENDIENTE", "APROBADO"]
    })
else:
    df = pd.DataFrame({
        "tx_id": ["TX-01", "TX-02", "TX-03"],
        "monto": [-50.0, None, 3000.0],
        "estado": ["APROBADO", "IRREGULAR", "APROBADO"]
    })

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Dataset de Entrada")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("Auditoría del Contrato de Datos")
    if st.button("Ejecutar Validación de Calidad", type="primary"):
        with st.spinner("Evaluando expectativas de Great Expectations..."):
            validator = DataQualityValidator()
            report = validator.validate_procurement_data(df)
            
            if report["success"]:
                st.success("✅ **CONTRATO CUMPLIDO:** El dataset ha superado todas las pruebas de integridad.")
            else:
                st.error("🚨 **INCUMPLIMIENTO DE CONTRATO:** Se detectaron anomalías estructurales o de rango.")
            
            st.metric("Expectativas Evaluadas", report["statistics"]["evaluated_expectations"])
            st.write(f"- **Exitosas:** {report['statistics']['successful_expectations']}")
            st.write(f"- **Fallidas:** {report['statistics']['unsuccessful_expectations']}")