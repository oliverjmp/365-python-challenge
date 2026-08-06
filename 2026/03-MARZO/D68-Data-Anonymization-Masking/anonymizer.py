import logging
import re
from typing import Dict, Any
import pandas as pd
from faker import Faker

# Configuración de logging estructurado corporativo
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] DataAnonymizationEngine - %(message)s",
)
logger = logging.getLogger("DataAnonymizationEngine")

class PIIAnonymizer:
    """Motor de enmascaramiento y anonimización de PII en DataFrames de Pandas mediante RegEx."""
    
    def __init__(self) -> None:
        # Expresiones regulares estandarizadas para detección de PII
        self.patterns: Dict[str, str] = {
            "email": r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",
            "phone": r"(\+?\d{1,3}[\s-]?)?(\d{2,4}[\s-]?\d{3,4}[\s-]?\d{3,4})",
            "credit_card": r"\b(?:\d[ -]*?){13,16}\b",
            "dni_nie": r"\b[0-9]{8}[A-Z]\b|\b[XYZ][0-9]{7}[A-Z]\b"
        }

    def mask_email(self, email: str) -> str:
        """Enmascara un correo electrónico conservando la primera letra y el dominio."""
        if not isinstance(email, str):
            return email
        match = re.match(self.patterns["email"], email)
        if match:
            username, domain = match.groups()
            masked_user = username[0] + "***" if len(username) > 1 else "***"
            return f"{masked_user}@{domain}"
        return "***@***.com"

    def mask_phone(self, phone: str) -> str:
        """Enmascara un número telefónico mostrando solo los últimos 4 dígitos."""
        if not isinstance(phone, str):
            return phone
        clean_phone = re.sub(r"\D", "", phone)
        if len(clean_phone) >= 4:
            return f"***-***-{clean_phone[-4:]}"
        return "***-***-****"

    def mask_credit_card(self, cc: str) -> str:
        """Enmascara una tarjeta de crédito mostrando solo los últimos 4 dígitos."""
        if not isinstance(cc, str):
            return cc
        clean_cc = re.sub(r"\D", "", cc)
        if len(clean_cc) >= 4:
            return f"****-****-****-{clean_cc[-4:]}"
        return "****-****-****-****"

    def mask_dni(self, dni: str) -> str:
        """Enmascara un DNI/NIE ocultando los dígitos centrales y dejando la letra final."""
        if not isinstance(dni, str):
            return dni
        clean_dni = dni.strip().upper()
        if len(clean_dni) >= 9:
            return f"****{clean_dni[4:8]}-{clean_dni[-1]}"
        return "*******-*"

    def anonymize_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aplica las reglas de enmascaramiento sobre un DataFrame corporativo."""
        logger.info("Iniciando pipeline de enmascaramiento de PII...")
        df_masked = df.copy()

        if "email" in df_masked.columns:
            df_masked["email"] = df_masked["email"].apply(self.mask_email)
            logger.info("Columna 'email' enmascarada correctamente.")

        if "phone" in df_masked.columns:
            df_masked["phone"] = df_masked["phone"].apply(self.mask_phone)
            logger.info("Columna 'phone' enmascarada correctamente.")

        if "credit_card" in df_masked.columns:
            df_masked["credit_card"] = df_masked["credit_card"].apply(self.mask_credit_card)
            logger.info("Columna 'credit_card' enmascarada correctamente.")

        if "dni" in df_masked.columns:
            df_masked["dni"] = df_masked["dni"].apply(self.mask_dni)
            logger.info("Columna 'dni' enmascarada correctamente.")

        logger.info("Pipeline de anonimización completado con éxito.")
        return df_masked

def generate_mock_dataset(num_rows: int = 5) -> pd.DataFrame:
    """Genera un dataset sintético con Faker (es_ES) para pruebas de validación."""
    fake = Faker("es_ES")
    data = []
    for _ in range(num_rows):
        data.append({
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "credit_card": fake.credit_card_number(card_type="visa"),
            "dni": fake.bothify(text="########?")
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    original_df = generate_mock_dataset(5)
    print("\n--- DATOS ORIGINALES (CON PII EXPUESTA) ---")
    print(original_df.to_string())

    anonymizer = PIIAnonymizer()
    secured_df = anonymizer.anonymize_dataframe(original_df)

    print("\n--- DATOS SEGUROS (ENMASCARADOS / ANÓNIMOS) ---")
    print(secured_df.to_string())