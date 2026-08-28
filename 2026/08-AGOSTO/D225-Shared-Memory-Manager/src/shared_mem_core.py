import numpy as np
from multiprocessing import shared_memory
from concurrent.futures import ProcessPoolExecutor

def process_shared_array(shm_name: str, shape: tuple, dtype: str) -> dict:
    """Función ejecutada por un proceso hijo que accede directamente a la memoria compartida sin serializar."""
    try:
        # Conectar al bloque de memoria compartida existente por su nombre
        existing_shm = shared_memory.SharedMemory(name=shm_name)
        # Reconstruir la vista de NumPy sobre el buffer compartido existente
        arr = np.ndarray(shape, dtype=dtype, buffer=existing_shm.buf)
        
        # Realizar una operación numérica directa in-place (ej: multiplicar por 2)
        arr *= 2
        sum_val = float(np.sum(arr))
        
        existing_shm.close()
        return {"status": "SUCCESS", "sum": sum_val}
    except Exception as e:
        return {"status": "FAILED", "error": str(e)}

class SharedMemoryManagerEngine:
    """Núcleo de gestión de memoria compartida de alta velocidad para matrices NumPy entre procesos."""

    def execute_shared_computation(self, data: np.ndarray) -> dict:
        """Asigna un arreglo en memoria compartida y lanza un proceso hijo para operar sobre él."""
        if data is None or data.size == 0:
            raise ValueError("El arreglo de entrada no puede estar vacío.")

        # Crear bloque de memoria compartida dimensionado exactamente al tamaño del array de NumPy
        shm = shared_memory.SharedMemory(create=True, size=data.nbytes)
        try:
            # Crear un array NumPy respaldado por el buffer de la memoria compartida recién creada
            shared_arr = np.ndarray(data.shape, dtype=data.dtype, buffer=shm.buf)
            shared_arr[:] = data[:] # Copiar datos iniciales

            # Ejecutar proceso hijo pasando únicamente metadatos (nombre, forma y tipo) sin serializar la matriz
            with ProcessPoolExecutor(max_workers=1) as executor:
                future = executor.submit(process_shared_array, shm.name, data.shape, str(data.dtype))
                result = future.result()

            # Leer el resultado modificado directamente desde el buffer compartido antes de destruir la memoria
            final_data = np.ndarray(data.shape, dtype=data.dtype, buffer=shm.buf).copy()

            return {
                "initial_shape": data.shape,
                "computation_result": result,
                "modified_data": final_data.tolist()
            }
        finally:
            # Limpieza obligatoria del recurso de memoria compartida del sistema operativo
            shm.close()
            shm.unlink()