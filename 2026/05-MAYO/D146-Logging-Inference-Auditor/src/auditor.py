import json
import logging
import sys
import time
from typing import Dict, Any, Callable

class JSONFormatter(logging.Formatter):
    """Formateador personalizado para convertir registros de logging en cadenas JSON estructuradas."""

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if hasattr(record, "audit_data") and isinstance(record.audit_data, dict):
            log_entry.update(record.audit_data)
            
        return json.dumps(log_entry)

class InferenceAuditor:
    """Auditor de inferencias para registrar trazas estructuradas en formato JSON."""

    def __init__(self, logger_name: str = "InferenceAuditor"):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        
        if not self.logger.handlers:
            # Forzar el handler hacia sys.stdout para una captura limpia en pruebas con capsys
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(JSONFormatter())
            self.logger.addHandler(handler)
            self.logger.propagate = False

    def audit_inference(self, request_id: str, model_version: str, features: list, inference_func: Callable[[], Any]) -> Any:
        """Ejecuta una inferencia midiendo su latencia y auditando la petición y respuesta en JSON."""
        if not request_id or not model_version:
            raise ValueError("El ID de petición y la versión del modelo son obligatorios.")

        start_time = time.perf_counter()
        success = True
        prediction = None
        error_message = None

        try:
            prediction = inference_func()
            return prediction
        except Exception as e:
            success = False
            error_message = str(e)
            raise
        finally:
            latency_ms = (time.perf_counter() - start_time) * 1000.0

            audit_payload = {
                "request_id": request_id,
                "model_version": model_version,
                "features_count": len(features) if isinstance(features, list) else 0,
                "latency_ms": round(latency_ms, 4),
                "success": success,
                "prediction": prediction if success else None,
                "error": error_message
            }

            if success:
                self.logger.info("Inferencia ejecutada exitosamente", extra={"audit_data": audit_payload})
            else:
                self.logger.error("Error durante la ejecución de la inferencia", extra={"audit_data": audit_payload})