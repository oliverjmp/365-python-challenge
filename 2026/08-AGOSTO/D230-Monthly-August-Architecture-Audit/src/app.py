import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import json
from src.audit_engine import AuditEngine

st.set_page_config(
    page_title="D230 - Monthly August Architecture Audit",
    page_icon="📊",
    layout="wide"
)

st.title("📊 D230: Auditoría Integral de Rendimiento y Concurrencia (Agosto)")
st.markdown("""
Panel interactivo para supervisar y ejecutar pruebas de carga concurrentes sobre la arquitectura desarrollada durante el mes.
""")

st.sidebar.header("⚙️ Configuración de Auditoría")
probes_count = st.sidebar.slider("Número de Sondas Concurrentes", min_value=1, max_value=20, value=5)
workers_count = st.sidebar.slider("Hilos del Pool de Ejecución", min_value=1, max_value=8, value=4)

if st.button("🚀 Ejecutar Auditoría Arquitectónica", type="primary"):
    with st.spinner("Ejecutando pruebas concurrentes..."):
        engine = AuditEngine(max_workers=workers_count)
        audit_report = engine.run_full_audit(total_probes=probes_count)
        
        st.success("¡Auditoría completada con éxito!")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total de Sondas", audit_report["total_probes"])
        col2.metric("Pruebas Exitosas", audit_report["passed"])
        col3.metric("Índice de Salud", f"{audit_report['health_score']}%")
        
        st.subheader("📋 Detalle de Resultados por Sonda")
        st.table(audit_report["details"])
        
        st.subheader("📦 Reporte JSON Exportado")
        st.json(audit_report)