import pandas as pd
from typing import List

class DataFilterEngine:
    """Motor para procesar y aplicar filtros dinámicos sobre un DataFrame de Pandas."""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def filter_by_categories(self, column: str, selected_categories: List[str]) -> pd.DataFrame:
        """Filtra el DataFrame basado en una lista de categorías seleccionadas."""
        if not selected_categories:
            return self.df.copy()
        return self.df[self.df[column].isin(selected_categories)].copy()

    def filter_by_numeric_range(self, column: str, min_val: float, max_val: float) -> pd.DataFrame:
        """Filtra el DataFrame dentro de un rango numérico inclusivo."""
        return self.df[(self.df[column] >= min_val) & (self.df[column] <= max_val)].copy()

    def get_summary_metrics(self, filtered_df: pd.DataFrame, numeric_col: str) -> dict:
        """Calcula métricas resumen esenciales sobre el DataFrame filtrado."""
        if filtered_df.empty:
            return {"count": 0, "total": 0.0, "average": 0.0}
        
        return {
            "count": len(filtered_df),
            "total": float(filtered_df[numeric_col].sum()),
            "average": float(filtered_df[numeric_col].mean())
        }