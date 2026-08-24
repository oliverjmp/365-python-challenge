import cProfile
import pstats
import io
import time
import pandas as pd
from typing import Tuple, Any

def simulate_heavy_computation(delay: float = 0.5) -> pd.DataFrame:
    """Simula una tarea de procesamiento pesado o consulta analítica intensiva."""
    time.sleep(delay)
    # Generar un DataFrame sintético grande para la prueba de rendimiento
    data = {
        "ID": range(1, 1001),
        "Valor": [i * 1.5 for i in range(1, 1001)],
        "Categoria": ["A" if i % 2 == 0 else "B" for i in range(1, 1001)]
    }
    return pd.DataFrame(data)

def profile_function(func, *args, **kwargs) -> Tuple[Any, str]:
    """Ejecuta cProfile sobre una función dada y retorna su resultado junto con el reporte en texto."""
    profiler = cProfile.Profile()
    profiler.enable()
    
    result = func(*args, **kwargs)
    
    profiler.disable()
    s = io.StringIO()
    
    # Usamos directamente el string 'cumulative' para evitar problemas de enums en Windows
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(15)  # Mostrar las 15 funciones principales
    
    return result, s.getvalue()