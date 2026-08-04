import json
from pathlib import Path
from pydantic import BaseModel, Field, EmailStr

# Definición exacta del esquema de respuesta del Gateway
class AnalyticsResponse(BaseModel):
    status: str
    processed_id: int
    message: str

def export_contract_artifact():
    # Instancia de ejemplo validada por el esquema de Pydantic
    mock_response = AnalyticsResponse(
        status="success",
        processed_id=1024,
        message="Payload validado e ingerido correctamente en el motor analítico."
    )
    
    # Ruta de salida dentro del directorio del módulo D60
    output_path = Path("gateway_response.json")
    
    # Serialización a JSON con formato legible (indentado)
    output_path.write_text(
        mock_response.model_dump_json(indent=4),
        encoding="utf-8"
    )
    print(f"[SUCCESS] Artefacto de contrato generado en: {output_path.resolve()}")

if __name__ == "__main__":
    export_contract_artifact()