import pandas as pd
from pathlib import Path

class DataCleaningPipeline:
    def __init__(self, input_path: str = "data/raw_data.csv"):
        self.input_path = Path(input_path)

    def load_data(self) -> pd.DataFrame:
        """Carga el archivo CSV de origen."""
        if not self.input_path.exists():
            raise FileNotFoundError(f"El archivo no existe: {self.input_path}")
        return pd.read_csv(self.input_path)

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aplica operaciones vectorizadas de limpieza y tratamiento de nulos."""
        cleaned_df = df.copy()

        # Tratamiento vectorizado para columnas numéricas (rellenar nulos con la mediana o 0)
        if "price" in cleaned_df.columns:
            cleaned_df["price"] = cleaned_df["price"].fillna(cleaned_df["price"].median())
        
        if "stock" in cleaned_df.columns:
            cleaned_df["stock"] = cleaned_df["stock"].fillna(0).astype(int)

        # Tratamiento vectorizado para columnas de texto/categorías (rellenar con 'Unknown')
        if "category" in cleaned_df.columns:
            cleaned_df["category"] = cleaned_df["category"].fillna("Unknown")

        if "product" in cleaned_df.columns:
            cleaned_df["product"] = cleaned_df["product"].fillna("Unnamed Product")

        return cleaned_df

    def run_pipeline(self) -> pd.DataFrame:
        """Ejecuta el flujo completo de carga y limpieza."""
        raw_df = self.load_data()
        cleaned_df = self.clean_data(raw_df)
        return cleaned_df