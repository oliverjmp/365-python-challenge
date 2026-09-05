# D237 - Data Quality & Contracts

## 🏢 Resumen Ejecutivo
El hito **D237** aborda la certificación de integridad de datos previo a su consumo en pipelines analíticos o modelos de Machine Learning. Se implementa un **Contrato de Datos** utilizando `great_expectations` para asegurar que las variables críticas cumplan con las reglas de negocio estrictas de la corporación.

## 🎯 Objetivos y Principios
* **Interceptación Temprana:** Bloqueo de datos corruptos, valores nulos no permitidos o categorías inválidas antes de que contaminen el Data Lake.
* **Trazabilidad de Errores:** Generación de estadísticas exactas sobre qué porcentaje de un lote falló y por qué regla específica.