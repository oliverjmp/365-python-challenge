import pytest
from src.matrix_processor import MatrixProcessor, _multiply_row_by_scalar

def test_matrix_scalar_multiplication():
    """Valida que la multiplicación de una matriz por un escalar en paralelo sea correcta."""
    processor = MatrixProcessor(processes=2)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    scalar = 3
    
    expected = [
        [3, 6, 9],
        [12, 15, 18],
        [21, 24, 27]
    ]
    
    result = processor.multiply_matrix_by_scalar(matrix, scalar)
    assert result == expected

def test_empty_matrix_multiplication():
    """Valida el comportamiento del procesador ante una matriz vacía."""
    processor = MatrixProcessor(processes=2)
    matrix = []
    scalar = 5
    
    result = processor.multiply_matrix_by_scalar(matrix, scalar)
    assert result == []

def test_helper_row_multiplication_directly():
    """Fuerza la ejecución directa de la función auxiliar para asegurar el 100% de cobertura en Windows."""
    row = [1, 2, 3]
    scalar = 4
    result = _multiply_row_by_scalar((row, scalar))
    assert result == [4, 8, 12]