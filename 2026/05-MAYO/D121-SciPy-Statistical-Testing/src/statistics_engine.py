import numpy as np
from scipy import stats
from typing import Dict, Any, List

class BusinessStatisticalEngine:
    """Motor de análisis estadístico y pruebas de hipótesis para datasets de negocio."""
    
    def __init__(self, alpha: float = 0.05):
        self.alpha = alpha

    def perform_anova(self, groups: List[List[float]]) -> Dict[str, Any]:
        """Realiza una prueba ANOVA de una vía para comparar medias entre múltiples grupos (ej. rendimiento de campañas de marketing)."""
        f_stat, p_value = stats.f_oneway(*groups)
        reject_null = p_value < self.alpha
        
        return {
            "test": "ANOVA",
            "statistic": float(f_stat),
            "p_value": float(p_value),
            "reject_null": bool(reject_null),
            "interpretation": "Existen diferencias significativas entre los grupos analizados." if reject_null else "No se aprecian diferencias estadísticamente significativas."
        }

    def perform_chi_square(self, contingency_table: List[List[int]]) -> Dict[str, Any]:
        """Realiza una prueba de Chi-cuadrado de independencia (ej. relación entre tipo de cliente y preferencia de producto)."""
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        reject_null = p_value < self.alpha
        
        return {
            "test": "Chi-Square",
            "statistic": float(chi2),
            "p_value": float(p_value),
            "degrees_of_freedom": int(dof),
            "reject_null": bool(reject_null),
            "interpretation": "Las variables son dependientes (existe asociación significativa)." if reject_null else "Las variables son independientes (no hay asociación significativa)."
        }