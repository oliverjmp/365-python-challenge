# Módulo D70: Automatización de Pruebas y Pipeline de CI/CD

Este módulo implementa un pipeline de Integración Continua (CI) utilizando GitHub Actions para automatizar la ejecución de pruebas unitarias y el control de cobertura de código.

## Estructura del Proyecto
- `src/`: Contiene el código fuente del transformador ETL (`etl_transformer.py`).
- `tests/`: Contiene la suite de pruebas unitarias (`test_etl_transformer.py`).
- `.github/workflows/ci.yml`: Configuración del pipeline automatizado.

## Ejecución Local
Para ejecutar las pruebas y verificar la cobertura en tu equipo local:
```bash
pytest --cov=src --cov-report=term-missing