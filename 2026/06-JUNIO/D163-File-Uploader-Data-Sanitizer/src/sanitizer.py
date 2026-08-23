import pandas as pd
from pydantic import ValidationError
from src.validator import RecordSchema

def sanitize_and_validate_dataframe(df: pd.DataFrame):
    """
    Procesa un DataFrame fila por fila validándolo contra el esquema de Pydantic.
    Retorna los registros válidos y un listado de errores detallados.
    """
    valid_records = []
    errors = []

    for index, row in df.iterrows():
        try:
            # Convertimos la fila a diccionario y validamos con Pydantic
            record_dict = row.to_dict()
            validated = RecordSchema(**record_dict)
            valid_records.append(validated.model_dump())
        except ValidationError as e:
            for err in e.errors():
                errors.append({
                    "row": index + 1,
                    "field": err["loc"][0],
                    "error": err["msg"]
                })
        except Exception as e:
            errors.append({
                "row": index + 1,
                "field": "general",
                "error": str(e)
            })

    return pd.DataFrame(valid_records) if valid_records else pd.DataFrame(), errors