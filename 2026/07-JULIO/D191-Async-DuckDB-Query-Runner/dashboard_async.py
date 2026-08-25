import streamlit as st
import asyncio
import time
import pandas as pd
from src.async_engine import AsyncDuckDBRunner

# Configuración de la página web
st.set_page_config(
    page_title="D191 - Async DuckDB Query Runner",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Tablero Ejecutivo - Motor Asíncrono de DuckDB (D191)")
st.markdown("Demostración visual de **ejecución concurrente y no bloqueante** sobre el Almacén de Datos (Data Lake).")

# Inicializar el runner apuntando al Data Lake
@st.cache_resource
def get_runner():
    return AsyncDuckDBRunner(db_path="data_lake/async_analytics.db")

runner = get_runner()

st.sidebar.header("🎛️ Panel de Control")
st.sidebar.info("Este motor procesa consultas analíticas pesadas en paralelo utilizando `asyncio.gather` y hilos independientes.")

if st.sidebar.button("🚀 Ejecutar Lote de Consultas Concurrente", type="primary"):
    
    # Definir el lote de consultas analíticas
    lote_consultas = [
        {
            "id": "Q_VENTAS_TOTALES",
            "query": "SELECT categoria, SUM(monto) AS total_monto FROM ventas_analiticas GROUP BY categoria;",
            "delay": 0.2
        },
        {
            "id": "Q_FILTRO_TECNOLOGIA",
            "query": "SELECT id, categoria, monto, fecha FROM ventas_analiticas WHERE categoria = 'Tecnología';",
            "delay": 0.1
        },
        {
            "id": "Q_ESTADISTICAS_GLOBALES",
            "query": "SELECT COUNT(*) AS total_registros, AVG(monto) AS promedio, MAX(monto) AS maximo FROM ventas_analiticas;",
            "delay": 0.3
        }
    ]

    with st.spinner("Ejecutando consultas de forma concurrente y no bloqueante..."):
        inicio_total = time.time()
        
        # Ejecutar el bucle asíncrono dentro de Streamlit
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        resultados = loop.run_until_complete(runner.ejecutar_lote_concurrente(lote_consultas))
        
        tiempo_total = (time.time() - inicio_total) * 1000

    # --- Métricas Globales ---
    st.success(f"✅ ¡Lote completado de forma no bloqueante en **{round(tiempo_total, 2)} ms**!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Consultas Procesadas", len(resultados))
    with col2:
        st.metric("Tiempo Total Lote", f"{round(tiempo_total, 2)} ms")
    with col3:
        st.metric("Modo de Ejecución", "Concurrente (Async)")

    st.markdown("---")
    st.subheader("📋 Resultados Detallados por Hilo de Consulta")

    # Mostrar resultados en pestañas (Tabs) interactivas por cada consulta
    tabs = st.tabs([res["query_id"] for res in resultados])
    
    for i, tab in enumerate(tabs):
        res = resultados[i]
        with tab:
            st.write(f"**Identificador:** `{res['query_id']}`")
            st.write(f"**Duración Individual:** `{res['duracion_ms']} ms`")
            st.write(f"**Filas Obtenidas:** `{res['filas_obtenidas']}`")
            
            # Convertir los datos a DataFrame de Pandas para mostrarlos de forma elegante en tabla
            if res["data"]:
                # Inferir nombres de columnas básicos o genéricos según la consulta
                df_res = pd.DataFrame(res["data"])
                st.dataframe(df_res, use_container_width=True)
            else:
                st.info("La consulta no devolvió registros.")

else:
    st.info("👈 Haz clic en el botón **'Ejecutar Lote de Consultas Concurrente'** en la barra lateral para iniciar la demostración en vivo.")