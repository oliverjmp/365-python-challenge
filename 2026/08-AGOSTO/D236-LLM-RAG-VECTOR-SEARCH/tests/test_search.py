import pytest
from src.semantic_search import VectorSearchEngine

def test_build_empty_corpus_raises_error():
    engine = VectorSearchEngine()
    with pytest.raises(ValueError, match="no puede estar vacío"):
        engine.build_index([])

def test_search_unfitted_raises_error():
    engine = VectorSearchEngine()
    with pytest.raises(ValueError, match="no ha sido construido"):
        engine.search("busqueda de prueba")

def test_build_and_search_success():
    engine = VectorSearchEngine(embedding_dim=16)
    corpus = [
        {"id": "DOC-001", "text": "Reporte financiero consolidado Q1"},
        {"id": "DOC-002", "text": "Archivo de Análisis de Datos de comportamiento de usuarios"},
        {"id": "DOC-003", "text": "Minuta de la junta directiva corporativa"}
    ]
    
    engine.build_index(corpus)
    assert engine.is_fitted is True
    assert engine.index.ntotal == 3
    
    df_results = engine.search("Análisis de Datos", top_k=2)
    assert not df_results.empty
    assert len(df_results) == 2
    assert "distance_l2" in df_results.columns
    assert "text" in df_results.columns