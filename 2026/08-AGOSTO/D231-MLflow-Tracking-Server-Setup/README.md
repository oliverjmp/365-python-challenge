# D231 - MLflow Tracking Server Setup | Enterprise MLOps Core

## 📋 Visión General del Proyecto
El hito **D231** establece la infraestructura de MLOps para el registro, trazabilidad y control de versiones de experimentos de Machine Learning utilizando **MLflow Tracking** con almacenamiento persistente en **SQLite**. Permite registrar hiperparámetros, métricas de rendimiento y artefactos de modelos de manera estructurada en entornos corporativos.

---

## 🎯 Casos de Uso Empresariales

### Caso de Uso 1: Control de Experimentos de Modelos Predictivos
* **Contexto:** Los equipos de ciencia de datos entrenan iterativamente múltiples variantes de modelos de Machine Learning (por ejemplo, Regresión Lineal o Bosques Aleatorios) y necesitan comparar qué combinación de hiperparámetros ofrece la mayor precisión en validación.
* **Implementación con D231:** El módulo centralizado `MLflowTracker` registra cada ejecución (*run*) en un experimento específico, almacenando métricas clave (como RMSE o Accuracy) y parámetros de configuración para su posterior auditoría visual o programática.

### Caso de Uso 2: Trazabilidad y Reproductibilidad para Auditoría
* **Contexto:** Los estándares de cumplimiento regulatorio exigen conocer exactamente qué código, datos y parámetros generaron un modelo puesto en producción.
* **Implementación con D231:** El servidor centralizado con backend SQLite consolida el historial inmutable de todas las ejecuciones del equipo.

---

## 🏛️ Arquitectura y Patrones de Diseño
* **Patrón Tracker / Wrapper:** Centraliza la interacción con la API de MLflow, aislando la lógica de negocio de los comandos específicos del framework de trazabilidad.
* **Backend Persistente Local:** Utiliza una base de datos ligera SQLite combinada con un directorio local para artefactos, ideal para entornos de desarrollo y staging robustos.

---

## 🚀 Guía de Instalación y Ejecución

### 1. Instalación de Dependencias
```bash
pip install -r requirements.txt