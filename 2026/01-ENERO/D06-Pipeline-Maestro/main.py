import subprocess
import time
import sys
import io
from datetime import datetime
from pathlib import Path

# ============================================================
# SOLUCIÓN AL ERROR 'CHARMAP': Forzar UTF-8 en Windows
# ============================================================
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# ============================================================
# CONFIGURACIÓN DE RUTAS DINÁMICAS
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent 

# RUTA DEL EJECUTABLE QUE FUNCIONA EN TU SISTEMA
PYTHON_EXE = r"C:/Users/olive/AppData/Local/Programs/Python/Python313/python.exe"

SCRIPTS_PIPELINE = [
    ("D01 - ETL Clima", ROOT_DIR / "D01-ETL-Clima" / "main.py"),
    ("D02 - Crypto API", ROOT_DIR / "D02-Scraper-Avanzado" / "main.py"),
    ("D03 - Excel Format", ROOT_DIR / "D03-Excel-Profesional" / "main.py"),
    ("D04 - Dashboard", ROOT_DIR / "D04-Graficos-Excel" / "main.py"),
    ("D05 - Export PDF", ROOT_DIR / "D05-Reporte-PDF" / "main.py"),
]

def ejecutar_paso(nombre, ruta):
    print(f"🚀 [{nombre}] Iniciando...")
    
    if not ruta.exists():
        return False, 0, f"ERROR: No se encontro el archivo en {ruta}"

    inicio = time.time()
    script_folder = ruta.parent
    
    try:
        # Ejecución forzando el Python correcto y el directorio de trabajo
        resultado = subprocess.run(
            [PYTHON_EXE, str(ruta)],
            capture_output=True,
            text=False, 
            cwd=str(script_folder)
        )
        
        # ============================================================
        # DECODIFICACIÓN ULTRA-ROBUSTA (IGNORA EMOJIS PROBLEMÁTICOS)
        # ============================================================
        def safe_decode(b_data):
            if not b_data: return ""
            # Intentamos decodificar ignorando caracteres que den error en Windows
            for encoding in ['utf-8', 'cp1252', 'latin-1']:
                try:
                    return b_data.decode(encoding, errors='ignore') # <--- CLAVE DEL ÉXITO
                except UnicodeDecodeError:
                    continue
            return b_data.decode('utf-8', errors='replace')

        stdout = safe_decode(resultado.stdout)
        stderr = safe_decode(resultado.stderr)
        duracion = round(time.time() - inicio, 2)
        
        if resultado.returncode == 0:
            print(f"✅ {nombre} finalizado con exito ({duracion}s)")
            return True, duracion, stdout
        else:
            print(f"❌ {nombre} fallo.")
            # Si falla, imprimimos el error en consola para verlo rápido
            if stderr: print(f"DETALLE ERROR: {stderr}")
            return False, duracion, f"STDOUT: {stdout}\nSTDERR: {stderr}"
            
    except Exception as e:
        return False, 0, f"Error sistemico: {str(e)}"

def guardar_historial(contenido):
    logs_dir = BASE_DIR / "logs"
    logs_dir.mkdir(exist_ok=True)
    nombre_log = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    ruta_log = logs_dir / nombre_log
    with open(ruta_log, "w", encoding="utf-8") as f:
        f.write(contenido)
    return ruta_log

if __name__ == "__main__":
    print("\n" + "="*60)
    print("💎 MASTER PIPELINE ORCHESTRATOR — V4.1 (ANTI-CHARMAP)")
    print("="*60 + "\n")

    inicio_total = time.time()
    reporte = []
    exito_global = True

    for nombre, ruta in SCRIPTS_PIPELINE:
        ok, t, output = ejecutar_paso(nombre, ruta)
        
        status = "SUCCESS" if ok else "FAILED"
        reporte.append(f"STEP: {nombre}\nSTATUS: {status}\nTIME: {t}s\nLOG:\n{output}\n{'-'*40}")
        
        if not ok:
            exito_global = False
            print(f"\n🛑 PIPELINE INTERRUMPIDO EN {nombre}")
            break

    duracion_total = round(time.time() - inicio_total, 2)
    resumen = f"\nRESULTADO GLOBAL: {'EXITOSO' if exito_global else 'FALLIDO'}\nTIEMPO TOTAL: {duracion_total}s"
    
    log_file = guardar_historial("\n".join(reporte) + resumen)
    
    print("\n" + "="*60)
    print(resumen)
    print(f"DETALLE LOG: logs/{log_file.name}")
    print("="*60)