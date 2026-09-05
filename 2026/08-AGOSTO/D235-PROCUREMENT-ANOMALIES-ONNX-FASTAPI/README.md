# D235 - Procurement Anomalies ONNX FastAPI

Microservicio analítico de alto rendimiento diseñado para la detección en tiempo real de anomalías en procesos de compras corporativas (Procurement). Sustituye la serialización de objetos estándar por **ONNX**, desacoplando el entorno de entrenamiento del servidor de producción.

## 🏛️ Arquitectura Implementada
1. **Interoperabilidad ONNX:** El modelo de Machine Learning es exportado a un grafo computacional estandarizado mediante `skl2onnx`, eliminando la necesidad de empaquetar `scikit-learn` en producción.
2. **Inferencia Acelerada:** Utiliza `onnxruntime` en lugar del runtime de Python estándar, optimizando la latencia de las consultas estructuradas de FastAPI.
3. **Validación Estricta:** Implementación de esquemas Pydantic para asegurar que las variables financieras (montos, desviaciones) sean matemáticamente válidas antes de cruzar la capa del tensor.

## 🚀 Ejecución del Pipeline
1. **Generación del artefacto ONNX:**
   ```bash
   python train_to_onnx.py