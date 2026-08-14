import pytest
import numpy as np
from src.nb_text_classifier import NaiveBayesTextClassifier

def test_empty_inputs_fit_raises_error():
    """Valida que entradas vacías al ajustar lancen un ValueError."""
    clf = NaiveBayesTextClassifier()
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        clf.fit([], [])

def test_mismatched_lengths_raises_error():
    """Valida que longitudes desiguales entre textos y etiquetas lancen un ValueError."""
    clf = NaiveBayesTextClassifier()
    with pytest.raises(ValueError, match="debe coincidir exactamente"):
        clf.fit(["Texto 1"], ["Etiqueta 1", "Etiqueta 2"])

def test_invalid_text_type_raises_error():
    """Valida que elementos que no sean strings en el ajuste lancen un TypeError."""
    clf = NaiveBayesTextClassifier()
    with pytest.raises(TypeError, match="deben ser cadenas de texto"):
        clf.fit([12345], ["Etiqueta"])

def test_predict_without_fit_raises_error():
    """Valida que predecir sin ajustar lance un RuntimeError."""
    clf = NaiveBayesTextClassifier()
    with pytest.raises(RuntimeError, match="debe ser ajustado"):
        clf.predict(["Texto de prueba"])

def test_predict_proba_without_fit_raises_error():
    """Valida que calcular probabilidades sin ajustar lance un RuntimeError."""
    clf = NaiveBayesTextClassifier()
    with pytest.raises(RuntimeError, match="debe ser ajustado"):
        clf.predict_proba(["Texto de prueba"])

def test_empty_predict_input_raises_error():
    """Valida que predecir con una lista vacía lance un ValueError."""
    clf = NaiveBayesTextClassifier()
    clf.fit(["Entrenamiento de prueba"], ["ClaseA"])
    with pytest.raises(ValueError, match="debe ser una lista no vacía"):
        clf.predict([])

def test_invalid_predict_type_raises_error():
    """Valida que predecir elementos que no sean strings lance un TypeError."""
    clf = NaiveBayesTextClassifier()
    clf.fit(["Entrenamiento de prueba"], ["ClaseA"])
    with pytest.raises(TypeError, match="deben ser cadenas de texto"):
        clf.predict([999])

def test_empty_predict_proba_input_raises_error():
    """Valida que calcular probabilidades con una lista vacía lance un ValueError."""
    clf = NaiveBayesTextClassifier()
    clf.fit(["Entrenamiento de prueba"], ["ClaseA"])
    with pytest.raises(ValueError, match="debe ser una lista no vacía"):
        clf.predict_proba([])

def test_invalid_predict_proba_type_raises_error():
    """Valida que calcular probabilidades con elementos que no sean strings lance un TypeError."""
    clf = NaiveBayesTextClassifier()
    clf.fit(["Entrenamiento de prueba"], ["ClaseA"])
    with pytest.raises(TypeError, match="deben ser cadenas de texto"):
        clf.predict_proba([999])

def test_naive_bayes_classifier_success():
    """Valida el flujo completo exitoso: entrenamiento, predicción y cálculo de probabilidades."""
    train_texts = [
        "Python es un lenguaje de programación excelente para ciencia de datos",
        "Machine learning y algoritmos de inteligencia artificial avanzados",
        "El partido de futbol terminó con victoria del equipo local",
        "La final del campeonato de deportes estuvo emocionante"
    ]
    train_labels = ["Tecnología", "Tecnología", "Deportes", "Deportes"]

    classifier = NaiveBayesTextClassifier(alpha=1.0)
    classifier.fit(train_texts, train_labels)

    # Prueba de predicción
    test_texts = [
        "Programación en python para machine learning",
        "Marcador final del partido de futbol"
    ]
    predictions = classifier.predict(test_texts)
    
    assert len(predictions) == 2
    assert predictions[0] == "Tecnología"
    assert predictions[1] == "Deportes"

    # Prueba de probabilidades
    probabilities = classifier.predict_proba(test_texts)
    assert isinstance(probabilities, np.ndarray)
    assert probabilities.shape[0] == 2