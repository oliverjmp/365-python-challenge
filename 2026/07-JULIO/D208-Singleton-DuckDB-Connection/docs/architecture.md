# Arquitectura del Patrón Singleton para DuckDB - D208

## 📐 Topología y Control de Concurrencia por Hilos

```mermaid
graph TD
    A[Hilo de Ejecución 1 ó N] -->|Solicita Instancia| B{¿Existe Instancia _instance?}
    B -->|Bloqueo Lock Sincronizado| C{¿Es None?}
    C -->|Sí| D[Crea Nueva Conexión DuckDB in-process]
    C -->|No| E[Retorna Instancia Existente en Memoria]
    D --> E
    E --> F[Operaciones SQL Seguras y Compartidas]