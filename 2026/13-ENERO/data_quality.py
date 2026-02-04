import pandas as pd
import json
import logging
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------
# CONFIGURACIÓN DE LOGGING
# ---------------------------------------------------------
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "data_quality.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------------------------------------------
# CARGA DE REGLAS
# ---------------------------------------------------------
def load_rules(path="rules.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# ---------------------------------------------------------
# VALIDACIONES
# ---------------------------------------------------------
def check_required_columns(df, rules):
    missing = [col for col in rules["required_columns"] if col not in df.columns]
    if missing:
        logging.error(f"Columnas faltantes: {missing}")
        return False
    return True

def check_column_types(df, rules):
    for col, expected_type in rules["column_types"].items():
        if col not in df.columns:
            continue

        try:
            if expected_type == "datetime":
                pd.to_datetime(df[col])
            elif expected_type == "int":
                df[col].astype(int)
            elif expected_type == "float":
                df[col].astype(float)
        except Exception:
            logging.error(f"Tipo incorrecto en columna '{col}'. Se esperaba {expected_type}.")
            return False

    return True

def check_nulls(df):
    nulls = df.isnull().sum()
    problematic = nulls[nulls > 0]

    if not problematic.empty:
        logging.warning(f"Valores nulos detectados:\n{problematic}")
        return False

    return True

def check_duplicates(df):
    if df.duplicated().sum() > 0:
        logging.warning("Duplicados detectados en el dataset.")
        return False
    return True

def check_ranges(df, rules):
    if "range_rules" not in rules:
        return True

    for col, limits in rules["range_rules"].items():
        if col not in df.columns:
            continue

        min_val = limits.get("min")
        max_val = limits.get("max")

        if min_val is not None and (df[col] < min_val).any():
            logging.error(f"Valores menores al mínimo permitido en '{col}'.")
            return False

        if max_val is not None and (df[col] > max_val).any():
            logging.error(f"Valores mayores al máximo permitido en '{col}'.")
            return False

    return True

# ---------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ---------------------------------------------------------
def validar_dataset(path_csv, rules_path="rules.json"):
    logging.info(f"Validando dataset: {path_csv}")

    try:
        df = pd.read_csv(path_csv)
    except Exception as e:
        logging.critical(f"No se pudo leer el archivo: {e}")
        return False

    rules = load_rules(rules_path)

    checks = [
        check_required_columns(df, rules),
        check_column_types(df, rules),
        check_nulls(df),
        check_duplicates(df),
        check_ranges(df, rules)
    ]

    if all(checks):
        logging.info("VALIDACIÓN COMPLETA: El dataset es válido.")
        return True
    else:
        logging.error("VALIDACIÓN FALLIDA: El dataset contiene errores.")
        return False

# ---------------------------------------------------------
# EJEMPLO DE USO
# ---------------------------------------------------------
if __name__ == "__main__":
    resultado = validar_dataset("data.csv")
    print("¿Dataset válido?:", resultado)
