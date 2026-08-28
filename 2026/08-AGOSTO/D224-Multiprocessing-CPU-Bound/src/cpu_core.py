import math
from concurrent.futures import ProcessPoolExecutor

def compute_heavy_math(n: int) -> int:
    """Función de carga intensiva de CPU (cálculo factorial pesado o sumatorias)."""
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    return math.factorial(n)

class MultiprocessingCPUBoundManager:
    """Núcleo de ejecución paralela para superar el GIL mediante multiprocessing."""

    def compute_batch(self, numbers: list[int], max_workers: int = None) -> dict:
        """Ejecuta un lote de cálculos numéricos pesados en paralelo usando múltiples núcleos de CPU."""
        if not numbers:
            raise ValueError("La lista de números no puede estar vacía.")
        if max_workers is not None and max_workers <= 0:
            raise ValueError("El número de workers debe ser mayor a cero.")

        results = []
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            future_to_number = {executor.submit(compute_heavy_math, num): num for num in numbers}
            for future in future_to_number:
                num = future_to_number[future]
                try:
                    res = future.result()
                    results.append({"number": num, "result_digits": len(str(res)), "status": "SUCCESS"})
                except Exception as e:
                    results.append({"number": num, "result_digits": 0, "error": str(e), "status": "FAILED"})

        return {
            "total_computations": len(numbers),
            "max_workers_used": max_workers,
            "results": results
        }