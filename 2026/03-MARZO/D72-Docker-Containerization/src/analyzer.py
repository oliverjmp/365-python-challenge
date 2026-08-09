import pandas as pd

class AnalyticsMicroservice:
    """Microservicio analítico para procesamiento de datos."""

    def process_data(self, data: list) -> pd.DataFrame:
        """Convierte una lista de diccionarios en un DataFrame y calcula estadísticas básicas."""
        df = pd.DataFrame(data)
        if df.empty:
            return df
        
        # Ejemplo analítico: normalizar texto y calcular métrica
        if "category" in df.columns:
            df["category"] = df["category"].str.strip().str.upper()
            
        return df