# D233 - MLflow Model Registry | Enterprise MLOps Core

## 📋 Visión General del Proyecto
El hito **D233** implementa la gestión del ciclo de vida de modelos mediante **MLflow Model Registry**. Permite registrar modelos entrenados en un repositorio centralizado, versionarlos de forma incremental y transicionar sus etapas operativas (*Staging*, *Production*, *Archived*) para garantizar un control riguroso en despliegues corporativos.

---

## 🎯 Casos de Uso Empresariales

### Caso de Uso 1: Promoción Controlada de Modelos a Producción
* **Contexto:** Los modelos predictivos evaluados en entornos de staging deben pasar por criterios de aprobación antes de servir tráfico en producción.
* **Implementación con D233:** El módulo `ModelRegistryManager` registra el binario del modelo y actualiza su etapa (*stage*) programáticamente a `Production`, archivando automáticamente versiones anteriores obsoletas.

### Caso de Uso 2: Gobernanza y Auditoría del Ciclo de Vida
* **Contexto:** Los equipos de operaciones requieren trazabilidad absoluta sobre qué versión exacta de un modelo se encuentra activa en cada entorno de negocio.
* **Implementación con D233:** Uso del registro centralizado basado en metadatos persistidos para consultar el estado actual, número de versión y descripciones de cada artefacto.

---

## 🏛️ Arquitectura y Patrones de Diseño
* **Patrón Registry Wrapper:** Centraliza las operaciones de registro, transición de etapas y recuperación de metadatos del Model Registry de MLflow.
* **Persistencia Centralizada:** Conexión mediante backend SQLite para el almacenamiento estructurado de versiones y estados de modelos.

---

## 🚀 Guía de Instalación y Ejecución

### 1. Instalación de Dependencias
```bash
pip install -r requirements.txt