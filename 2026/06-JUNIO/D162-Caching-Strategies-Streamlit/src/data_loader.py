import time
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data(ttl=60, show_spinner="Cargando datos pesados optimizados...")
def load_cached_data(row_count: int) -> pd.DataFrame:
    """
    Simula una consulta analítica pesada cacheada en memoria.
    """
    time.sleep(2)  # Simulación de latencia de base de datos
    np.random.seed(42)
    data = {
        "id": range(1, row_count + 1),
        "category": np.random.choice(["Finanzas", "Operaciones", "Ventas", "TI"], row_count),
        "value": np.random.uniform(50.0, 500.0, row_count),
        "date": pd.date_range(start="2026-01-01", periods=row_count, freq="h")
    }
    return pd.DataFrame(data)