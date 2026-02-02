import os
import subprocess
import time
from datetime import datetime

# ============================================================
# Función para ejecutar scripts y mostrar progreso
# ============================================================

def ejecutar_script(nombre, ruta):
    print(f"[...] Ejecutando {nombre}...")
    inicio = time.time()

    resultado = subprocess.run(
        ["python", ruta],
        capture_output=True,
        text=True
    )

    duracion = round(time.time() - inicio, 2)

    if resultado.returncode == 0:
        print(f"[OK] {nombre} completado en {duracion}s\n")
        return True, duracion, resultado.stdout
    else:
        print(f"[ERROR] {nombre} falló\n")
        return False, duracion, resultado.stderr

# ============================================================
# Crear carpeta de logs
# ============================================================

def crear_carpeta_logs():
    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(carpeta, exist_ok=True)
    return carpeta

# ============================================================
# Guardar log
# ============================================================

def guardar_log(contenido):
    carpeta_logs = crear_carpeta_logs()
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ruta_log = os.path.join(carpeta_logs, f"pipeline_{fecha}.log")

    with open(ruta_log, "w", encoding="utf-8") as f:
        f.write(contenido)

    print(f"Log guardado en: {ruta_log}")

# ============================================================
# Ejecución principal del pipeline
# ============================================================

if __name__ == "__main__":
    print("\n=== PIPELINE AUTOMÁTICO — DÍA 06 ===\n")

    base = os.path.dirname(os.path.abspath(__file__))

    scripts = [
        ("Día 03 — Limpieza de Datos", os.path.join(base, "..", "03-ENERO", "main.py")),
        ("Día 04 — Dashboard Premium", os.path.join(base, "..", "04-ENERO", "main.py")),
        ("Día 05 — Exportación PDF", os.path.join(base, "..", "05-ENERO", "main.py")),
    ]

    log = []
    inicio_total = time.time()

    for nombre, ruta in scripts:
        ok, duracion, salida = ejecutar_script(nombre, ruta)
        log.append(f"{nombre}: {'OK' if ok else 'ERROR'} — {duracion}s\nSalida:\n{salida}\n")

        if not ok:
            log.append("Pipeline detenido por error.\n")
            guardar_log("\n".join(log))
            exit()

    duracion_total = round(time.time() - inicio_total, 2)
    log.append(f"Pipeline completado correctamente en {duracion_total}s.\n")

    print(f"Pipeline completado correctamente en {duracion_total}s.\n")

    guardar_log("\n".join(log))
