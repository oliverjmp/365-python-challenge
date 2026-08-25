import pytest
from src.lineage_engine import DataLineageTracker

def test_lineage_inicializacion_y_carga(tmp_path):
    dl_dir = tmp_path / "data_lake"
    meta_file = tmp_path / "data_lake" / "lineage_metadata.json"
    
    tracker = DataLineageTracker(data_lake_dir=str(dl_dir), metadata_path=str(meta_file))
    lineage = tracker.obtener_linaje()
    
    assert "nodes" in lineage
    assert "edges" in lineage
    assert len(lineage["nodes"]) == 2

def test_registrar_transformacion(tmp_path):
    dl_dir = tmp_path / "data_lake"
    meta_file = tmp_path / "data_lake" / "lineage_metadata.json"
    
    tracker = DataLineageTracker(data_lake_dir=str(dl_dir), metadata_path=str(meta_file))
    
    # Registrar relación adicional
    resultado = tracker.registrar_transformacion("raw_data.parquet", "processed_data.parquet", "Test Transformation")
    assert resultado is True
    
    lineage = tracker.obtener_linaje()
    assert len(lineage["edges"]) >= 1