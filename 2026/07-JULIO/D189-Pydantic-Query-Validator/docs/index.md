# Pydantic Query Validator (D189)

Micro-librería especializada en validación estricta de parámetros de entrada mediante **Pydantic v2** y un **SQL Sanitizer** heurístico basado en expresiones regulares para prevenir inyecciones SQL en APIs analíticas[cite: 1].

## 🏛️ Características Técnicas
- **Interceptación Temprana:** Inspección y limpieza de datos crudos antes de que el motor de tipos comience su validación estructural mediante `@field_validator(..., mode="before")`[cite: 1].
- **Prevención Proactiva de Inyecciones SQL:** Bloqueo automatizado de comentarios maliciosos, comandos destructivos (`DROP TABLE`) y tautologías lógicas (`OR 1=1`)[cite: 1].
- **Contratos de Datos Confiables:** Garantía estricta de formatos de fecha mediante expresiones regulares y control de rangos numéricos.

---

## 📊 Demostración Interactiva del Validador

A continuación se muestra el comportamiento del sistema al procesar diferentes tipos de consultas entrantes:

### 1. Casos de Prueba y Resultados en Ejecución

| ID Prueba | Tipo de Payload / Consulta | Datos de Entrada | Resultado del Validador | Estado Técnico |
|:----------|:---------------------------|:-----------------|:------------------------|:---------------|
| **TEST-01** | Consulta Analítica Válida | `metric="active_users"`, `dates="2026-01-01 / 2026-03-31"` | Datos tipados y devueltos correctamente | ✅ **APROBADO** |
| **TEST-02** | Intento de Inyección (Tautología) | `filters=["country = 'ES' OR 1=1"]` | Excepción disparada por patrón prohibido | 🛡️ **BLOQUEADO** |
| **TEST-03** | Intento de Inyección (Destructiva) | `metric="sales; DROP TABLE users; --"` | Bloqueo por detección de sentencia SQL múltiple | 🛡️ **BLOQUEADO** |
| **TEST-04** | Formato de Fecha Inválido | `start_date="01/01/2026"` (DD/MM/YYYY) | Error de validación por contrato de Regex | ❌ **RECHAZADO** |

> **Nota Técnica de Seguridad:** La intercepción en modo `before` garantiza que ningún parámetro malicioso llegue a ser interpretado por los motores de bases de datos analíticas (como DuckDB o Snowflake), protegiendo la infraestructura subyacente de ataques de manipulación de consultas.

---

## 🚀 Guía Rápida de Ejecución

Si deseas probar el validador o levantar esta documentación en tu entorno local, ejecuta los siguientes comandos en tu terminal (PowerShell):

1. **Instalar dependencias del entorno:**
   ```powershell
   python -m pip install -r requirements.txt