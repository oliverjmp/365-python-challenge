import os
import time
from parquet_query_engine import EnterpriseParquetEngine

def ejecutar_demostracion_empresarial():
    print("======================================================")
    print("   D183 - MOTOR ANALÍTICO CORPORATIVO (DUCKDB + PARQUET) ")
    print("======================================================\n")

    archivo_parquet = "data_lake/transacciones_enterprise.parquet"
    engine = EnterpriseParquetEngine()

    # Paso 1: Ingesta y almacenamiento columnar avanzado
    print("[1/3] Iniciando simulación de ingesta corporativa...")
    meta = engine.simular_ingesta_corporativa(archivo_parquet)
    print(f" > Registros procesados: {meta['registros']:,}")
    print(f" > Fichero en disco: {archivo_parquet} ({meta['tamano_mb']} MB)")
    print(f" > Tiempo de escritura (Compresión ZSTD): {meta['tiempo_escritura_s']}s\n")

    # Paso 2: Ejecución de analítica de cero copia (Zero-Copy)
    print("[2/3] Ejecutando consulta SQL directa sobre el fichero Parquet (Sin RAM)...")
    analisis = engine.ejecutar_analitica_directa(archivo_parquet)
    print(f" > Latencia de la consulta analítica: {analisis['latencia_consulta_ms']} ms\n")

    # Paso 3: Visualización de resultados de negocio
    print("[3/3] Reporte Analítico Consolidado:")
    print(analisis["dataframe_resultados"].to_string(index=False))

    # Limpieza controlada del entorno de demostración
    engine.cerrar_conexion()
    if os.path.exists(archivo_parquet):
        os.remove(archivo_parquet)
    
    print("\n======================================================")
    print("       ¡DEMOSTRACIÓN FINALIZADA CON ÉXITO!            ")
    print("======================================================")

if __name__ == "__main__":
    ejecutar_demostracion_empresarial()