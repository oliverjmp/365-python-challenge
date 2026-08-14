import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Union, Dict, Any

class TextTfidfVectorizer:
    """Clase envoltorio para vectorizar corpus de texto utilizando TF-IDF de Scikit-learn."""

    def __init__(self, max_features: Union[int, None] = None, ngram_range: tuple = (1, 1), **kwargs):
        self.max_features = max_features
        self.ngram_range = ngram_range
        self.kwargs = kwargs
        
        self.vectorizer = TfidfVectorizer(
            max_features=self.max_features,
            ngram_range=self.ngram_range,
            **self.kwargs
        )
        self.is_fitted = False

    def fit_transform(self, corpus: List[str]) -> np.ndarray:
        """Ajusta el vectorizador al corpus y transforma el texto en una matriz numérica dispersa (o densa)."""
        if not corpus or not isinstance(corpus, list):
            raise ValueError("El corpus de texto debe ser una lista no vacía de cadenas de caracteres.")
        
        # Validar que todos los elementos sean strings
        if not all(isinstance(doc, str) for doc in corpus):
            raise TypeError("Todos los elementos del corpus deben ser cadenas de texto (str).")

        sparse_matrix = self.vectorizer.fit_transform(corpus)
        self.is_fitted = True
        return sparse_matrix.toarray()

    def transform(self, corpus: List[str]) -> np.ndarray:
        """Transforma un nuevo corpus utilizando el vocabulario ya ajustado."""
        if not self.is_fitted:
            raise RuntimeError("El vectorizador debe ser ajustado (fit) antes de transformar nuevos textos.")
        if not corpus or not isinstance(corpus, list):
            raise ValueError("El corpus de texto debe ser una lista no vacía de cadenas de caracteres.")
        if not all(isinstance(doc, str) for doc in corpus):
            raise TypeError("Todos los elementos del corpus deben ser cadenas de texto (str).")

        sparse_matrix = self.vectorizer.transform(corpus)
        return sparse_matrix.toarray()

    def get_feature_names(self) -> List[str]:
        """Retorna la lista de términos (vocabulario) extraídos del corpus."""
        if not self.is_fitted:
            raise RuntimeError("El vectorizador debe ser ajustado antes de obtener las características.")
        return self.vectorizer.get_feature_names_out().tolist()