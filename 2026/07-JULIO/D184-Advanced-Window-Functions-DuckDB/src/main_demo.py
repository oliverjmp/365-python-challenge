import os
from window_analytics_engine import AdvancedWindowAnalyticsEngine

def ejecutar_demostracion_d184():
    print("==================================================================")
    print("   D184 - MOTOR DE FUNCIONES DE VENTANA AVANZADAS (DUCKDB)       ")
    print("==================================================================\n")

    archivo_parquet = "data_lake/historico_financiero.parquet"
    engine = AdvancedWindowAnalyticsEngine()

    # 1. Ingesta
    print("[1/3] Generando dataset histórico corporativo...")
    meta = engine.generar_dataset_financiero(archivo_parquet)
    print(f" > Registros generados: {meta['total_filas']}")
    print(f" > Almacenamiento ZSTD en disco: {archivo_parquet} ({meta['tamano_mb']} MB)\n")

    # 2. SQL Analítico
    print("[2/3] Calculando métricas financieras con funciones de ventana (LAG, SUM OVER)...")
    analisis = engine.calcular_metricas_financieras(archivo_parquet)
    print(f" > Latencia del motor analítico: {analisis['latencia_ms']} ms\n")

    # 3. Presentación
    print("[3/3] Muestra de Resultados Analíticos (Top 5 registros):")
    print(analisis["dataframe_resultados"].head(5).to_string(index=False))

    engine.cerrar_conexion()

    print("\n==================================================================")
    print("            ¡DEMOSTRACIÓN D184 COMPLETADA CON ÉXITO!              ")
    print("==================================================================")

if __name__ == "__main__":
    ejecutar_demostracion_d184()