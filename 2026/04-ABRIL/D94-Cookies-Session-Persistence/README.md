# D94 - Persistencia de Sesiones con Selenium y Pickle

Este proyecto forma parte del desafío de automatización en Python. Su objetivo principal es gestionar la persistencia de sesiones de usuario en navegadores automatizados mediante el almacenamiento y carga de cookies utilizando los módulos `Selenium` y `pickle`.

## Características Principales
- **Guardado de Sesión:** Captura las cookies activas de una sesión de navegador autenticada y las serializa en un archivo local (`cookies.pkl`).
- **Restauración de Sesión:** Inyecta cookies guardadas previamente en una nueva instancia de Selenium para mantener el estado de autenticación sin reintroducir credenciales.
- **Pruebas Unitarias Robustas:** Cobertura de código al 100% implementada con `pytest` y simulación de comportamientos (*mocking*).

## Requisitos del Entorno
- Python 3.11 o superior.
- Librerías necesarias:
  ```bash
  pip install selenium webdriver-manager pytest pytest-cov