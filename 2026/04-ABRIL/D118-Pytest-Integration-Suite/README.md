# D118 - Pytest Integration Suite

Este hito implementa una **suite avanzada de pruebas de integración con simulación de servicios externos (Mocking)** utilizando `Pytest`, `Fixtures` y `monkeypatch`.

## Características Principales
- **Aislamiento de Pruebas:** Permite probar clientes HTTP y flujos complejos sin realizar peticiones de red reales (evitando latencia, costos o caídas de servicios de terceros).
- **Uso Avanzado de Fixtures:** Configuración reutilizable de estados iniciales y dependencias para múltiples escenarios de prueba.
- **Manejo Robusto de Excepciones:** Validación de fallos y códigos de estado HTTP (404, 500) de manera controlada.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En sistemas empresariales, las aplicaciones interactúan constantemente con pasarelas de pago, APIs bancarias o microservicios externos.

### Ejemplos de Uso:
1. **Pruebas de Integración Resilientes:**
   * *Caso:* Comprobar cómo reacciona tu pipeline de datos si la pasarela de pagos externa se cae o responde con errores inesperados.
2. **Entornos de CI/CD Sin Dependencias Externas:**
   * *Caso:* Garantizar que los pipelines de integración continua pasen de forma rápida y confiable sin depender de que los servidores externos estén activos.

## 📂 Estructura del Proyecto
```text
D118-Pytest-Integration-Suite/
│
├── src/
│   ├── __init__.py
│   └── external_service.py
├── tests/
│   └── test_integration.py
├── run_integration.py
├── requirements.txt
└── README.md
