from __future__ import annotations
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfgen import canvas
from typing import List, Dict, Any, Optional

class NumberedCanvas(canvas.Canvas):
    """Canvas personalizado para numeración dinámica de páginas (Página X de Y) y pie de página institucional."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._saved_page_states: List[Dict[str, Any]] = []

    def showPage(self) -> None:
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self) -> None:
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count: int) -> None:
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#555555"))
        
        # Línea divisoria de pie de página
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 50, letter[0] - 54, 50)
        
        # Texto del pie de página
        footer_text = f"Reporte Ejecutivo Automatizado | Página {self._pageNumber} de {page_count}"
        self.drawRightString(letter[0] - 54, 35, footer_text)
        
        # Marca de agua institucional superior o pie izquierdo
        self.drawString(54, 35, "Confidencial - Uso Interno")
        self.restoreState()


class ExecutivePDFGenerator:
    """Motor robusto para la generación de informes ejecutivos en PDF estructurados mediante ReportLab."""

    def __init__(self, filename: str) -> None:
        if not filename or not filename.endswith(".pdf"):
            raise ValueError("El archivo de salida debe ser una ruta válida con extensión .pdf")
        self.filename = filename

    def generate_report(self, title: str, subtitle: str, data_rows: List[List[Any]]) -> str:
        """Construye y compila el documento PDF estructurado con Flowables y Canvas maestro."""
        if not title.strip():
            raise ValueError("El título del informe no puede estar vacío.")
        if not data_rows:
            raise ValueError("Las filas de datos para la tabla ejecutiva no pueden estar vacías.")

        try:
            doc = SimpleDocTemplate(
                self.filename,
                pagesize=letter,
                rightMargin=54,
                leftMargin=54,
                topMargin=54,
                bottomMargin=72
            )

            styles = getSampleStyleSheet()
            
            # Estilos personalizados profesionales
            title_style = ParagraphStyle(
                'ExecTitle',
                parent=styles['Heading1'],
                fontName='Helvetica-Bold',
                fontSize=22,
                leading=26,
                textColor=colors.HexColor("#1A365D"),
                spaceAfter=6
            )

            subtitle_style = ParagraphStyle(
                'ExecSubtitle',
                parent=styles['Normal'],
                fontName='Helvetica',
                fontSize=12,
                leading=16,
                textColor=colors.HexColor("#4A5568"),
                spaceAfter=18
            )

            body_style = ParagraphStyle(
                'ExecBody',
                parent=styles['Normal'],
                fontName='Helvetica',
                fontSize=10,
                leading=14,
                textColor=colors.HexColor("#2D3748"),
                spaceAfter=12
            )

            story = []

            # Encabezados del informe
            story.append(Paragraph(title, title_style))
            story.append(Paragraph(subtitle, subtitle_style))
            story.append(Spacer(1, 10))

            intro_text = (
                "El presente documento detalla el resumen ejecutivo consolidado correspondiente "
                "al periodo actual. Los datos reflejan las métricas clave de rendimiento operativo "
                "y financiero procesadas automáticamente por el motor analítico."
            )
            story.append(Paragraph(intro_text, body_style))
            story.append(Spacer(1, 15))

            # Tabla estructurada de datos
            table = Table(data_rows, colWidths=[150, 150, 204])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('TOPPADDING', (0, 0), (-1, 0), 8),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#F7FAFC")),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 9),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))

            story.append(table)

            # Construir documento usando el Canvas dinámico
            doc.build(story, canvasmaker=NumberedCanvas)
            return self.filename

        except Exception as e:
            raise RuntimeError(f"Error crítico al compilar el documento PDF: {str(e)}")