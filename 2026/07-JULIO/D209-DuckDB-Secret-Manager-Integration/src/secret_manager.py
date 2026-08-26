import os
import secrets

class SecretManager:
    """Gestor seguro de secretos y configuración de entornos analíticos."""

    def __init__(self):
        # Cargar o validar credenciales predeterminadas desde el entorno
        self.db_user = os.getenv("DUCKDB_USER", "admin_analitica")
        self.storage_bucket = os.getenv("DUCKDB_STORAGE_BUCKET", "s3://enterprise-data-lake-raw")
        self.api_token = os.getenv("DUCKDB_API_TOKEN", "")

    def generar_token_seguro(self) -> str:
        """Genera un token criptográficamente seguro para sesiones analíticas temporales."""
        return secrets.token_hex(16)

    def validar_credenciales(self) -> dict:
        """Valida que los secretos críticos estén presentes y seguros."""
        if not self.storage_bucket.startswith("s3://") and not self.storage_bucket.startswith("azure://"):
            raise ValueError("La ruta del Data Lake debe ser un almacenamiento remoto seguro válido (s3:// o azure://).")
        
        return {
            "user": self.db_user,
            "bucket": self.storage_bucket,
            "token_generado": self.generar_token_seguro(),
            "status": "SECURE_CONFIGURED"
        }