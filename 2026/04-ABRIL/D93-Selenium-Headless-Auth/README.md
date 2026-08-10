# Módulo D93: Selenium Headless Auth (`Selenium + WebDriver Manager`)

## Descripción General
Este módulo implementa la **automatización de flujos de inicio de sesión** en aplicaciones web utilizando Selenium WebDriver en modo `headless` y `webdriver-manager` para la gestión automática de binarios, incorporando pasos para credenciales y autenticación de doble factor (MFA).

---

## Características Principales
* **Modo Headless Optimizado**: Ejecución de pruebas de navegador sin interfaz gráfica, ideal para servidores y pipelines de integración continua.
* **Gestión Automática de Drivers**: Uso de `webdriver-manager` para evitar configuraciones manuales de ChromeDriver.
* **Robustez y Limpieza**: Bloques de control de excepciones y cierre seguro de sesiones mediante `finally`.

---

## Estructura del Proyecto
```text
D93-Selenium-Headless-Auth/
├── src/
│   ├── __init__.py
│   └── auth_automation.py # Lógica del bot de Selenium y flujo de autenticación
├── tests/
│   ├── __init__.py
│   └── test_auth_automation.py # Pruebas unitarias de inicialización y manejo de errores
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo