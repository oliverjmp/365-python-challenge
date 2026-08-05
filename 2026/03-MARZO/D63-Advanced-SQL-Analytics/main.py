import logging
import sys
from database import init_database
from models import FinancialTrendRecord
from queries import ADVANCED_FINANCIAL_TRENDS_QUERY

# Configuración de logging estructurado para el orquestador
logger = logging.getLogger("PipelineOrchestrator")


def run_pipeline() -> None:
    logger.info(
        "=== [D63] INICIANDO MOTOR DE SQL AVANZADO Y ANALÍTICA FINANCIERA ==="
    )

    conn = None
    try:
        # 1. Inicializar base de datos persistente
        conn = init_database("analytics.db")
        cursor = conn.cursor()

        # 2. Ejecutar consulta SQL analítica avanzada
        logger.info(
            "Ejecutando CTEs y Window Functions en el motor de base de datos..."
        )
        cursor.execute(ADVANCED_FINANCIAL_TRENDS_QUERY)
        rows = cursor.fetchall()

        # 3. Mapear y validar resultados estrictamente con Pydantic v2
        validated_records = []
        for row in rows:
            record = FinancialTrendRecord(
                transaction_date=row[0],
                category=row[1],
                daily_amount=row[2],
                moving_average_7d=row[3],
                previous_day_amount=row[4],
                trend_deviation_pct=row[5],
            )
            validated_records.append(record)

        logger.info(
            f"Se procesaron y validaron con éxito {len(validated_records)} registros analíticos."
        )

        # 4. Presentar resultados en consola de forma estructurada
        print(
            f"\n[ÉXITO] Resultados del Análisis Financiero Avanzado ({len(validated_records)} filas):\n"
        )
        print(
            f"{'Fecha':<12} | {'Categoría':<10} | {'Monto':<10} | {'Media 7D':<10} | {'Día Prev':<10} | {'Desv. Tendencia (%)':<20}"
        )
        print("-" * 85)

        for rec in validated_records:
            print(
                f"{str(rec.transaction_date):<12} | "
                f"{rec.category:<10} | "
                f"{rec.daily_amount:<10.2f} | "
                f"{rec.moving_average_7d:<10.2f} | "
                f"{rec.previous_day_amount:<10.2f} | "
                f"{rec.trend_deviation_pct:<20.2f}%"
            )

    except Exception as e:
        logger.error(
            f"[ERROR CRÍTICO] Falló la ejecución del pipeline analítico: {e}",
            exc_info=True,
        )
        sys.exit(1)
    finally:
        if conn:
            conn.close()
            logger.info(
                "=== [D63] PIPELINE FINALIZADO Y CONEXIÓN CERRADA CORRECTAMENTE ==="
            )


if __name__ == "__main__":
    run_pipeline()