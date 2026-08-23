from __future__ import annotations
import pandas as pd
from ydata_profiling import ProfileReport
from typing import Optional

class DataAuditorEngine:
    """Motor automatizado para la auditoría exploratoria de datos y generación de reportes interactivos."""

    def __init__(self, df: pd.DataFrame) -> None:
        if df is None or df.empty:
            raise ValueError("El DataFrame de entrada no puede ser nulo ni estar vacío.")
        self.df = df

    def generate_profile_report(self, title: str = "Reporte de Auditoría Exploratoria", explorative: bool = True) -> ProfileReport:
        """Genera y retorna el objeto ProfileReport de YData Profiling."""
        try:
            profile = ProfileReport(self.df, title=title, explorative=explorative)
            return profile
        except Exception as e:
            raise RuntimeError(f"Error crítico al generar el reporte de auditoría: {str(e)}")

    def export_report_to_html(self, output_path: str, title: str = "Reporte de Auditoría Exploratoria") -> str:
        """Exporta el reporte analítico interactivo directamente a un archivo HTML."""
        if not output_path.endswith(".html"):
            raise ValueError("La ruta de salida debe especificar un archivo con extensión .html")
        
        profile = self.generate_profile_report(title=title)
        profile.to_file(output_path)
        return output_path