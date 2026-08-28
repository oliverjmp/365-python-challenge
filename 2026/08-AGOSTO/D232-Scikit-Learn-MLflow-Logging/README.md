# D232 - Scikit-Learn MLflow Logging | Enterprise MLOps Core

## 📋 Visión General del Proyecto
El hito **D232** implementa un pipeline automatizado de entrenamiento de Machine Learning utilizando **Scikit-learn** en conjunto con la API de **MLflow**. Su propósito es automatizar el entrenamiento de modelos predictivos, evaluar métricas de rendimiento (como Accuracy o MSE) y registrar de forma programática tanto los hiperparámetros como los artefactos binarios del modelo entrenado.

---

## 🎯 Casos de Uso Empresariales

### Caso de Uso 1: Automatización de Pipelines de Entrenamiento Predictivo
* **Contexto:** Las plataformas de analítica empresarial requieren reentrenar modelos de clasificación o regresión de forma programática con nuevos lotes de datos, asegurando que cada iteración quede documentada sin intervención manual.
* **Implementación con D232:** El módulo `ModelPipelineTrainer` procesa los datos, entrena el estimador de Scikit-learn, calcula métricas de evaluación y empaqueta el artefacto directamente en el servidor de MLflow.

### Caso de Uso 2: Versionado y Despliegue de Modelos Binarios
* **Contexto:** Garantizar que los pesos y la estructura de los modelos de Machine Learning queden guardados como artefactos recuperables para futuras fases de inferencia o despliegue en producción.
* **Implementación con D232:** Utilización nativa de `mlflow.sklearn.log_model` para guardar el modelo serializado junto con su entorno de ejecución y dependencias.

---

## 🏛️ Arquitectura y Patrones de Diseño
* **Patrón Pipeline Wrapper:** Encapsula la lógica de preprocesamiento, ajuste (*fit*) y evaluación dentro de una clase cohesiva y testeable.
* **Trazabilidad de Artefactos:** Integración directa entre el ciclo de vida del modelo de Scikit-learn y el almacenamiento de metadatos de MLflow.

---

## 🚀 Guía de Instalación y Ejecución

### 1. Instalación de Dependencias
```bash
pip install -r requirements.txt