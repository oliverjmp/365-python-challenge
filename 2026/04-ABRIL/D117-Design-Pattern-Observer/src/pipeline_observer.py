from abc import ABC, abstractmethod
from typing import List, Dict, Any
import logging

logger = logging.getLogger("PipelineObserver")

class Observer(ABC):
    """Interfaz abstracta para los observadores del pipeline."""
    @abstractmethod
    def update(self, event_name: str, data: Dict[str, Any]) -> None:
        pass

class Subject(ABC):
    """Clase base o interfaz para el sujeto (Publisher) que emite eventos."""
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event_name: str, data: Dict[str, Any]) -> None:
        for observer in self._observers:
            observer.update(event_name, data)

class DataPipeline(Subject):
    """Pipeline de datos que actúa como Sujeto, notificando eventos a sus observadores."""
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self, records: int) -> None:
        logger.info(f"Iniciando ejecución del pipeline '{self.name}'...")
        self.notify("pipeline_started", {"pipeline": self.name, "records": records})
        
        try:
            # Simulación de procesamiento de datos
            if records <= 0:
                raise ValueError("Cantidad de registros inválida")
            
            logger.info(f"Procesando {records} registros exitosamente...")
            self.notify("pipeline_success", {"pipeline": self.name, "records_processed": records})
        except Exception as e:
            logger.error(f"Error en pipeline '{self.name}': {str(e)}")
            self.notify("pipeline_failed", {"pipeline": self.name, "error": str(e)})

class LoggingObserver(Observer):
    """Observador encargado de registrar eventos en los logs del sistema."""
    def update(self, event_name: str, data: Dict[str, Any]) -> None:
        logger.info(f"[LOG OBSERVER] Evento recibido -> '{event_name}' con datos: {data}")

class MetricsObserver(Observer):
    """Observador encargado de capturar métricas de rendimiento o estado."""
    def __init__(self):
        self.events_received: List[str] = []

    def update(self, event_name: str, data: Dict[str, Any]) -> None:
        self.events_received.append(event_name)
        logger.info(f"[METRICS OBSERVER] Métrica actualizada por evento '{event_name}'")