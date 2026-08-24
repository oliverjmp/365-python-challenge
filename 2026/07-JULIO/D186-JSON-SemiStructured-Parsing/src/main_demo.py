import os
from json_parsing_engine import JSONSemiStructuredEngine

def ejecutar_demostracion_d186():
    print("==================================================================")
    print("   D186 - MOTOR DE EXTRACCIÓN DE DATOS SEMI-ESTRUCTURADOS (JSON)  ")
    print("==================================================================\n")

    archivo_parquet = "data_lake/eventos_semi_estructurados.parquet"
    engine = JSONSemiStructuredEngine()

    print("[1/3] Generando dataset corporativo con payloads JSON anidados...")
    meta = engine.generar_dataset_json(archivo_parquet)
    print(f" > Registros generados: {meta['total_filas']:,}")
    print(f" > Fichero en disco (ZSTD): {archivo_parquet} ({meta['tamano_mb']} MB)\n")

    print("[2/3] Ejecutando consultas SQL sobre estructuras JSON anidadas...")
    analisis = engine.consultar_datos_json(archivo_parquet)
    print(f" > Latencia de la consulta analítica: {analisis['latencia_ms']} ms\n")

    print("[3/3] Reporte Consolidado (Primeras filas):")
    print(analisis["dataframe_resultados"].head(5).to_string(index=False))

    engine.cerrar_conexion()
    print("\n==================================================================")
    print("            ¡DEMOSTRACIÓN D186 COMPLETADA CON ÉXITO!              ")
    print("  Para desplegar el Dashboard interactivo ejecuta:                ")
    print("  python -m streamlit run src/dashboard.py                        ")
    print("==================================================================")

if __name__ == "__main__":
    ejecutar_demostracion_d186()