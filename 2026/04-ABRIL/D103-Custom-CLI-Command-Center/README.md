# D103 - Custom CLI Command Center

Este proyecto implementa una **Interfaz de Línea de Comandos (CLI) enriquecida con Typer y Rich**, diseñada para actuar como un centro de control visual y moderno en consola.

## Características Principales
- **Typer Framework:** Creación intuitiva de comandos y opciones basadas en anotaciones de tipos de Python.
- **Rich UI:** Renderizado de tablas estilizadas, colores personalizados y barras de progreso en tiempo real.
- **Pruebas Unitarias:** Cobertura validada mediante el `CliRunner` de Typer.

## Requisitos del Entorno
- Python 3.11 o superior.
- Librerías especificadas en `requirements.txt`:
  ```text
  typer==0.9.0
  rich==13.7.1