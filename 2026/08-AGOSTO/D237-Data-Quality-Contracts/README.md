# D237 - Data Quality & Data Contracts

Motor de perfilado y certificación de calidad de datos corporativos utilizando **Great Expectations**. 

## 💼 Casos Prácticos de Uso Empresarial

1. **Filtro de Ingesta en Data Lakes:**
   - Prevenir que sistemas externos inyecten valores nulos, fechas imposibles o montos negativos en las tablas núcleo de finanzas.
2. **Auditoría Pre-Modelado (MLOps):**
   - Asegurar que las variables (features) que alimentan los modelos ONNX cumplan estrictamente con las distribuciones matemáticas esperadas.
3. **Migración Segura de Datos:**
   - Validar que los datos extraídos de sistemas *legacy* mantengan la coherencia estructural antes de insertarse en el almacén columnar moderno.

## 🏛️ Estructura del Proyecto

D237-Data-Quality-Contracts/
├── .coveragerc            # Configuración de políticas estrictas de cobertura (100%)
├── docs/
│   ├── index.md           # Documentación técnica corporativa
│   └── architecture.md    # Arquitectura detallada del contrato de datos
├── src/
│   ├── __init__.py
│   └── data_contract.py   # Motor de validación efímero con Great Expectations
├── tests/
│   ├── __init__.py
│   └── test_contract.py   # Pruebas unitarias estrictas con pytest
├── app_frontend.py        # Dashboard interactivo en Streamlit
├── mkdocs.yml             # Configuración del portal web (Tema Índigo)
├── requirements.txt       # Dependencias del entorno
└── README.md              # Documentación principal en la raíz

## 🚀 Ejecución y Comandos de Pruebas

- **Instalación de dependencias:**
  `pip install -r requirements.txt`

- **Ejecución de pruebas unitarias (Garantizando 100% de cobertura):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Lanzamiento del Dashboard de Calidad (Streamlit):**
  `streamlit run app_frontend.py`

- **Lanzamiento del Portal de Documentación:**
  `mkdocs serve`