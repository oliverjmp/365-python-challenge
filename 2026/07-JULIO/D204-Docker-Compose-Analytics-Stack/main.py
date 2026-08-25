from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.analytics_service import AnalyticsService

app = FastAPI(
    title="D204 - Analytics API",
    description="Microservicio analítico impulsado por FastAPI y DuckDB",
    version="1.0.0"
)

analytics = AnalyticsService()

@app.get("/", response_class=HTMLResponse)
def read_root():
    """Renderiza un dashboard HTML profesional con los datos analíticos."""
    try:
        data = analytics.obtener_resumen()
        
        # Construimos filas de la tabla dinámicamente con los datos de DuckDB
        filas_html = ""
        for row in data:
            filas_html += f"""
                <tr>
                    <td>{row.get('categoria')}</td>
                    <td>{row.get('region')}</td>
                    <td>{row.get('total_transacciones')}</td>
                    <td>${row.get('monto_total'):,.2f}</td>
                    <td>${row.get('monto_promedio'):,.2f}</td>
                </tr>
            """
            
        html_content = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>D204 - Dashboard Analítico</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; margin: 0; padding: 40px; color: #333; }}
                .container {{ max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
                h1 {{ color: #1e293b; margin-bottom: 5px; }}
                p.subtitle {{ color: #64748b; margin-top: 0; margin-bottom: 25px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
                th, td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid #e2e8f0; }}
                th {{ background-color: #0f172a; color: white; font-weight: 600; text-transform: uppercase; font-size: 0.85rem; }}
                tr:hover {{ background-color: #f8fafc; }}
                .badge {{ background-color: #22c55e; color: white; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📊 Dashboard Analítico D204</h1>
                <p class="subtitle">Procesamiento de transacciones en tiempo real con FastAPI y DuckDB <span class="badge">ACTIVO</span></p>
                <table>
                    <thead>
                        <tr>
                            <th>Categoría</th>
                            <th>Región</th>
                            <th>Transacciones</th>
                            <th>Monto Total</th>
                            <th>Monto Promedio</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filas_html}
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        """
        return html_content
    except Exception as e:
        return f"<h3>❌ Error al procesar los datos analíticos: {e}</h3>"

@app.get("/analytics/summary")
def get_analytics_summary():
    """Endpoint RESTful puro que mantiene el JSON original."""
    try:
        data = analytics.obtener_resumen()
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}