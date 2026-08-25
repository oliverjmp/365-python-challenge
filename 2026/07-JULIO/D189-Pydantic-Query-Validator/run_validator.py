import logging
from pydantic import ValidationError
from src.query_validator import AnalyticsQuerySchema

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def ejecutar_demostracion_validador():
    print("==================================================================")
    print("   D189 - VALIDADOR ESTRICTO DE CONSULTAS (PYDANTIC V2 + SQL)    ")
    print("==================================================================\n")

    # Caso 1: Payload Legítimo y Correcto
    print("[1/3] Probando consulta analítica legítima...")
    payload_valido = {
        "metric": "conversion_rate_q2",
        "start_date": "2026-04-01",
        "end_date": "2026-06-30",
        "filters": ["region_latam", "channel_direct"],
        "limit": 250
    }
    
    try:
        query_valida = AnalyticsQuerySchema(**payload_valido)
        print(" > Estado: ✅ APROBADO")
        print(f" > Datos Sanitizados y Tipados: {query_valida.model_dump()}\n")
    except ValidationError as e:
        print(f" > Error inesperado: {e}\n")

    # Caso 2: Intento de Inyección SQL (Tautología en Filtros)
    print("[2/3] Simulando ataque malicioso (Tautología SQL: OR 1=1)...")
    payload_ataque_1 = {
        "metric": "active_users",
        "start_date": "2026-01-01",
        "end_date": "2026-03-31",
        "filters": ["country = 'ES' OR 1=1"]
    }
    
    try:
        AnalyticsQuerySchema(**payload_ataque_1)
    except ValidationError as e:
        print(" > Estado: 🛡️ BLOQUEADO EXITOSAMENTE POR PYZANTIC")
        print(f" > Detalle de la Alerta:\n{e}\n")

    # Caso 3: Intento de Inyección SQL (DROP TABLE destructivo en Métrica)
    print("[3/3] Simulando ataque malicioso crítico (DROP TABLE en Métrica)...")
    payload_ataque_2 = {
        "metric": "sales; DROP TABLE analytics_db; --",
        "start_date": "2026-01-01",
        "end_date": "2026-03-31"
    }
    
    try:
        AnalyticsQuerySchema(**payload_ataque_2)
    except ValidationError as e:
        print(" > Estado: 🛡️ BLOQUEADO EXITOSAMENTE POR PYZANTIC")
        print(f" > Detalle de la Alerta:\n{e}\n")

    print("==================================================================")
    print("       ¡DEMOSTRACIÓN DE SEGURIDAD FINALIZADA CON ÉXITO!           ")
    print("==================================================================")

if __name__ == "__main__":
    ejecutar_demostracion_validador()