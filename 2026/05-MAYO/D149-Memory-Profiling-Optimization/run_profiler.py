import logging
import pandas as pd
from src.memory_profiler import MemoryProfilerEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Perfilamiento y Optimización de Memoria (D149) ===")
    
    profiler = MemoryProfilerEngine()
    
    # Generar DataFrame analítico pesado (ej. 200,000 filas)
    num_rows = 200_000
    logging.info(f"Generando dataset analítico con {num_rows:,} registros...")
    
    # Perfilando la creación y carga inicial en memoria
    df_raw, peak_creation_mb = profiler.measure_memory_usage(
        profiler.generate_heavy_dataframe, num_rows=num_rows
    )
    
    stats_raw = profiler.get_memory_stats(df_raw)
    logging.info(f"Memoria inicial consumida (RAM Pico): {peak_creation_mb:.2f} MB")
    logging.info(f"Tamaño reportado por Pandas (deep): {stats_raw['mb']:.2f} MB")
    
    print("\n--- Tipos de Datos Originales ---")
    print(df_raw.dtypes)
    
    # Optimización de tipos de datos
    logging.info("Aplicando optimización de tipos de datos para reducir RAM...")
    df_optimized = profiler.optimize_dataframe_memory(df_raw)
    stats_optimized = profiler.get_memory_stats(df_optimized)
    
    print("\n--- Tipos de Datos Optimizado ---")
    print(df_optimized.dtypes)
    
    # Resultados comparativos
    reduction_pct = ((stats_raw['mb'] - stats_optimized['mb']) / stats_raw['mb']) * 100
    
    print("\n==============================================")
    print(f" Memoria Original:  {stats_raw['mb']:.2f} MB")
    print(f" Memoria Optimizada: {stats_optimized['mb']:.2f} MB")
    print(f" Reducción Lograda:  {reduction_pct:.2f}%")
    print("==============================================")
    
    logging.info("=== Hito D149 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()