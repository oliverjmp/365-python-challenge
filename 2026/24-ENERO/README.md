# 📈 Día 24: Dashboard Conectado a Base de Datos (SQL)

## 🎯 Objetivo del Reto
Integrar la capa de **Visualización** con la capa de **Persistencia**. El objetivo es que el dashboard sea dinámico y refleje en tiempo real el estado de la base de datos SQL.

## 🛠️ Tecnologías Aplicadas
* **SQL Querying:** Uso de `GROUP BY` y `COUNT` para procesar datos directamente en el motor de la DB.
* **Matplotlib:** Generación de gráficos de barras para seguimiento de KPIs de gestión.
* **Integración Pandas-SQL:** Consumo eficiente de registros relacionales.

## 🚀 Logros del Día
* Eliminación de la dependencia de archivos planos (CSV).
* Implementación de etiquetas de datos dinámicas sobre gráficos.
* Automatización del reporte de "Estado de Tickets" (Pendientes vs. Resueltos).

## 💡 Impacto Senior
Este diseño separa la **Data** de la **Presentación**. Es una arquitectura profesional donde los datos residen seguros en SQL y el código de Python solo se encarga de presentarlos de forma inteligente.