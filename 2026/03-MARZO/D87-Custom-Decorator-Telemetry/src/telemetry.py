import functools
import time
import logging
from typing import Callable, Any

# Configuración básica de logs para telemetría
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TelemetryLogger")

def monitor_telemetry(func: Callable) -> Callable:
    """Decorador avanzado para medir el tiempo de ejecución y registrar telemetría."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        success = True
        error_msg = None
        
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            success = False
            error_msg = str(e)
            raise
        finally:
            end_time = time.perf_counter()
            duration_ms = (end_time - start_time) * 1000
            
            log_data = {
                "function": func.__name__,
                "duration_ms": round(duration_ms, 4),
                "success": success
            }
            if error_msg:
                log_data["error"] = error_msg
                
            logger.info(f"TELEMETRY: {log_data}")
            
    return wrapper