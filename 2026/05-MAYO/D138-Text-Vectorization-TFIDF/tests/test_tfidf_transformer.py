import pytest
import numpy as np
from src.tfidf_transformer import TextTfidfVectorizer

def test_empty_corpus_fit_raises_error():
    """Valida que un corpus vacío o inválido al ajustar lance un ValueError."""
    transformer = TextTfidfVectorizer()
    with pytest.raises(ValueError, match="debe ser una lista no vacía"):
        transformer.fit_transform([])

def test_invalid_type_corpus_raises_error():
    """Valida que elementos que no sean strings lancen un TypeError."""
    transformer = TextTfidfVectorizer()
    with pytest.raises(TypeError, match="deben ser cadenas de texto"):
        transformer.fit_transform(["Texto válido", 12345])

def test_transform_without_fit_raises_error():
    """Valida que intentar transformar sin haber ajustado el modelo lance un RuntimeError."""
    transformer = TextTfidfVectorizer()
    with pytest.raises(RuntimeError, match="debe ser ajustado"):
        transformer.transform(["Nuevo texto"])

def test_get_feature_names_without_fit_raises_error():
    """Valida que obtener nombres de características sin ajustar lance un RuntimeError."""
    transformer = TextTfidfVectorizer()
    with pytest.raises(RuntimeError, match="debe ser ajustado"):
        transformer.get_feature_names()

def test_empty_corpus_transform_raises_error():
    """Valida que transformar un corpus vacío posterior al ajuste lance un ValueError."""
    transformer = TextTfidfVectorizer()
    transformer.fit_transform(["Texto inicial de prueba"])
    with pytest.raises(ValueError, match="debe ser una lista no vacía"):
        transformer.transform([])

def test_invalid_type_transform_raises_error():
    """Valida que transformar elementos que no sean strings lance un TypeError."""
    transformer = TextTfidfVectorizer()
    transformer.fit_transform(["Texto inicial de prueba"])
    with pytest.raises(TypeError, match="deben ser cadenas de texto"):
        transformer.transform(["Texto", None])

def test_tfidf_vectorization_success():
    """Valida el flujo completo exitoso: fit_transform, transform y extracción de características."""
    corpus = [
        "Machine learning y ciencia de datos",
        "Procesamiento de lenguaje natural con python",
        "Machine learning avanzado y modelos predictivos"
    ]

    transformer = TextTfidfVectorizer(ngram_range=(1, 2))
    matrix = transformer.fit_transform(corpus)

    assert isinstance(matrix, np.ndarray)
    assert matrix.shape[0] == 3

    features = transformer.get_feature_names()
    assert len(features) > 0
    assert "machine learning" in features

    # Probar transformación de un nuevo documento
    new_doc = ["Python para ciencia de datos"]
    new_matrix = transformer.transform(new_doc)
    assert new_matrix.shape == (1, len(features))