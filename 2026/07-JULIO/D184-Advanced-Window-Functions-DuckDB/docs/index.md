# Advanced Window Functions DuckDB (D184)

Cálculo de métricas financieras de crecimiento y tendencias secuenciales mediante **funciones de ventana avanzadas (*Window Functions*)** ejecutadas directamente con DuckDB sobre almacenamiento columnar comprimido.

## 🏛️ Fundamentos de Arquitectura Analítica
1. **Particionamiento Lógico (`PARTITION BY`):** Aislamiento de cálculos por dimensiones de negocio sin necesidad de agrupar físicamente el conjunto de datos.
2. **Ventanas Deslizantes y Acumuladas (`ROWS BETWEEN`):** Cálculo eficiente de sumas móviles y saldos acumulados anuales (*Running Totals*).
3. **Funciones de Retraso Temporal (`LAG`):** Acceso a filas anteriores en datasets ordenados cronológicamente para el cálculo automático de tasas de variación intermensual (MoM).

---

## 📈 Resultados del Motor Analítico

| Línea de Negocio | Año | Mes | Ingresos Mensuales ($) | Ingresos Acumulados ($) | Variación MoM (%) |
|:-----------------|:----|:----|:-----------------------|:------------------------|:------------------|
| **Cloud Infrastructure** | 2024 | 1 | 172,500.00 | 172,500.00 | 0.00 |
| **Cloud Infrastructure** | 2024 | 2 | 176,025.00 | 348,525.00 | 2.04 |
| **Cloud Infrastructure** | 2024 | 3 | 179,550.00 | 528,075.00 | 2.00 |
| **Cybersecurity Suite** | 2024 | 1 | 103,500.00 | 103,500.00 | 0.00 |

> **Visualización Interactiva:** Adicionalmente a esta documentación técnica, el proyecto cuenta con un **Dashboard Ejecutivo Interactivo** accesible mediante `streamlit run src/dashboard.py`.