import os
import win32com.client as win32
from datetime import datetime

# ============================================================
# Obtener ruta del Excel generado en el Día 4
# ============================================================

def obtener_ruta_excel():
    carpeta = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(carpeta, "..", "04-ENERO", "informe_cripto.xlsx"))

# ============================================================
# Configurar todas las hojas antes de exportar
# ============================================================

def configurar_hojas(wb):
    fecha = datetime.now().strftime("%d/%m/%Y")
    pie = f"Oliver Javier Morales Pérez — 365 Python Challenge — {fecha}"

    for hoja in wb.Worksheets:
        hoja.PageSetup.Orientation = 2               # Horizontal
        hoja.PageSetup.Zoom = False
        hoja.PageSetup.FitToPagesWide = 1            # Ajustar ancho
        hoja.PageSetup.FitToPagesTall = False        # Alto libre
        hoja.PageSetup.LeftMargin = 20
        hoja.PageSetup.RightMargin = 20
        hoja.PageSetup.TopMargin = 20
        hoja.PageSetup.BottomMargin = 20
        hoja.PageSetup.CenterHorizontally = True

        # ✔ CORREGIDO: Excel no permite FooterCenter, pero sí CenterFooter
        hoja.PageSetup.CenterFooter = pie

# ============================================================
# Exportar a PDF
# ============================================================

def exportar_pdf(ruta_excel):
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_pdf = os.path.join(carpeta, "informe_cripto.pdf")

    excel = win32.Dispatch("Excel.Application")
    excel.Visible = False

    wb = excel.Workbooks.Open(ruta_excel)
    configurar_hojas(wb)

    # Exportar portada + tabla + marketcap + gráficos
    wb.WorkSheets([1, 2, 3, 4]).Select()

    wb.ExportAsFixedFormat(0, ruta_pdf)

    wb.Close()
    excel.Quit()

    print(f"PDF generado correctamente en:\n{ruta_pdf}")

# ============================================================
# Ejecución principal
# ============================================================

if __name__ == "__main__":
    exportar_pdf(obtener_ruta_excel())
    print("Día 5 PREMIUM EJECUTIVO completado.")
