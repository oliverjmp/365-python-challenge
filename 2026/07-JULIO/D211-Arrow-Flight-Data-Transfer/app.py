import streamlit as st
import pandas as pd
import pyarrow as pa
from src.flight_server import SimpleFlightServer

st.set_page_config(page_title="D211 - Arrow Flight Data Transfer", layout="wide")

st.title("⚡ D211: Panel de Control Apache Flight Data Transfer")
st.markdown("Simulación y transferencia ultrarrápida de datasets distribuidos en memoria mediante el protocolo Apache Flight.")

df_demo = pd.DataFrame({
    "transaccion_id": range(1, 1001),
    "monto": [float(i * 5.25) for i in range(1, 1001)],
    "region": ["Norte" if i % 2 == 0 else "Sur" for i in range(1000)]
})

st.subheader("📊 Dataset Analítico Preparado para Flight")
st.dataframe(df_demo.head(10), use_container_width=True)

if st.button("🚀 Simular Transferencia Ultrarrápida Flight"):
    server = SimpleFlightServer("grpc://localhost:8822")
    server.populate_table("transacciones", df_demo)
    
    # Simular lectura desde cliente virtual
    table = server.flights["transacciones"]
    bytes_size = table.nbytes
    
    st.success(f"¡Transferencia completada exitosamente!")
    st.info(bytes_size)
    server.shutdown()