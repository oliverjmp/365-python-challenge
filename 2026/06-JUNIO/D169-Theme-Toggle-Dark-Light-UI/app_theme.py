import streamlit as st
from src.theme_manager import get_theme_styles

st.set_page_config(
    page_title="D169 - Theme Toggle UI",
    page_icon="🌓",
    layout="wide"
)

# Inicializar el estado de la sesión para el tema si no existe
if "theme" not in st.session_state:
    st.session_state.theme = "Claro"

# Selector de tema en la barra lateral
st.sidebar.title("⚙️ Preferencias de UI")
selected_theme = st.sidebar.selectbox(
    "Selecciona el Modo Visual",
    options=["Claro", "Oscuro"],
    index=0 if st.session_state.theme == "Claro" else 1
)

st.session_state.theme = selected_theme
styles = get_theme_styles(st.session_state.theme)

# Aplicar estilos CSS personalizados basados en el tema
st.markdown(
    f"""
    <style>
    .main {{
        background-color: {styles['bg_color']};
        color: {styles['text_color']};
    }}
    .metric-card {{
        background-color: {styles['card_bg']};
        color: {styles['text_color']};
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    .metric-card h3, .metric-card h2 {{
        color: {styles['text_color']} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌓 Panel Analítico con Adaptación de Tema (D169)")
st.write(f"Actualmente visualizando en **Modo {st.session_state.theme}**.")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <h3>Ingresos Totales</h3>
            <h2>$482,000</h2>
            <p style="color: {styles['accent']}; margin-top: 10px;">+14.2% vs mes anterior</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <h3>Usuarios Activos</h3>
            <h2>12,840</h2>
            <p style="color: {styles['accent']}; margin-top: 10px;">+5.1% nuevos registros</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <h3>Retención de Clientes</h3>
            <h2>94.6%</h2>
            <p style="color: {styles['accent']}; margin-top: 10px;">+0.8% optimización</p>
        </div>
    """, unsafe_allow_html=True)