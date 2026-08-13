import pandas as pd
import numpy as np
from typing import Dict, Any

class AdvancedWindowProcessor:
    """Procesador de operaciones avanzadas de ventanas deslizantes (rolling) vectorizadas con Pandas."""
    
    def __init__(self, data: pd.DataFrame):
        self.df = data.copy()

    def compute_advanced_metrics(self, window_size: int = 3) -> pd.DataFrame:
        """Calcula métricas estadísticas pesadas en memoria usando rolling de Pandas de forma vectorizada."""
        if self.df.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
        
        result_df = pd.DataFrame(index=self.df.index)
        
        for col in self.df.select_dtypes(include=[np.number]).columns:
            # Ventana deslizante para la media móvil
            result_df[f"{col}_rolling_mean"] = self.df[col].rolling(window=window_size, min_periods=1).mean()
            # Ventana deslizante para la desviación estándar ponderada
            result_df[f"{col}_rolling_std"] = self.df[col].rolling(window=window_size, min_periods=1).std().fillna(0.0)
            # Z-Score enrollado optimizado vectorialmente
            mean_series = result_df[f"{col}_rolling_mean"]
            std_series = result_df[f"{col}_rolling_std"]
            
            # Evitar división por cero si la desviación estándar es cero
            safe_std = np.where(std_series == 0, 1e-8, std_series)
            result_df[f"{col}_rolling_zscore"] = (self.df[col] - mean_series) / safe_std
            
        return result_df