# D98 - OS Process Manager

Este proyecto forma parte del desafío de automatización y desarrollo en Python. Su objetivo principal es implementar un gestor de procesos del sistema operativo utilizando las librerías `psutil` y `subprocess` para el control de recursos, monitoreo en tiempo real y prevención de cuelgues del sistema.

## Características Principales
- **Listado de Procesos Activos:** Inspección segura de los procesos en ejecución obteniendo métricas clave como PID, nombre, consumo de CPU y porcentaje de memoria.
- **Prevención de Cuergues / Auto-terminación:** Identificación y cierre automático de procesos que superen los umbrales críticos configurados, protegiendo los procesos esenciales del sistema operativo.
- **Pruebas Unitarias Robustas:** Cobertura de código validada con `pytest` y simulación de comportamientos de sistema mediante técnicas de *mocking*.

## Requisitos del Entorno
- Python 3.11 o superior.
- Librerías necesarias (especificadas en `requirements.txt`):
  ```text
  psutil==5.9.8
  pytest==8.1.1
  pytest-cov==4.1.0