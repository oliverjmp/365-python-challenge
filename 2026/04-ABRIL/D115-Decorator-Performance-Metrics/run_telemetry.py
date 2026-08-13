import logging
import time
from src.telemetry import measure_performance

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@measure_performance
def heavy_computation_task(iterations: int):
    """Simula una tarea de procesamiento pesado."""
    total = 0
    for i in range(iterations):
        total += i
    time.sleep(0.05)  # Simular latencia de red o base de datos
    return total

def main():
    logging.info("=== Iniciando Sistema de Telemetría Avanzada (D115) ===")
    
    logging.info("Ejecutando función decorada...")
    resultado = heavy_computation_task(1000000)
    
    logging.info(f"Resultado de la tarea computacional: {resultado}")
    logging.info("=== Hito D115 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()