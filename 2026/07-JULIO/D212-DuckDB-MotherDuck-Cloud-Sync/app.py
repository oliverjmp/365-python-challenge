import streamlit as st
import pandas as pd
from src.duck_sync import DuckDBMotherDuckManager

st.set_page_config(page_title="D212 - DuckDB & MotherDuck Cloud Sync", layout="wide")

st.title("🦆 D212: Panel Híbrido DuckDB & MotherDuck Cloud Sync")
st.markdown("Sincronización híbrida de bases de datos analíticas locales con la infraestructura en la nube de MotherDuck.")

df_demo = pd.DataFrame({
    "transaccion_id": range(1, 501),
    "monto": [float(i * 10.5) for i in range(1, 501)],
    "categoria": ["Hardware" if i % 2 == 0 else "Software" for i in range(500)]
})

st.subheader("📊 Dataset Analítico Local en Memoria")
st.dataframe(df_demo.head(10), width="stretch")

if st.button("☁️ Sincronizar con MotherDuck (Cloud Sync)"):
    manager = DuckDBMotherDuckManager(":memory:")
    manager.create_local_table("transacciones_locales", df_demo)
    
    synced_rows = manager.simulate_cloud_sync("transacciones_locales", "md.transacciones_nube")
    
    st.success("¡Sincronización híbrida completada con éxito!")
    st.info(f"Registros analíticos sincronizados hacia la nube: {synced_rows}")
    
    manager.close()