import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from typing import List, Union

class NaiveBayesTextClassifier:
    """Clasificador de textos basado en Multinomial Naive Bayes y vectorización TF-IDF integrados en un Pipeline."""

    def __init__(self, alpha: float = 1.0, ngram_range: tuple = (1, 1)):
        self.alpha = alpha
        self.ngram_range = ngram_range
        
        # Pipeline que une la vectorización TF-IDF con el clasificador Multinomial Naive Bayes
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=self.ngram_range)),
            ('clf', MultinomialNB(alpha=self.alpha))
        ])
        self.is_fitted = False

    def fit(self, texts: List[str], labels: List[Union[str, int]]) -> None:
        """Ajusta el modelo de clasificación con el corpus de entrenamiento y sus respectivas etiquetas."""
        if not texts or not labels:
            raise ValueError("Los textos y las etiquetas de entrenamiento no pueden estar vacíos.")
        if len(texts) != len(labels):
            raise ValueError("El número de textos debe coincidir exactamente con el número de etiquetas.")
        if not all(isinstance(t, str) for t in texts):
            raise TypeError("Todos los elementos del corpus deben ser cadenas de texto (str).")

        self.pipeline.fit(texts, labels)
        self.is_fitted = True

    def predict(self, texts: List[str]) -> np.ndarray:
        """Predice las etiquetas para una lista de nuevos textos."""
        if not self.is_fitted:
            raise RuntimeError("El clasificador debe ser ajustado (fit) antes de realizar predicciones.")
        if not texts or not isinstance(texts, list):
            raise ValueError("El corpus de texto a predecir debe ser una lista no vacía.")
        if not all(isinstance(t, str) for t in texts):
            raise TypeError("Todos los elementos a predecir deben ser cadenas de texto (str).")

        return self.pipeline.predict(texts)

    def predict_proba(self, texts: List[str]) -> np.ndarray:
        """Calcula las probabilidades de predicción para cada clase en los textos dados."""
        if not self.is_fitted:
            raise RuntimeError("El clasificador debe ser ajustado antes de calcular probabilidades.")
        if not texts or not isinstance(texts, list):
            raise ValueError("El corpus de texto debe ser una lista no vacía.")
        if not all(isinstance(t, str) for t in texts):
            raise TypeError("Todos los elementos deben ser cadenas de texto (str).")

        return self.pipeline.predict_proba(texts)