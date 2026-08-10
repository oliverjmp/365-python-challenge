import multiprocessing
from typing import List

def _multiply_row_by_scalar(args: tuple) -> List[int]:
    """Multiplica una fila de la matriz por un escalar en un proceso independiente."""
    row, scalar = args
    return [element * scalar for element in row]

class MatrixProcessor:
    def __init__(self, processes: int = None):
        self.processes = processes

    def multiply_matrix_by_scalar(self, matrix: List[List[int]], scalar: int) -> List[List[int]]:
        """Distribuye la multiplicación de la matriz por filas usando un Pool de procesos."""
        if not matrix:
            return []
            
        tasks = [(row, scalar) for row in matrix]
        with multiprocessing.Pool(processes=self.processes) as pool:
            result = pool.map(_multiply_row_by_scalar, tasks)
        return result