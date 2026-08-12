import pytest
import numpy as np
from pathlib import Path
from src.detector import OutlierDetectionEngine

def test_load_data_success(tmp_path):
    """Valida la carga correcta de datos desde un CSV válido."""
    file_path = tmp_path / "test_metrics.csv"
    file_path.write_text("id,metric_value\n1,10.0\n2,20.0\n3,15.0", encoding="utf-8")

    engine = OutlierDetectionEngine(input_path=str(file_path))
    data = engine.load_data()
    assert isinstance(data, np.ndarray)
    assert len(data) == 3

def test_load_data_not_found():
    """Valida que lance FileNotFoundError si el archivo no existe."""
    engine = OutlierDetectionEngine(input_path="nonexistent.csv")
    with pytest.raises(FileNotFoundError):
        engine.load_data()

def test_load_data_invalid_column(tmp_path):
    """Valida que lance ValueError si falta la columna requerida."""
    file_path = tmp_path / "bad_metrics.csv"
    file_path.write_text("id,wrong_column\n1,10.0", encoding="utf-8")

    engine = OutlierDetectionEngine(input_path=str(file_path))
    with pytest.raises(ValueError):
        engine.load_data()

def test_detect_outliers_iqr():
    """Valida la detección correcta de outliers usando IQR."""
    data = np.array([10, 11, 12, 10, 11, 100]) # 100 es claramente un outlier
    engine = OutlierDetectionEngine()
    outliers = engine.detect_outliers_iqr(data)
    assert outliers[-1] == True
    assert not np.any(outliers[:-1])

def test_detect_outliers_zscore():
    """Valida la detección correcta de outliers usando Z-score."""
    data = np.array([10, 11, 12, 10, 11, 200])
    engine = OutlierDetectionEngine(threshold=2.0)
    outliers = engine.detect_outliers_zscore(data)
    assert outliers[-1] == True

def test_treat_outliers_iqr():
    """Valida el tratamiento y reemplazo de valores atípicos."""
    data = np.array([10, 11, 12, 10, 11, 100])
    engine = OutlierDetectionEngine()
    treated = engine.treat_outliers(data, method="iqr")
    assert treated[-1] != 100  # Fue reemplazado por la mediana

def test_treat_outliers_invalid_method():
    """Valida que lance ValueError al usar un método desconocido."""
    data = np.array([10, 11, 12])
    engine = OutlierDetectionEngine()
    with pytest.raises(ValueError):
        engine.treat_outliers(data, method="unknown")

def test_treat_outliers_invalid_method():
    """Valida que lance ValueError al usar un método desconocido."""
    data = np.array([10, 11, 12])
    engine = OutlierDetectionEngine()
    with pytest.raises(ValueError):
        engine.treat_outliers(data, method="unknown")

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