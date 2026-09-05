import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd

# Configuración de página
st.set_page_config(page_title="D235 - Procurement AI", page_icon="🛡️", layout="wide")

st.title("🛡️ Prevención de Fraude en Compras Corporativas (ONNX)")
st.markdown("Interfaz ejecutiva para la evaluación en tiempo real de órdenes de compra mediante modelos **ONNX de ultra baja latencia** servidos con FastAPI.")

API_URL = "http://127.0.0.1:8000/detect"
HEALTH_URL = "http://127.0.0.1:8000/health"

# Comprobar salud del microservicio FastAPI
try:
    health = requests.get(HEALTH_URL, timeout=2)
    if health.status_code == 200:
        st.sidebar.success("🟢 Motor ONNX Online y Conectado")
    else:
        st.sidebar.error("🔴 Error en el Motor ONNX")
except requests.exceptions.ConnectionError:
    st.sidebar.error("🔴 Motor Offline (Inicia FastAPI primero)")

st.sidebar.markdown("---")
st.sidebar.header("📝 Detalles de la Orden")

# Formulario de parámetros de compra
with st.sidebar.form("anomaly_form"):
    monto = st.number_input("Monto de la Orden (USD)", min_value=1.0, value=12500.0, step=500.0)
    frecuencia = st.slider("Frecuencia Proveedor (Mensual)", min_value=0.0, max_value=20.0, value=2.5, step=0.1)
    desviacion = st.slider("Desviación de Precio vs Mercado (%)", min_value=-50.0, max_value=150.0, value=15.0, step=1.0)
    
    submit = st.form_submit_button("🔍 Evaluar Riesgo", type="primary")

if submit:
    payload = {
        "monto": monto,
        "frecuencia_proveedor": frecuencia,
        "desviacion_precio": desviacion
    }
    
    try:
        with st.spinner("Ejecutando inferencia ONNX en milisegundos..."):
            response = requests.post(API_URL, json=payload, timeout=5)
            
        if response.status_code == 200:
            result = response.json()
            is_anomaly = result.get("anomaly_detected", False)
            
            st.markdown("---")
            st.subheader("🎯 Veredicto del Modelo")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if is_anomaly:
                    st.error("🚨 **ALERTA: ANOMALÍA DETECTADA**")
                    st.markdown("La transacción presenta patrones inusuales que sugieren riesgo de fraude, sobreprecio o irregularidad en adquisiciones.")
                else:
                    st.success("✅ **ORDEN VALIDADA**")
                    st.markdown("Los parámetros de la orden se encuentran dentro del comportamiento histórico normal. Aprobación recomendada.")
                    
                st.metric("Latencia de Red + Inferencia", f"{response.elapsed.microseconds / 1000:.2f} ms")
                st.info("⚡ Inferencia acelerada por ONNX Runtime sin dependencias de Scikit-Learn.")
                
            with col2:
                # Gráfico Radar para el perfil de riesgo (Normalizando datos visualmente)
                fig = go.Figure(data=go.Scatterpolar(
                    r=[
                        min(monto / 50000, 1.0),            # Normalizado a 50k max
                        min(frecuencia / 20, 1.0),          # Normalizado a 20 max
                        max(0, min((desviacion) / 100, 1.0)) # Normalizado
                    ],
                    theta=['Volumen Monetario', 'Frecuencia Proveedor', 'Desviación Precio'],
                    fill='toself',
                    marker_color='red' if is_anomaly else '#00cc96',
                    line_color='darkred' if is_anomaly else 'darkgreen'
                ))
                
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=False, range=[0, 1])),
                    showlegend=False,
                    title="Perfil Multidimensional de la Transacción",
                    height=350,
                    margin=dict(l=40, r=40, t=40, b=40)
                )
                st.plotly_chart(fig, use_container_width=True)
                
        else:
            st.error(f"Error de validación (Pydantic): Revisa los datos ingresados. Código {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ **No se pudo conectar con el servidor.** Asegúrate de ejecutar `uvicorn src.api:app` en otra terminal.")
else:
    st.info("👈 Modifica los parámetros en la barra lateral y haz clic en **'Evaluar Riesgo'** para analizar una transacción usando la API de FastAPI.")