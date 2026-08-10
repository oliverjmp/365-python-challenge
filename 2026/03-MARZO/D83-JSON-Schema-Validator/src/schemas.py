# Esquema JSON formal para validar registros de eventos o usuarios
USER_EVENT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "event_id": {"type": "string"},
        "username": {"type": "string", "minLength": 3, "maxLength": 50},
        "age": {"type": "integer", "minimum": 18, "maximum": 120},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["event_id", "username", "age", "email"],
    "additionalProperties": False
}