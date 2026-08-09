import csv
from typing import Generator, Dict, Any

def stream_csv_rows(file_path: str) -> Generator[Dict[str, Any], None, None]:
    """Generador que lee un archivo CSV línea por línea para optimizar la memoria RAM."""
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def filter_high_values(rows: Generator[Dict[str, Any], None, None], threshold: float) -> Generator[Dict[str, Any], None, None]:
    """Generador secundario que filtra filas cuyo valor supere un umbral específico."""
    for row in rows:
        # Suponemos que la columna de interés se llama 'value'
        if float(row.get("value", 0)) > threshold:
            yield row