# D148 - Dockerized ML Microservice

Este hito implementa la **containerización optimizada de un microservicio de inferencia de Machine Learning** con dependencias de Scikit-learn utilizando `Dockerfile` y Python.

## Características Principales
- **Imagen Contenedora Optimizada:** Basada en `python:3.11-slim` para reducir la superficie de ataque y el tamaño total de la imagen Docker.
- **Microservicio Modular:** Encapsula el estado del modelo (`MLInferenceService`) garantizando verificaciones de preparación (*readiness*).
- **Portabilidad Total:** Permite empaquetar código, dependencias numéricas (`numpy`, `scikit-learn`, `pandas`) y artefactos en un entorno reproducible.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Dockerizar microservicios de Machine Learning es el estándar de la industria para garantizar que los modelos entrenados localmente funcionen exactamente igual en servidores de producción o clústeres de Kubernetes.

### Ejemplos de Uso:
1. **Despliegues en la Nube (AWS ECS, Google Cloud Run):**
   * *Caso:* Desplegar contenedores efímeros que respondan a peticiones HTTP de inferencia bajo demanda.
2. **Pipelines de CI/CD Reproducibles:**
   * *Caso:* Ejecutar pruebas de integración dentro del contenedor para validar que las librerías binarias (como Scikit-learn) operen sin conflictos de entorno.

## 📂 Estructura del Proyecto
```text
D148-Dockerized-ML-Microservice/
│
├── src/
│   ├── __init__.py
│   └── service.py
├── tests/
│   ├── __init__.py
│   └── test_service.py
├── Dockerfile
├── run_service.py
├── requirements.txt
└── README.md