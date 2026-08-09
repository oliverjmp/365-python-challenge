import logging
import psutil

# Configuración básica del Logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("SystemMonitor")

class SystemMonitor:
    def __init__(self, cpu_threshold: float = 80.0, memory_threshold: float = 80.0):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold

    def check_metrics(self) -> dict:
        """Captura métricas de CPU, Memoria y Disco."""
        # interval=1 es necesario para psutil para dar una lectura precisa
        metrics = {
            "cpu": psutil.cpu_percent(interval=1),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent
        }
        
        logger.info(f"Métricas actuales -> CPU: {metrics['cpu']}% | Memoria: {metrics['memory']}% | Disco: {metrics['disk']}%")
        self._evaluate_alerts(metrics)
        return metrics

    def _evaluate_alerts(self, metrics: dict):
        """Dispara alertas si los recursos superan los umbrales."""
        if metrics["cpu"] > self.cpu_threshold:
            logger.warning(f"¡Alerta de CPU alta! {metrics['cpu']}%")
        if metrics["memory"] > self.memory_threshold:
            logger.warning(f"¡Alerta de Memoria alta! {metrics['memory']}%")