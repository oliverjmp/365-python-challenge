import streamlit as st
import pandas as pd
import json
import logging
from pathlib import Path

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA Y LOGS
# ---------------------------------------------------------
st.set_page_config(page_title="D13 - Data Quality Validator", layout="wide")

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    filename=LOG_DIR / "data_quality.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------------------------------------------
# FUNCIONES DE CARGA Y VALIDACIÓN
# ---------------------------------------------------------
def load_rules(path="rules.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("❌ No se encontró el archivo 'rules.json'.")
        return None

def validar_dataset_profesional(df, rules):
    errores = []
    total_filas = len(df)
    
    # 1. Verificar Columnas Requeridas
    missing = [col for col in rules["required_columns"] if col not in df.columns]
    if missing:
        errores.append(f"Faltan columnas críticas: {missing}")
    
    # 2. Verificar Duplicados
    duplicados = df.duplicated().sum()
    
    # 3. Verificar Nulos
    nulos_por_columna = df.isnull().sum()
    
    # 4. Verificar Rangos y Tipos (Fila por fila para el reporte visual)
    filas_corruptas = []
    if "range_rules" in rules:
        for col, limits in rules["range_rules"].items():
            if col in df.columns:
                fuera_de_rango = df[(df[col] < limits["min"]) | (df[col] > limits["max"])]
                if not fuera_de_rango.empty:
                    filas_corruptas.append(fuera_de_rango)

    # Calcular Score de Salud (Lógica simple: % de celdas no nulas y no duplicadas)
    celdas_totales = df.size
    celdas_nulas = df.isnull().sum().sum()
    health_score = max(0, 100 - ( (celdas_nulas / celdas_totales) * 100) - ( (duplicados / total_filas) * 100))
    
    return health_score, duplicados, nulos_por_columna, filas_corruptas

# ---------------------------------------------------------
# INTERFAZ DE USUARIO (STREAMLIT)
# ---------------------------------------------------------
st.title("🛡️ Sistema de Auditoría de Calidad de Datos")
st.write("Sube tu archivo CSV para pasar el control de aduanas.")

rules = load_rules()

uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None and rules is not None:
    # Manejo de Encodings Robusto
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8-sig')
    except:
        df = pd.read_csv(uploaded_file, encoding='latin1')

    # Ejecutar validación
    score, dups, nulos, corruptas = validar_dataset_profesional(df, rules)

    # --- MÉTRICAS PRINCIPALES ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Health Score", f"{round(score, 2)}%", delta="Calidad" if score > 80 else "Crítico")
    col2.metric("Duplicados", dups)
    col3.metric("Filas Totales", len(df))

    st.markdown("---")

    # --- ANÁLISIS DETALLADO ---
    tab1, tab2, tab3 = st.tabs(["📊 Vista Previa", "❌ Errores de Rango", "❓ Nulos por Columna"])

    with tab1:
        st.subheader("Primeras 10 filas")
        st.dataframe(df.head(10), use_container_width=True)

    with tab2:
        st.subheader("Filas que violan reglas de rango")
        if corruptas:
            reporte_corruptas = pd.concat(corruptas).drop_duplicates()
            st.warning(f"Se encontraron {len(reporte_corruptas)} filas fuera de los límites permitidos.")
            st.dataframe(reporte_corruptas, use_container_width=True)
        else:
            st.success("✅ ¡No hay valores fuera de rango!")

    with tab3:
        st.subheader("Conteo de valores vacíos")
        st.table(nulos)

    # Botón de descarga si el score es bueno
    if score > 90:
        st.balloons()
        st.success("Dataset apto para producción.")
    else:
        st.error("Dataset NO apto para producción. Limpia los datos primero.")