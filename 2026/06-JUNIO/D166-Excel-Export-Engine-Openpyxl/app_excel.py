import streamlit as st
import pandas as pd
from src.exporter import generate_styled_excel

st.set_page_config(
    page_title="D166 - Excel Export Engine",
    page_icon="📥",
    layout="wide"
)

st.title("📥 D166: Motor de Exportación Profesional a Excel")
st.markdown("Generación automatizada de ficheros `.xlsx` con estilos corporativos y formato avanzado.")

# Datos de muestra para el reporte analítico
data = {
    "ID Transacción": [1001, 1002, 1003, 1004, 1005],
    "Departamento": ["Finanzas", "Operaciones", "Ventas", "TI", "Marketing"],
    "Responsable": ["Ana Pérez", "Carlos Ruiz", "Lucía Gómez", "Miguel Ángel", "Sofía Torres"],
    "Presupuesto Asignado": [15400.50, 22300.00, 48900.75, 12000.00, 31500.25],
    "Estado": ["Aprobado", "Pendiente", "Aprobado", "Aprobado", "En Revisión"]
}
df_report = pd.DataFrame(data)

st.subheader("📊 Vista Previa del Reporte Ejecutivo")
st.dataframe(df_report, use_container_width=True)

# Botón de exportación con Openpyxl
excel_file = generate_styled_excel(df_report, sheet_name="Resumen Ejecutivo")

st.download_button(
    label="📥 Descargar Reporte en Excel Profesional",
    data=excel_file,
    file_name="reporte_ejecutivo_d166.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)