import streamlit as st
import requests

st.set_page_config(page_title="D204 Analytics Dashboard", page_icon="📊", layout="wide")

st.title("📊 Dashboard Analítico (Docker Compose + FastAPI)")
st.markdown("Consumiendo datos desde el microservicio analítico en FastAPI.")

try:
    response = requests.get("http://localhost:8000/analytics/summary")
    if response.status_code == 200:
        res = response.json()
        if res["status"] == "success":
            data = res["data"]
            st.success("✅ Conexión exitosa con el microservicio FastAPI.")
            st.subheader("📋 Resumen por Categoría")
            st.dataframe(data, use_container_width=True)
        else:
            st.error(f"Error en API: {res.get('message')}")
    else:
        st.error("❌ No se pudo conectar con el microservicio. ¿Está corriendo Docker Compose?")
except Exception as e:
    st.warning(f"⚠️ Asegúrate de levantar el stack con `docker-compose up --build`. Detalle: {e}")