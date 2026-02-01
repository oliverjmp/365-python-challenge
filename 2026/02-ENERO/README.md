🕸️ Día 02 — Scraper Avanzado con Rotación de User Agents + API Profesional
Autor: Oliver Javier Morales Pérez
Proyecto: 365 Python Challenge
🚀 Descripción del proyecto
Este proyecto implementa un scraper profesional que obtiene información actualizada de criptomonedas utilizando la API oficial de CoinGecko, garantizando datos precisos y estables.

Incluye:

Extracción de datos reales del mercado cripto

Rotación de user agents (para evitar bloqueos en versiones futuras del scraper HTML)

Limpieza y transformación de datos

Exportación a un archivo CSV

Visualización de un resumen en consola

Este tipo de solución es común en:

Automatización de reportes financieros

Monitoreo de precios en tiempo real

Data Engineering

Integración de datos externos en pipelines ETL

🧠 Tecnologías utilizadas
Python 3

requests — consumo de API

pandas — transformación y exportación de datos

Rotación de user agents (estructura preparada para scraping avanzado)

📦 Estructura del proyecto
Código
dia_02_Scraper_Avanzado/
│── main.py
│── README.md
└── recursos/
▶️ Cómo ejecutar
1. Instala las dependencias:
bash
pip install requests pandas
2. Ejecuta el script:
bash
python main.py
3. Se generará automáticamente el archivo:
Código
precios_crypto.csv
📊 Resultado
El CSV contiene:

Nombre de la criptomoneda

Precio actual (USD)

Variación porcentual en 24h

Capitalización de mercado

Además, el programa muestra en consola una tabla profesional con los Top 10 criptoactivos por capitalización.

Ejemplo:

Top 10 criptomonedas extraídas:
              Nombre      Precio Cambio 24h          Market Cap
0            Bitcoin  $76,691.00     -1.98%  $1,532,471,563,150
1           Ethereum   $2,296.78     -4.75%    $277,028,660,491
2             Tether       $1.00      0.00%    $185,141,612,568
3                BNB     $756.46     -2.34%    $103,307,651,089
4                XRP       $1.59     -0.90%     $97,068,320,069
5               USDC       $1.00      0.00%     $70,276,477,860
6             Solana     $101.50     -2.00%     $57,731,317,524
7               TRON       $0.28     -0.19%     $27,006,469,507
8  Lido Staked Ether   $2,296.00     -4.71%     $22,088,165,012
9           Dogecoin       $0.10      2.33%     $17,570,047,660