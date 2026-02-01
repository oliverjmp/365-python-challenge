📄 Día 04 — Limpieza de Datos y Dashboard Profesional en Excel
Autor: Oliver Javier Morales Pérez
Proyecto: 365 Python Challenge

🚀 Descripción del proyecto
En este cuarto día del reto, el objetivo es transformar el informe generado en el Día 03 en un Excel profesional, estructurado en varias hojas, con datos limpios, formateados y acompañados de gráficos generados automáticamente desde Python.

El script toma el archivo:

Código
../03-ENERO/informe_cripto.xlsx
y produce un nuevo informe con estilo Premium Ejecutivo, aplicando formatos avanzados, colores corporativos y gráficos optimizados.

📑 Contenido del informe generado
✔ Hoja 1 — Tabla (Datos limpios y formateados)
Precios correctamente formateados

Market Cap sin notación científica

Porcentajes con formato profesional

Separadores de miles

Columnas ajustadas

Estilo gris oscuro + dorado

✔ Hoja 2 — MarketCap (Gráfico profesional)
Gráfico de barras del Market Cap

Valores correctamente formateados

Visualización clara y ejecutiva

Estética premium

✔ Hoja 3 — Gráficos (Variación y Precio)
📈 Gráfico de líneas con la variación porcentual 24h

💵 Gráfico de barras con el precio actual

Tamaños y posiciones optimizadas

Fondo gris oscuro y tipografía elegante

🧠 Tecnologías utilizadas
Python 3

pandas

openpyxl

openpyxl.chart (BarChart, LineChart)

📦 Estructura del proyecto
Código
dia_04_Graficos_Profesionales/
│── main.py
│── README.md
└── informe_cripto.xlsx  (salida)
▶️ Cómo ejecutar
1. Instalar dependencias:
bash
pip install pandas openpyxl
2. Asegurarte de tener el archivo:
Código
../03-ENERO/informe_cripto.xlsx
3. Ejecutar el script:
bash
python main.py
4. Se generará automáticamente:
Código
informe_cripto.xlsx
con todas las hojas listas para exportar a PDF en el Día 05.

📊 Resultado final
El archivo Excel generado presenta:

Datos limpios y correctamente formateados

Gráficos profesionales

Estilo visual coherente y elegante

Estructura clara para análisis ejecutivo

Preparación perfecta para exportación a PDF

✨ Nota final
Este dashboard es totalmente funcional, pero puede ampliarse tanto como necesites:
nuevos gráficos, más hojas, estilos alternativos, automatización avanzada… lo que haga falta para llevar tu informe al siguiente nivel.

Cuando quieras, seguimos evolucionándolo.