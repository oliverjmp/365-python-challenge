### 🧹 Proyecto Día 54: Data Cleaning & Normalization 🐼🧪

El objetivo de hoy es transformar un dataset "sucio" e inconsistente en uno listo para el análisis profesional. Hemos implementado técnicas de limpieza forense para asegurar la integridad de los datos antes de cualquier visualización.

#### **Hitos Técnicos Alcanzados:**
1.  **Imputación de Valores Nulos:** Detección de `NaN` (Not a Number) y toma de decisiones estratégica: eliminar (`dropna`) o rellenar (`fillna`).
2.  **Casting y Normalización:** Conversión de tipos de datos (strings a floats) eliminando ruidos visuales como símbolos de moneda o comas.
3.  **Filtrado de Outliers:** Eliminación de registros con errores lógicos (precios negativos o stocks imposibles).
4.  **Deduplicación:** Identificación y limpieza de registros repetidos que sesgan el análisis.

#### **Tecnologías Utilizadas:**
* **Pandas:** Uso de métodos `.str`, `.astype()`, y `.apply()`.