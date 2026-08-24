import os
from arrow_bridge_engine import PandasDuckDBBridgeEngine

def ejecutar_demostracion_d185():
    print("==================================================================")
    print("   D185 - PUENTE DE RENDIMIENTO PANDAS + DUCKDB (APACHE ARROW)   ")
    print("==================================================================\n")

    engine = PandasDuckDBBridgeEngine()

    print("[1/3] Generando dataset y convirtiendo a formato columnar Arrow...")
    table_arrow = engine.generar_dataset_vectorial(150000)
    print(f" > Estructura Arrow generada con éxito ({table_arrow.num_rows:,} filas)\n")

    print("[2/3] Ejecutando motor de analítica Zero-Copy sobre Apache Arrow...")
    analisis = engine.ejecutar_analitica_bridge(table_arrow)
    print(f" > Latencia del motor analítico: {analisis['latencia_ms']} ms\n")

    print("[3/3] Reporte Consolidado (Top 5 resultados):")
    print(analisis["dataframe_resultados"].head(5).to_string(index=False))

    engine.cerrar_conexion()
    print("\n==================================================================")
    print("            ¡DEMOSTRACIÓN D185 COMPLETADA CON ÉXITO!              ")
    print("  Para desplegar el Dashboard interactivo ejecuta:                ")
    print("  python -m streamlit run src/dashboard.py                        ")
    print("==================================================================")

if __name__ == "__main__":
    ejecutar_demostracion_d185()