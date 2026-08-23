import pandas as pd

def process_analytics_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza una limpieza y transformación básica sobre los datos analíticos de entrada.
    """
    if df.empty:
        return df
    
    # Rellenar valores nulos y estandarizar columnas numéricas si existen
    df_clean = df.copy()
    for col in df_clean.select_dtypes(include=['number']).columns:
        df_clean[col] = df_clean[col].fillna(0)
        
    return df_clean