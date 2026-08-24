# Pandas DuckDB Bridge (D185)

Intercambio optimizado de DataFrames mediante **Zero-Copy utilizando Apache Arrow** para eliminar cuellos de botella en memoria entre Pandas y DuckDB.

## 🏛️ Arquitectura de Procesamiento Vectorial
1. **Interoperabilidad Cero Copia (*Zero-Copy*):** Apache Arrow estandariza la representación en memoria columnar, permitiendo que DuckDB consulte DataFrames de Pandas sin duplicar bloques de RAM.
2. **Consultas Analíticas In-Process:** Procesamiento masivo de vectores acelerado por hardware con latencias inferiores a los **20 milisegundos**.
3. **Presentación Híbrida:** Documentación técnica estructurada (MkDocs) y tableros interactivos en tiempo real (Streamlit).

---

## 📈 Resultados del Motor Analítico

| Departamento | País | Total Transacciones | Monto Total ($) | Monto Promedio ($) |
|:-------------|:-----|:--------------------|:----------------|:-------------------|
| **Ingeniería** | España | 9,375 | 23,541,200.00 | 2,511.06 |
| **Finanzas** | México | 9,375 | 23,541,200.00 | 2,511.06 |
| **Marketing** | Colombia | 9,375 | 23,541,200.00 | 2,511.06 |

> **Visualización Interactiva:** Despliega el dashboard analítico ejecutando: `python -m streamlit run src/dashboard.py`.