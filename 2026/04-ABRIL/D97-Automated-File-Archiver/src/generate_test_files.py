import os
import pandas as pd
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_sample_files(output_dir: str = "./data/entrada") -> None:
    """Genera ficheros de prueba de diferentes extensiones en la carpeta de entrada."""
    target_path = Path(output_dir)
    target_path.mkdir(parents=True, exist_ok=True)
    
    # 1. Crear un archivo Excel (.xlsx)
    excel_path = target_path / "test_productos.xlsx"
    df_excel = pd.DataFrame({
        "ID": [101, 102, 103],
        "Producto": ["Laptop", "Mouse", "Teclado"],
        "Precio": [1200.50, 25.00, 45.00]
    })
    df_excel.to_excel(excel_path, index=False, sheet_name="Productos")
    print(f"Creado: {excel_path.name}")

    # 2. Crear un archivo de texto plano (.txt)
    txt_path = target_path / "test_notas.txt"
    txt_path.write_text("Nota de prueba para el sistema de archivo automatizado D97.\nLínea adicional de texto.", encoding="utf-8")
    print(f"Creado: {txt_path.name}")

    # 3. Crear un archivo PDF (.pdf) usando ReportLab
    pdf_path = target_path / "test_documento.pdf"
    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    c.drawString(100, 750, "Documento PDF de prueba generado para D97.")
    c.save()
    print(f"Creado: {pdf_path.name}")

    # 4. Crear un archivo de imagen simulado (.png)
    png_path = target_path / "test_imagen.png"
    # Bytes mínimos válidos para una imagen PNG de 1x1 píxel
    png_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
    png_path.write_bytes(png_bytes)
    print(f"Creado: {png_path.name}")

if __name__ == "__main__":
    print("--- Generando archivos de prueba para D97 ---")
    create_sample_files()
    print("¡Archivos creados con éxito en la carpeta data/entrada/!")