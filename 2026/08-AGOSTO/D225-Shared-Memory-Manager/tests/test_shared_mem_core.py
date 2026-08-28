import pytest
import numpy as np
from src.shared_mem_core import SharedMemoryManagerEngine, process_shared_array

def test_shared_memory_computation_success():
    engine = SharedMemoryManagerEngine()
    data = np.array([1, 2, 3, 4], dtype=np.int64)
    
    summary = engine.execute_shared_computation(data)
    assert summary["computation_result"]["status"] == "SUCCESS"
    assert summary["computation_result"]["sum"] == 20.0  # (1+2+3+4)*2 = 20
    assert summary["modified_data"] == [2, 4, 6, 8]

def test_execute_shared_computation_empty_data():
    engine = SharedMemoryManagerEngine()
    with pytest.raises(ValueError, match="El arreglo de entrada no puede estar vacío."):
        engine.execute_shared_computation(np.array([], dtype=np.int64))

def test_process_shared_array_exception_branch():
    # Forzar un nombre de memoria inexistente para cubrir la excepción del bloque try-except
    res = process_shared_array("non_existent_shm_block_name_xyz", (2, 2), "int64")
    assert res["status"] == "FAILED"
    assert "error" in res