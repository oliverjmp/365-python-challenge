from __future__ import annotations
import os
import io
import matplotlib
matplotlib.use('Agg') # Usar backend no interactivo para evitar problemas en entornos headless
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from typing import List, Tuple, Any

class ChartPDFPipeline:
    """Pipeline automatizado para generar gráficos estadísticos con Matplotlib e incrustarlos en informes PDF ejecutivos."""

    def __init__(self, output_filename: str) -> None:
        if not output_filename or not output_filename.endswith(".pdf"):
            raise ValueError("La ruta del archivo de salida debe ser válida y tener extensión .pdf")
        self.output_filename = output_filename

    def generate_chart_image(self, categories: List[str], values: List[float]) -> io.BytesIO:
        """Genera un gráfico de barras estadístico con Matplotlib y lo retorna en memoria como un buffer de bytes."""
        if not categories or not values or len(categories) != len(values):
            raise ValueError("Las categorías y valores no pueden estar vacíos y deben tener la misma longitud.")

        try:
            fig, ax = plt.subplots(figsize=(6, 3.2), dpi=150)
            
            # Estilos profesionales de Matplotlib
            bars = ax.bar(categories, values, color='#2B6CB0', width=0.55, edgecolor='#1A365D', linewidth=0.8)
            
            ax.set_title("Rendimiento Comercial por Categoría", fontsize=11, fontweight='bold', color='#1A365D', pad=12)
            ax.set_ylabel("Valor Monetario (USD)", fontsize=9, color='#4A5568')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_color('#CBD5E0')
            ax.spines['bottom'].set_color('#CBD5E0')
            ax.tick_params(axis='both', colors='#4A5568', labelsize=8)
            ax.grid(axis='y', linestyle='--', alpha=0.5, color='#E2E8F0')

            # Añadir etiquetas de valor sobre las barras
            for bar in bars:
                height = bar.get_height()
                ax.annotate(f'${height:,.0f}',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 4),  # Desplazamiento vertical de 4 puntos
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=8, color='#2D3748', fontweight='bold')

            plt.tight_layout()

            # Guardar en búfer de memoria en formato PNG de alta calidad
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png', bbox_inches='tight')
            buffer.seek(0)
            plt.close(fig)
            return buffer

        except Exception as e:
            raise RuntimeError(f"Error crítico al renderizar el gráfico estadístico: {str(e)}")

    def build_report_with_chart(self, title: str, categories: List[str], values: List[float], summary_table_data: List[List[Any]]) -> str:
        """Construye el informe PDF completo incrustando el gráfico generado en memoria y una tabla resumen."""
        if not title.strip():
            raise ValueError("El título del informe no puede estar vacío.")
        if not summary_table_data:
            raise ValueError("Los datos de la tabla resumen no pueden estar vacíos.")

        try:
            doc = SimpleDocTemplate(
                self.output_filename,
                pagesize=letter,
                rightMargin=54,
                leftMargin=54,
                topMargin=54,
                bottomMargin=54
            )

            styles = getSampleStyleSheet()
            
            title_style = ParagraphStyle(
                'ReportTitle',
                parent=styles['Heading1'],
                fontName='Helvetica-Bold',
                fontSize=20,
                leading=24,
                textColor=colors.HexColor("#1A365D"),
                spaceAfter=4
            )

            subtitle_style = ParagraphStyle(
                'ReportSubtitle',
                parent=styles['Normal'],
                fontName='Helvetica',
                fontSize=11,
                leading=15,
                textColor=colors.HexColor("#4A5568"),
                spaceAfter=14
            )

            story = []

            # Encabezados
            story.append(Paragraph(title, title_style))
            story.append(Paragraph("Informe analítico automatizado con integración gráfica Matplotlib + ReportLab.", subtitle_style))
            story.append(Spacer(1, 5))

            # Obtener gráfico en memoria e incrustarlo como Flowable Image
            chart_buffer = self.generate_chart_image(categories, values)
            chart_image = Image(chart_buffer, width=450, height=240)
            story.append(chart_image)
            story.append(Spacer(1, 15))

            # Tabla resumen estructurada
            table = Table(summary_table_data, colWidths=[150, 150, 204])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 9),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
                ('TOPPADDING', (0, 0), (-1, 0), 6),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#F7FAFC")),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 9),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))

            story.append(table)

            doc.build(story)
            return self.output_filename

        except (ValueError, RuntimeError) as e:
            raise e
        except Exception as e:
            raise RuntimeError(f"Error crítico al compilar el PDF con gráficos: {str(e)}")