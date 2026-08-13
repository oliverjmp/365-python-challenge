import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger("Telemetry")

def measure_performance(func: Callable) -> Callable:
    """Decorador avanzado de telemetría para medir latencia y rendimiento de funciones."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        success = True
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            success = False
            raise e
        finally:
            end_time = time.perf_counter()
            duration_ms = (end_time - start_time) * 1000
            logger.info(
                f"[TELEMETRY] Función '{func.__name__}' ejecutada en {duration_ms:.4f} ms | Estado: {'EXITO' if success else 'FALLIDO'}"
            )
    return wrapper