import pytest
from src.mmap_engine import MemoryMappedFileProcessor

def test_mmap_busqueda_con_metricas(tmp_path):
    bin_file = tmp_path / "data_lake" / "test_records.bin"
    processor = MemoryMappedFileProcessor(file_path=str(bin_file))
    
    with open(bin_file, "wb") as f:
        f.write(b"SAMPLE_DATA_BLOCK_ONE_SAMPLE_DATA_BLOCK_TWO")
        
    resultado = processor.buscar_patron_con_metricas(b"DATA")
    
    assert len(resultado["coincidencias"]) == 2
    assert resultado["duracion_ms"] >= 0.0
    assert resultado["tamano_archivo_bytes"] > 0

def test_archivo_no_encontrado_lanza_error():
    processor = MemoryMappedFileProcessor(file_path="ruta/inexistente/file.bin")
    import os
    if os.path.exists("ruta/inexistente/file.bin"):
        os.remove("ruta/inexistente/file.bin")
        
    with pytest.raises(FileNotFoundError):
        processor.buscar_patron_con_metricas(b"TEST")