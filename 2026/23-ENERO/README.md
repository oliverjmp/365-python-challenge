# 🗄️ Día 23: Persistencia de Datos con SQLite

## 🎯 Objetivo del Reto
Migrar de un sistema de almacenamiento plano (archivos temporales) a un sistema de almacenamiento persistente y relacional utilizando **SQL**.

## 🛠️ Tecnologías
* **SQLite3:** Motor de base de datos relacional integrado en Python.
* **SQL (Structured Query Language):** Para la creación de tablas y gestión de registros.
* **Pandas + SQL:** Integración para lectura de queries directamente a DataFrames.

## 🏗️ Estructura de la Tabla `AlertasCriticas`
| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| id | INT | Clave primaria autoincremental |
| fecha | TEXT | Timestamp del registro |
| usuario | TEXT | Identificador del cliente |
| comentario| TEXT | Texto analizado |
| score | REAL | Valor numérico del sentimiento |
| estado | TEXT | Estado de gestión (PENDIENTE/RESUELTO) |

## 🚀 Valor Agregado
Este módulo permite la **auditoría histórica**. A diferencia de los CSV que se sobrescriben, la base de datos acumula el conocimiento, permitiendo análisis de tendencias a largo plazo en cualquier herramienta de BI.