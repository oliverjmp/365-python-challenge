import streamlit as st
import pandas as pd
from src.filter_engine import DataFilterEngine

# Configuración de página
st.set_page_config(
    page_title="D152 - Dynamic Sidebar Filters",
    page_icon="📊",
    layout="wide"
)

# Dataset simulado de ejemplo
@st.cache_data
def load_data():
    return pd.DataFrame({
        "id": range(1, 101),
        "departamento": ["Ventas", "IT", "Marketing", "Finanzas"] * 25,
        "presupuesto": [val * 125.5 for val in range(1, 101)],
        "activo": [True, False, True, True] * 25
    })

df = load_data()
engine = DataFilterEngine(df)

st.sidebar.title("🎛️ Filtros Dinámicos")

# Filtro 1: Multiselect por Departamento
all_deps = df["departamento"].unique().tolist()
selected_deps = st.sidebar.multiselect("Seleccionar Departamentos", all_deps, default=all_deps)

# Filtro 2: Slider por Rango de Presupuesto
min_p = float(df["presupuesto"].min())
max_p = float(df["presupuesto"].max())
selected_range = st.sidebar.slider("Rango de Presupuesto", min_p, max_p, (min_p, max_p))

# Aplicar filtros de forma encadenada
filtered_df = engine.filter_by_categories("departamento", selected_deps)
filtered_df = engine.filter_by_numeric_range("presupuesto", selected_range[0], selected_range[1])

# Métricas Principales
st.title("📊 Panel de Control con Filtros Multidimensionales")
metrics = engine.get_summary_metrics(filtered_df, "presupuesto")

col1, col2, col3 = st.columns(3)
col1.metric("Registros Filtrados", metrics["count"])
col2.metric("Presupuesto Total", f"${metrics['total']:,.2f}")
col3.metric("Promedio por Registro", f"${metrics['average']:,.2f}")

st.markdown("---")
st.subheader("📋 Detalle de Datos Filtrados")
st.dataframe(filtered_df, use_container_width=True)