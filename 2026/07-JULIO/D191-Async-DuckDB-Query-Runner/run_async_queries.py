import asyncio
import time
import logging
from src.async_engine import AsyncDuckDBRunner

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    print("==================================================================")
    print("   D191 - EJECUTOR ASÍNCRONO DE CONSULTAS ANALÍTICAS (DUCKDB)    ")
    print("==================================================================\n")
    
    runner = AsyncDuckDBRunner()
    
    lote_consultas = [
        {
            "id": "Q_VENTAS_TOTALES",
            "query": "SELECT categoria, SUM(monto) FROM ventas_analiticas GROUP BY categoria;",
            "delay": 0.2
        },
        {
            "id": "Q_FILTRO_TECNOLOGIA",
            "query": "SELECT * FROM ventas_analiticas WHERE categoria = 'Tecnología';",
            "delay": 0.1
        },
        {
            "id": "Q_ESTADISTICAS_GLOBALES",
            "query": "SELECT COUNT(*), AVG(monto), MAX(monto) FROM ventas_analiticas;",
            "delay": 0.3
        }
    ]
    
    print(f"[1/2] Lanzando {len(lote_consultas)} consultas analíticas en paralelo hacia el Data Lake...")
    inicio_total = time.time()
    
    resultados = await runner.ejecutar_lote_concurrente(lote_consultas)
    
    tiempo_total = (time.time() - inicio_total) * 1000
    print(f" > ¡Lote completado de forma no bloqueante en {round(tiempo_total, 2)} ms!\n")
    
    print("[2/2] Reporte de Resultados Individuales por Hilo:")
    for res in resultados:
        print(f" • Consulta ID : {res['query_id']}")
        print(f"   - Duración  : {res['duracion_ms']} ms")
        print(f"   - Filas     : {res['filas_obtenidas']}")
        print(f"   - Datos     : {res['data']}")
        print("-" * 50)
        
    print("\n==================================================================")
    print("         ¡DEMOSTRACIÓN ASÍNCRONA FINALIZADA CON ÉXITO!           ")
    print("==================================================================")

if __name__ == "__main__":
    asyncio.run(main())