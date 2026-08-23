import streamlit as st
from typing import Optional

def render_kpi_card(title: str, value: str | float, delta: Optional[str] = None, delta_color: str = "normal"):
    """
    Renderiza una tarjeta de KPI personalizada y reutilizable en Streamlit.
    """
    st.markdown(
        f"""
        <div style="
            padding: 20px;
            border-radius: 10px;
            background-color: #f0f2f6;
            border: 1px solid #e0e2e6;
            margin-bottom: 10px;
        ">
            <h4 style="margin: 0; color: #31333F; font-size: 16px;">{title}</h4>
            <h2 style="margin: 10px 0 0 0; color: #0e1117; font-size: 28px;">{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    if delta:
        st.caption(f"Tendencia: {delta} ({delta_color})")

def format_currency_metric(amount: float) -> str:
    """Formatea un valor numérico como divisa estándar."""
    return f"${amount:,.2f}"