from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.shapes import Drawing, Rect, String, Circle
from pathlib import Path
from typing import Dict, Any

class ExecutiveReportGenerator:
    def __init__(self, output_filename: str = "output_report.pdf"):
        self.output_filename = output_filename

    def create_vector_chart(self) -> Drawing:
        """Genera un gráfico vectorial embebido personalizado utilizando figuras geométricas de ReportLab."""
        d = Drawing(400, 150)
        # Fondo del gráfico
        d.add(Rect(0, 0, 400, 150, fillColor=colors.HexColor("#f8f9fa"), strokeColor=colors.HexColor("#dee2e6"), strokeWidth=1))
        # Título interno del gráfico
        d.add(String(20, 120, "Resumen de Rendimiento Trimestral (Vectorial)", fontSize=12, fillColor=colors.HexColor("#343a40"), fontName="Helvetica-Bold"))
        
        # Barras simuladas de ejemplo
        bars = [("Q1", 60, colors.HexColor("#4dabf7")), 
                ("Q2", 90, colors.HexColor("#3b5bdb")), 
                ("Q3", 75, colors.HexColor("#748ffc")), 
                ("Q4", 110, colors.HexColor("#1971c2"))]
        
        x_offset = 50
        for label, val, color in bars:
            bar_height = val
            d.add(Rect(x_offset, 30, 40, bar_height, fillColor=color, strokeColor=None))
            d.add(String(x_offset + 12, 15, label, fontSize=10, fillColor=colors.HexColor("#495057")))
            x_offset += 80

        return d

    def generate_pdf(self, report_data: Dict[str, Any]) -> str:
        """Construye y compila el documento PDF ejecutivo completo."""
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
            'ExecutiveTitle',
            parent=styles['Heading1'],
            fontSize=22,
            leading=26,
            textColor=colors.HexColor("#1a365d"),
            spaceAfter=15
        )
        
        body_style = ParagraphStyle(
            'ExecutiveBody',
            parent=styles['Normal'],
            fontSize=10,
            leading=14,
            textColor=colors.HexColor("#2d3748"),
            spaceAfter=10
        )

        story = []

        # Título principal del reporte
        story.append(Paragraph(report_data.get("title", "Reporte Ejecutivo Automatizado"), title_style))
        story.append(Paragraph(f"<b>Fecha de emisión:</b> {report_data.get('date', 'N/A')}", body_style))
        story.append(Paragraph(f"<b>Autor/Sistema:</b> {report_data.get('author', 'Motor Python')}", body_style))
        story.append(Spacer(1, 15))

        # Sección de texto descriptivo
        story.append(Paragraph("Este informe detalla las métricas operativas recopiladas de forma automatizada por el sistema. Los gráficos a continuación representan el comportamiento consolidado por periodos.", body_style))
        story.append(Spacer(1, 10))

        # Embeber gráfico vectorial
        story.append(self.create_vector_chart())
        story.append(Spacer(1, 20))

        # Tabla de datos detallados
        story.append(Paragraph("<b>Desglose Tabular de Métricas</b>", body_style))
        
        table_data = [
            ["Trimestre", "Métrica Clave", "Estado"],
            ["Q1", "1,240 transacciones", "Completado"],
            ["Q2", "2,100 transacciones", "Completado"],
            ["Q3", "1,850 transacciones", "En revisión"],
            ["Q4", "3,400 transacciones", "Proyectado"]
        ]

        t = Table(table_data, colWidths=[100, 200, 150])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1a365d")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (-1,0), 8),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#f7fafc")),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e0")),
            ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
            ('FONTSIZE', (0,1), (-1,-1), 9),
        ]))
        
        story.append(t)

        # Construir documento
        doc.build(story)
        return self.output_filename