from typing import List, Dict, Any

class DataContractValidator:
    def __init__(self, schema: Dict[str, Dict[str, Any]]):
        """Define el contrato de datos con las reglas esperadas por columna."""
        self.schema = schema

    def validate_record(self, record: Dict[str, Any]) -> List[str]:
        """Valida un registro individual contra el contrato de datos y devuelve los errores encontrados."""
        errors = []
        for column, rules in self.schema.items():
            if column not in record:
                if not rules.get("nullable", True):
                    errors.append(f"La columna obligatoria '{column}' está ausente.")
                continue

            value = record[column]

            # Validación de nulos
            if value is None:
                if not rules.get("nullable", True):
                    errors.append(f"La columna '{column}' no permite valores nulos.")
                continue

            # Validación de tipos
            expected_type = rules.get("type")
            if expected_type and not isinstance(value, expected_type):
                errors.append(f"La columna '{column}' esperaba tipo {expected_type.__name__}, pero recibió {type(value).__name__}.")

        return errors

    def validate_batch(self, batch: List[Dict[str, Any]]) -> Dict[int, List[str]]:
        """Valida un lote completo de registros y retorna un diccionario con los errores por índice de fila."""
        batch_errors = {}
        for index, record in enumerate(batch):
            errors = self.validate_record(record)
            if errors:
                batch_errors[index] = errors
        return batch_errors