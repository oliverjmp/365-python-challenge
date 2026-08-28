import pandas as pd
from src.subsystems import (
    ArrowMemoryManagementSubsystem,
    ColumnarIngestionSubsystem,
    AnalyticalProcessingSubsystem
)

class AnalyticsCoreFacade:
    """Fachada unificada que encapsula la complejidad del núcleo analítico basado en Arrow."""
    def __init__(self):
        self.memory_subsystem = ArrowMemoryManagementSubsystem()
        self.ingestion_subsystem = ColumnarIngestionSubsystem()
        self.analytical_subsystem = AnalyticalProcessingSubsystem()

    def execute_pipeline(self, df: pd.DataFrame) -> dict:
        """Ejecuta de forma transparente la monitorización de memoria, ingesta y analítica."""
        pre_stats = self.memory_subsystem.get_active_pool_stats()
        arrow_table = self.ingestion_subsystem.ingest_to_arrow(df)
        metrics = self.analytical_subsystem.compute_metrics(arrow_table)
        post_stats = self.memory_subsystem.get_active_pool_stats()

        return {
            "initial_memory": pre_stats,
            "analytical_metrics": metrics,
            "final_memory": post_stats
        }