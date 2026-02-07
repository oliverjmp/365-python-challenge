# 📥 Día 27: Ingesta de Datos Incremental

## 🎯 Objetivo del Reto
Desarrollar un flujo de actualización de datos que permita alimentar la base de datos SQL con nueva información sin comprometer los registros históricos.

## 🛠️ Lógica Aplicada
* **Filtrado en el Edge:** El script evalúa los datos antes de la inserción, aplicando la regla de negocio: "Solo comentarios con Score <= -0.7 califican como Alertas".
* **Persistencia Acumulativa:** Uso de `INSERT` para expandir el dataset histórico en lugar de reemplazarlo.

## 🚀 Valor para BI
Permite observar la evolución de la calidad del servicio a lo largo del tiempo. Al no borrar los datos del pasado, podemos comparar si las crisis de hoy son menores o mayores que las de la semana pasada.