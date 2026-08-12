import numpy as np
from scipy import stats
import pandas as pd
from pathlib import Path

class OutlierDetectionEngine:
    def __init__(self, input_path: str = "data/metrics.csv", threshold: float = 3.0):
        self.input_path = Path(input_path)
        self.threshold = threshold

    def load_data(self) -> np.ndarray:
        """Carga los datos numéricos desde un archivo CSV usando pandas y los convierte a un array de NumPy."""
        if not self.input_path.exists():
            raise FileNotFoundError(f"El archivo no existe: {self.input_path}")
        df = pd.read_csv(self.input_path)
        if "metric_value" not in df.columns:
            raise ValueError("El archivo CSV debe contener la columna 'metric_value'")
        return df["metric_value"].to_numpy(dtype=float)

    def detect_outliers_zscore(self, data: np.ndarray) -> np.ndarray:
        """Detecta outliers utilizando Z-score de SciPy (valores que superan el umbral)."""
        z_scores = np.abs(stats.zscore(data))
        return z_scores > self.threshold

    def detect_outliers_iqr(self, data: np.ndarray) -> np.ndarray:
        """Detecta outliers utilizando el método del Rango Intercuartílico (IQR) con NumPy."""
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        return (data < lower_bound) | (data > upper_bound)

    def treat_outliers(self, data: np.ndarray, method: str = "iqr") -> np.ndarray:
        """Trata los outliers reemplazándolos por la mediana de los datos limpios."""
        if method == "iqr":
            outliers = self.detect_outliers_iqr(data)
        elif method == "zscore":
            outliers = self.detect_outliers_zscore(data)
        else:
            raise ValueError("Método no soportado. Usa 'iqr' o 'zscore'.")

        treated_data = data.copy()
        if np.any(outliers):
            median_val = np.median(treated_data[~outliers])
            treated_data[outliers] = median_val

        return treated_data