import numpy as np
from scipy import stats
from typing import Dict, Any, Union, List

class DataDriftDetector:
    """Detector estadístico de deriva de datos (Data Drift) entre datasets de referencia y producción."""

    def __init__(self, significance_level: float = 0.05):
        self.significance_level = significance_level
        if not (0.0 < significance_level < 1.0):
            raise ValueError("El nivel de significancia debe estar entre 0.0 y 1.0.")

    def detect_drift(self, reference_data: Union[List[float], np.ndarray], production_data: Union[List[float], np.ndarray]) -> Dict[str, Any]:
        """Compara dos conjuntos de datos usando la prueba de Kolmogorov-Smirnov de dos muestras."""
        if reference_data is None or production_data is None:
            raise ValueError("Los datos de referencia y producción no pueden ser nulos.")
        
        ref_arr = np.array(reference_data)
        prod_arr = np.array(production_data)

        if len(ref_arr) == 0 or len(prod_arr) == 0:
            raise ValueError("Los conjuntos de datos no pueden estar vacíos.")

        # Ejecutar la prueba estadística de Kolmogorov-Smirnov
        ks_stat, p_value = stats.ks_2samp(ref_arr, prod_arr)

        # Si el p-value es menor que el nivel de significancia, se rechaza la hipótesis nula (hay drift)
        has_drift = bool(p_value < self.significance_level)

        return {
            "drift_detected": has_drift,
            "statistic": float(ks_stat),
            "p_value": float(p_value),
            "significance_level": self.significance_level
        }