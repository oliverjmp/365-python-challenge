# D220 - Phase 4 Milestone Consolidation (Git CI/CD Automation)

Consolidación y cierre formal del primer bloque intensivo de la Fase 4 del reto de ingeniería, implementando un pipeline automatizado de integración continua (**Git CI/CD**) mediante **GitHub Actions** para garantizar la calidad, estabilidad y cobertura estricta del código.

---

## 🏛️ Explicación Profunda de la Automatización CI/CD

### La Problemática: Despliegues Frágiles y Deuda Técnica Oculta
En proyectos analíticos y de ingeniería de datos complejos, confiar exclusivamente en la ejecución manual de pruebas locales genera vulnerabilidades críticas:
* **Falta de estandarización:** Las diferencias entre entornos locales de desarrollo (Windows, macOS, Linux) pueden enmascarar fallos de ejecución.
* **Corrupción de Cobertura:** A medida que el código escala, es común que se introduzcan bloques de código huérfanos o sin pruebas unitarias si no existe un guardián automatizado.

### La Solución: Integración Continua Estricta
El flujo de **GitHub Actions** implementado en este hito automatiza el ciclo de vida de validación. Cada vez que se emite un cambio, el sistema despliega un entorno virtual aislado, instala las dependencias declaradas y ejecuta la suite de pruebas bajo un umbral de exigencia intransigente del **100.00% de cobertura**.

---

## 💼 Casos de Uso Reales en Entornos de Producción

1. **Gobierno de Datos y Control de Calidad en Equipos Ágiles:**
   - Impide que desarrolladores integren código sin cobertura de pruebas a la rama principal, protegiendo los núcleos analíticos críticos frente a regresiones accidentales.
2. **Validación de Compatibilidad Multi-Plataforma:**
   - Permite verificar de manera transparente que las librerías de alto rendimiento y gestión de memoria (como PyArrow y DuckDB trabajadas en hitos anteriores) funcionen de manera idéntica en distintas versiones de Python y sistemas operativos del servidor.
3. **Auditoría Externa y Cumplimiento Normativo (*Compliance*):**
   - Proporciona un historial inmutable y público del estado de salud del software, facilitando certificaciones de calidad técnica exigidas en arquitecturas corporativas.

---

## 🛠️ Estructura del Proyecto

D220-Phase-4-Milestone-Consolidation/
├── .github/
│   └── workflows/
│       └── ci.yml         # Definición del Pipeline de GitHub Actions
├── .coveragerc            # Configuración de umbral de cobertura estricta (100%)
├── docs/
│   ├── index.md           # Documentación técnica ejecutiva (MkDocs)
│   └── architecture.md    # Diagrama y explicación profunda del pipeline CI/CD
├── src/
│   ├── __init__.py
│   └── pipeline_validator.py # Núcleo de validación del cierre de fase
├── tests/
│   ├── __init__.py
│   └── test_validator.py  # Pruebas unitarias con 100% de cobertura
├── main.py                # Script CLI de validación local del hito
├── mkdocs.yml             # Configuración del portal de documentación
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación raíz ampliada y casos de uso

---

## 🚀 Comandos de Ejecución y Validación Local

- **Instalar dependencias del entorno:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias locales (Garantizando el 100.00% de cobertura exacta):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar script de validación CLI:**
  `python main.py`

- **Levantar el servidor local de documentación (MkDocs):**
  `mkdocs serve`