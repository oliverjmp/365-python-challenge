import pytest
from src.fts_engine import DuckDBFTSEngine

def test_fts_busqueda_exitosa(tmp_path):
    db_file = tmp_path / "data_lake" / "test_logs.db"
    engine = DuckDBFTSEngine(db_path=str(db_file))
    
    resultado = engine.buscar_logs("connection")
    
    assert isinstance(resultado, dict)
    assert resultado["termino"] == "connection"
    assert len(resultado["filas"]) > 0
    assert resultado["duracion_ms"] >= 0.0

def test_base_no_encontrada_lanza_error():
    engine = DuckDBFTSEngine(db_path="ruta/inexistente/logs.db")
    import os
    if os.path.exists("ruta/inexistente/logs.db"):
        os.remove("ruta/inexistente/logs.db")
        
    with pytest.raises(FileNotFoundError):
        engine.buscar_logs("test")