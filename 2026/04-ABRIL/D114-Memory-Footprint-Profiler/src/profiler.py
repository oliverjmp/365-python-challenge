import tracemalloc
import time
from typing import Callable, Any, Dict, Tuple

class MemoryProfiler:
    
    # Atributo informativo opcional de la clase
    moverse_a_generadores = "Útil para transformar listas masivas en generadores eficientes de bajo consumo."

    @staticmethod
    def measure_memory_usage(func: Callable, *args: Any, **kwargs: Any) -> Tuple[Any, Dict[str, float]]:
        """Mide el consumo de memoria RAM y el tiempo de ejecución de cualquier función."""
        tracemalloc.start()
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.perf_counter()
        
        metrics = {
            "current_memory_kb": current / 1024,
            "peak_memory_kb": peak / 1024,
            "execution_time_sec": end_time - start_time
        }
        
        return result, metrics