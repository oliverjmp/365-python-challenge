import logging
from src.profiler import MemoryProfiler

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def heavy_data_processing():
    """Simula un procesamiento masivo de datos cargando objetos en memoria."""
    data = [range(500000) for _ in range(10)]
    return len(data)

def main():
    logging.info("=== Iniciando Perfilador de Memoria RAM (D114) ===")
    
    logging.info("Ejecutando tarea de procesamiento masivo bajo monitoreo de tracemalloc...")
    result, metrics = MemoryProfiler.measure_memory_usage(heavy_data_processing)
    
    logging.info(f"Resultado de la tarea: {result} colecciones procesadas.")
    logging.info(f"--- Métricas de Memoria y Rendimiento ---")
    logging.info(f"• Memoria Actual al finalizar: {metrics['current_memory_kb']:.2f} KB")
    logging.info(f"• Pico Máximo de Memoria (Peak): {metrics['peak_memory_kb']:.2f} KB")
    logging.info(f"• Tiempo de Ejecución: {metrics['execution_time_sec']:.4f} segundos")
    
    logging.info("=== Hito D114 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()