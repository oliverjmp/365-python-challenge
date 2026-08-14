import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from typing import Union, Dict, Any, Optional

class DecisionTreeEngine:
    """Motor de clasificación basado en Árboles de Decisión con optimización de criterios y profundidad."""
    
    def __init__(self, criterion: str = "gini", max_depth: Optional[int] = None, **kwargs: Any):
        self.criterion = criterion
        self.max_depth = max_depth
        self.model = DecisionTreeClassifier(criterion=self.criterion, max_depth=self.max_depth, **kwargs)
        self.is_fitted = False
        self.feature_names: Optional[list] = None
        self.class_names: Optional[list] = None

    def fit(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray]) -> None:
        """Ajusta el árbol de decisión con los datos de entrenamiento."""
        if isinstance(X, pd.DataFrame):
            if X.empty:
                raise ValueError("El DataFrame de características X está vacío.")
            self.feature_names = [str(col) for col in X.columns]
        else:
            if len(X) == 0:
                raise ValueError("El conjunto de características X está vacío.")
            self.feature_names = [f"feature_{i}" for i in range(np.array(X).shape[1])]
            
        if len(X) == 0 or len(y) == 0:
            raise ValueError("Los datos de entrenamiento no pueden estar vacíos.")
            
        if isinstance(y, (pd.Series, np.ndarray)):
            unique_classes = np.unique(y)
            self.class_names = [str(c) for c in unique_classes]

        self.model.fit(X, y)
        self.is_fitted = True

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Realiza predicciones de clase para nuevas muestras."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser ajustado (fit) antes de realizar predicciones.")
        if isinstance(X, pd.DataFrame) and X.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
        if not isinstance(X, pd.DataFrame) and len(X) == 0:
            raise ValueError("El arreglo de entrada está vacío.")
            
        return self.model.predict(X)

    def predict_proba(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Estima las probabilidades asociadas a cada clase."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser ajustado (fit) antes de estimar probabilidades.")
        if isinstance(X, pd.DataFrame) and X.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
        if not isinstance(X, pd.DataFrame) and len(X) == 0:
            raise ValueError("El arreglo de entrada está vacío.")
            
        return self.model.predict_proba(X)

    def export_tree_dot(self) -> str:
        """Exporta la estructura del árbol de decisión en formato DOT para visualización."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser ajustado antes de exportar la estructura del árbol.")
            
        return export_graphviz(
            self.model,
            out_file=None,
            feature_names=self.feature_names,
            class_names=self.class_names,
            filled=True,
            rounded=True,
            special_characters=True
        )

    @property
    def feature_importances(self) -> np.ndarray:
        """Retorna la importancia de cada característica calculada por el árbol."""
        if not self.is_fitted:
            raise ValueError("El modelo no ha sido ajustado todavía.")
        return self.model.feature_importances_