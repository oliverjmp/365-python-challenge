import pytest
import pyarrow as pa
from src.schema_evolution import SchemaEvolutionManager

def test_schema_evolution_integration(tmp_path):
    """Verifica que los lotes con diferentes esquemas se unifiquen correctamente rellenando nulos."""
    manager = SchemaEvolutionManager(dataset_dir=str(tmp_path))

    manager.guardar_lote_inicial("lote_1.parquet")
    manager.guardar_lote_evolucionado("lote_2.parquet")

    tabla = manager.leer_dataset_unificado()

    assert tabla.num_rows == 5
    assert "limite_credito" in tabla.column_names
    assert "pais" in tabla.column_names

    df_resultado = tabla.to_pandas()
    filas_lote_1 = df_resultado[df_resultado["cliente_id"].isin([1, 2, 3])]
    
    assert filas_lote_1["limite_credito"].isna().all()
    assert filas_lote_1["pais"].isna().all()

    filas_lote_2 = df_resultado[df_resultado["cliente_id"].isin([4, 5])]
    assert not filas_lote_2["limite_credito"].isna().any()
    assert list(filas_lote_2["pais"]) == ["España", "México"]

def test_directorio_vacio_lanza_error(tmp_path):
    """Verifica que se lance FileNotFoundError si el directorio de datos está vacío."""
    manager = SchemaEvolutionManager(dataset_dir=str(tmp_path))
    with pytest.raises(FileNotFoundError):
        manager.leer_dataset_unificado()