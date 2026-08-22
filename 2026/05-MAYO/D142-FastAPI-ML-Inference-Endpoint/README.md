# D142 - FastAPI ML Inference Endpoint

Este hito implementa un **microservicio web para la inferencia en tiempo real de modelos de Machine Learning serializados** utilizando `FastAPI` y `Joblib`.

## Características Principales
- **Arquitectura desacoplada:** Separa la lógica de carga y predicción del modelo (`ModelInferenceService`) de las rutas web (`FastAPI`).
- **Endpoints robustos:** Incluye verificación de estado (`/health`) y procesamiento de peticiones en tiempo real (`/predict`).
- **Validación de esquemas:** Utiliza `Pydantic` para asegurar que los datos de entrada cumplan con los tipos y dimensiones esperados.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En despliegues de Machine Learning de producción, empaquetar un modelo en una API REST permite que aplicaciones web, móviles o servicios backend consuman predicciones de forma síncrona.

### Ejemplos de Uso:
1. **Scoring Crediticio en Tiempo Real:** Evaluar si un cliente es apto para un crédito de forma instantánea al enviar su formulario de solicitud.
2. **Detección de Fraude en Pasarelas de Pago:** Analizar transacciones al instante para aprobar o denegar operaciones sospechosas.

## 📂 Estructura del Proyecto
```text
D142-FastAPI-ML-Inference-Endpoint/
│
├── src/
│   ├── __init__.py
│   ├── model_service.py
│   └── main.py
├── tests/
│   └── test_api.py
│   └── test_service.py
├── train_dummy_model.py
├── requirements.txt
└── README.md