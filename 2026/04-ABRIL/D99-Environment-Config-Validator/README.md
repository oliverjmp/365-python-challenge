# D99 - Environment Config Validator

Este proyecto forma parte del desafío diario en Python. Su objetivo principal es implementar un validador estricto de variables de entorno y secretos de configuración en el arranque utilizando **Pydantic BaseSettings**.

## Características Principales
- **Validación Estricta en Arranque:** Garantiza que todas las variables críticas requeridas estén presentes y tengan el tipo de dato correcto antes de iniciar la aplicación.
- **Valores por Defecto Seguros:** Configuración flexible para entornos de desarrollo y producción.
- **Pruebas Unitarias Robustas:** Cobertura de código validada al 100% con `pytest` y simulación de variables de entorno.

## Requisitos del Entorno
- Python 3.11 o superior.
- Librerías especificadas en `requirements.txt`:
  ```text
  pydantic==2.6.4
  pydantic-settings==2.2.1
  pytest==8.1.1
  pytest-cov==4.1.0
  python-dotenv==1.0.1