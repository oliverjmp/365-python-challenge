import time
import logging
from src.process_manager import OSProcessManager

# Configurar el sistema de logging para ver los avisos claramente en consola
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("=== Iniciando Monitoreo del OS Process Manager (D98) ===")
    
    # Instanciamos el gestor con umbrales ajustados para pruebas (ej. 70% CPU o Memoria)
    manager = OSProcessManager(cpu_threshold=70.0, mem_threshold=70.0)
    
    logging.info("[*] Listando los 5 procesos principales actuales por consumo...")
    processes = manager.list_running_processes()
    
    # Ordenar por uso de memoria de mayor a menor para mostrar información relevante
    sorted_processes = sorted(processes, key=lambda x: x["memory_percent"], reverse=True)[:5]
    
    for proc in sorted_processes:
        logging.info(f" -> PID: {proc['pid']} | Nombre: {proc['name']} | CPU: {proc['cpu_percent']}% | Memoria: {proc['memory_percent']}%")
    
    logging.info("[*] Ejecutando análisis de control de recursos y prevención de cuelgues...")
    terminated = manager.check_and_terminate_heavy_processes()
    
    if terminated:
        logging.warning(f"[!] Se terminaron {len(terminated)} procesos por exceso de recursos.")
    else:
        logging.info("[+] Sistema estable. Ningún proceso superó los umbrales críticos.")
        
    logging.info("=== Ejecución Finalizada con Éxito ===")

if __name__ == "__main__":
    main()