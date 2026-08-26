# Arquitectura de Decoradores y Telemetría - D207

## 📐 Topología de Intercepción y Ciclo de Ejecución

El siguiente diagrama detalla el flujo detallado de cómo el decorador interactúa con la llamada al método analítico y el motor DuckDB:

```mermaid
graph TD
    A[Cliente / Capa de Servicio] -->|Invoca Método Analítico| B(medir_rendimiento_sql Wrapper)
    B -->|Inicia time.perf_counter| C[Ejecución de Sentencia SQL en DuckDB]
    C -->|Retorno de DataFrame / Error| D{¿Ocurrió Excepción?}
    D -->|No| E[Recupera Resultados Exitosos]
    D -->|Sí| F[Captura Excepción y Marca Estado Fallido]
    E & F -->|Bloque Finally: Calcula Latencia ms| G[Registro de Logs de Telemetría]
    G -->|Entrega de Datos| H[Respuesta Final al Cliente]