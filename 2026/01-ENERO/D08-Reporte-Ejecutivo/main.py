import subprocess
import time
import sys
from datetime import datetime
from pathlib import Path

# ============================================================
# CONFIGURACIÓN DE RUTAS DINÁMICAS (Robustez Total)
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent # Apunta a la carpeta 2026/

# Mapeo exacto de tus carpetas actuales
MODULOS = [
    ("Día 03 - Formato Excel", ROOT_DIR / "D03-Excel-Profesional" / "main.py"),
    ("Día 04 - Dashboard", ROOT_DIR / "D04-Graficos-Excel" / "main.py"),
    ("Día 05 - Exportación PDF", ROOT_DIR / "D05-Reporte-PDF" / "main.py"),
    ("Día 07 - Envío Simulado", ROOT_DIR / "D07-Envio-Email" / "main.py"),
]

PYTHON_EXE = sys.executable # Usa el Python activo automáticamente

def ejecutar_modulo(nombre, ruta_script):
    print(f"--> Ejecutando: {nombre}")
    inicio = time.time()
    
    if not ruta_script.exists():
        return nombre, "ERROR: No encontrado", 0

    try:
        # Ejecutamos el script de forma silenciosa para el reporte
        resultado = subprocess.run(
            [PYTHON_EXE, str(ruta_script)],
            capture_output=True,
            text=True,
            cwd=str(ruta_script.parent)
        )
        estado = "OK" if resultado.returncode == 0 else "ERROR (Script Falló)"
    except Exception as e:
        estado = f"ERROR SISTEMICO: {str(e)}"

    duracion = round(time.time() - inicio, 2)
    return nombre, estado, duracion

def generar_reportes(resultados):
    # Crear carpetas
    (BASE_DIR / "logs").mkdir(exist_ok=True)
    (BASE_DIR / "reportes").mkdir(exist_ok=True)
    
    fecha_hoy = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    fecha_file = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    ruta_resumen = BASE_DIR / "reportes" / "resumen_ejecutivo.txt"
    
    with open(ruta_resumen, "w", encoding="utf-8") as f:
        f.write(f"=== RESUMEN EJECUTIVO - PIPELINE V1.0 ===\n")
        f.write(f"Fecha: {fecha_hoy}\n")
        f.write("-" * 40 + "\n")
        
        for nombre, estado, duracion in resultados:
            f.write(f"Modulo: {nombre}\n")
            f.write(f"Estado: {estado}\n")
            f.write(f"Tiempo: {duracion}s\n")
            f.write("." * 20 + "\n")
            
        f.write("\nConclusion: Proceso verificado y auditado.\n")
    
    print(f"\nResumen generado en: {ruta_resumen.name}")

if __name__ == "__main__":
    print("=== MONITOR DE PIPELINE - DIA 08 ===\n")
    resultados_finales = []
    
    for nombre, ruta in MODULOS:
        res = ejecutar_modulo(nombre, ruta)
        resultados_finales.append(res)
    
    generar_reportes(resultados_finales)
    print("\nAuditoria completada.")