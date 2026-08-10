import jsonschema
from jsonschema import validate, ValidationError
from typing import Dict, Any, Tuple

class DataContractValidator:
    def __init__(self, schema: Dict[str, Any]):
        self.schema = schema

    def validate_payload(self, payload: Dict[str, Any]) -> Tuple[bool, str]:
        """Valida una carga útil contra el esquema definido.
        Retorna una tupla (es_valido, mensaje_de_error).
        """
        try:
            validate(instance=payload, schema=self.schema)
            return True, "Validación exitosa"
        except ValidationError as e:
            return False, e.message