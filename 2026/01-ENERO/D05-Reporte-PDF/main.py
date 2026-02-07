import win32com.client as win32
import pythoncom
import sys
import os
from datetime import datetime
from pathlib import Path

# ============================================================
# CONFIGURACIÓN DE RUTAS DINÁMICAS
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
RUTA_EXCEL_DIA4 = BASE_DIR.parent / "D04-Graficos-Excel" / "informe_cripto_premium.xlsx"
RUTA_PDF_FINAL = BASE_DIR / "informe_cripto_ejecutivo.pdf"

def configurar_layout_pdf(wb):
    fecha = datetime.now().strftime("%d/%m/%Y")
    pie_pagina = f"Oliver Javier Morales Perez - 365 Python Challenge - {fecha}"

    for hoja in wb.Worksheets:
        setup = hoja.PageSetup
        setup.Orientation = 2            # xlLandscape
        setup.Zoom = False
        setup.FitToPagesWide = 1
        setup.FitToPagesTall = False
        setup.CenterHorizontally = True
        
        # Pie de página central (sin caracteres especiales problemáticos)
        setup.CenterFooter = pie_pagina

def generar_pdf():
    if not RUTA_EXCEL_DIA4.exists():
        print(f"STDERR: No se encuentra el origen en {RUTA_EXCEL_DIA4}")
        return False

    excel = None
    try:
        # Inicializar el motor COM para hilos
        pythoncom.CoInitialize()
        
        # Intentar conectar con Excel
        excel = win32.DispatchEx("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False

        print(f"Abriendo Excel Premium...")
        wb = excel.Workbooks.Open(str(RUTA_EXCEL_DIA4))
        
        configurar_layout_pdf(wb)

        # Seleccionamos las hojas (aseguramos que existen 4 hojas)
        try:
            wb.WorkSheets([1, 2, 3]).Select() # Seleccionamos las principales
        except:
            wb.ActiveSheet.Select() # Fallback si hay menos hojas

        print("Exportando a PDF...")
        # Type=0 es xlTypePDF
        wb.ActiveSheet.ExportAsFixedFormat(0, str(RUTA_PDF_FINAL))
        
        wb.Close(False)
        print("D05_OK: PDF Generado.")
        return True

    except Exception as e:
        print(f"STDERR: Error en conversion PDF: {e}")
        return False
    finally:
        if excel:
            excel.Quit()
        pythoncom.CoUninitialize()

if __name__ == "__main__":
    # Aseguramos el directorio de trabajo
    os.chdir(str(BASE_DIR))
    
    print("Iniciando D05 - Exportacion PDF...")
    if generar_pdf():
        sys.exit(0)
    else:
        sys.exit(1)
