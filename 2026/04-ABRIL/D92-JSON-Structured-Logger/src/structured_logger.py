import logging
import json
from contextvars import ContextVar
from typing import Dict, Any, Optional

# ContextVar para mantener el Correlation ID de forma segura en entornos concurrentes o síncronos
correlation_id_var: ContextVar[Optional[str]] = ContextVar("correlation_id", default=None)

class JsonFormatter(logging.Formatter):
    """Formateador personalizado para convertir los registros de log a formato JSON."""
    def format(self, record: logging.LogRecord) -> str:
        log_data: Dict[str, Any] = {
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "timestamp": self.formatTime(record, self.datefmt)
        }
        
        # Añadir Correlation ID si está presente en el contexto
        corr_id = correlation_id_var.get()
        if corr_id:
            log_data["correlation_id"] = corr_id
            
        # Añadir atributos adicionales si se pasaron en el log
        if hasattr(record, "extra_data") and isinstance(record.extra_data, dict):
            log_data.update(record.extra_data)
            
        return json.dumps(log_data)

def get_structured_logger(name: str) -> logging.Logger:
    """Configura y devuelve un logger corporativo estructurado en JSON."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
    return logger

def set_correlation_id(correlation_id: str) -> None:
    """Establece el Correlation ID para el contexto actual."""
    correlation_id_var.set(correlation_id)