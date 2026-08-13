# D110 - Openpyxl Financial Modeler

Este hito implementa un **constructor automatizado de modelos financieros en Excel** combinando Pandas para el procesamiento de datos y Openpyxl para la inyección de fórmulas nativas, estilos corporativos y formatos condicionales.

## Características Principales
- **Fórmulas Nativas de Excel:** Inserción dinámica de funciones de suma (`=SUM()`) tanto para filas como para totales generales.
- **Formato Condicional:** Aplicación automatizada de alertas visuales basadas en reglas de umbral de valores.
- **Diseño Profesional:** Estilos personalizados, paletas de colores corporativas, bordes contables y autoajuste de celdas.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En entornos financieros y de gestión empresarial, la creación manual de reportes en Excel es propensa a errores y consume mucho tiempo. La automatización mediante código permite:

### Ejemplos de Uso:
1. **Generación de Reportes P&L (PyG) Automatizados:**
   * *Caso:* Consolidar los estados financieros mensuales directamente desde bases de datos corporativas hacia plantillas ejecutivas estandarizadas para la junta directiva.
2. **Tableros de Presupuesto y Control de Gastos:**
   * *Caso:* Automatizar plantillas donde los departamentos proyectan sus costos operativos y el sistema aplica fórmulas y alertas de desviación de forma automática.
3. **Cierres Contables Periódicos:**
   * *Caso:* Exportar cierres contables con fórmulas preconfiguradas para que los analistas financieros solo validen los resultados sin reconstruir la estructura de la hoja de cálculo.

## 📂 Estructura del Proyecto
```text
D110-Openpyxl-Financial-Modeler/
│
├── src/
│   ├── __init__.py
│   └── modeler.py
├── tests/
│   └── test_modeler.py
├── run_model.py
├── requirements.txt
└── README.md