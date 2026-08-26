# Arquitectura del Gestor de Secretos - D209

## 📐 Topología de Seguridad y Flujo de Autenticación

```mermaid
graph TD
    A[.env / Entorno del Sistema] -->|Variables Sensibles| B[SecretManager / src/secret_manager.py]
    B -->|Validación de Integridad| C{¿Credenciales Válidas?}
    C -->|No| D[Lanzamiento de Excepción de Configuración]
    C -->|Sí| E[Inyección Segura a DuckDB / Secret Storage]
    E -->|Consulta Analítica Segura| F[Data Lake / Archivos Remotos]