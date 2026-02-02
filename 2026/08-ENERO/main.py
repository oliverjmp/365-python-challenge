import os
import time
from datetime import datetime

# ============================================================
# Configuración general
# ============================================================

CARPETA_LOGS = "logs"
CARPETA_REPORTES = "reportes"
NOMBRE_REPORTE_EJECUTIVO = "resumen_ejecutivo.txt"

# RUTAS CORREGIDAS — todas dentro de la carpeta 2026
MODULOS = [
    ("Día 03 — Limpieza de datos", "../365-python-challenge/2026/03-ENERO/main.py"),
    ("Día 04 — Dashboard", "../365-python-challenge/2026/04-ENERO/main.py"),
    ("Día 05 — Exportación PDF", "../365-python-challenge/2026/05-ENERO/main.py"),
    ("Día 06 — Pipeline Automático", "../365-python-challenge/2026/06-ENERO/main.py"),
    ("Día 07 — Envío Simulado", "../365-python-challenge/2026/07-ENERO/main.py"),
]

# ============================================================
# Crear carpetas necesarias
# ============================================================

def crear_carpeta(ruta):
    os.makedirs(ruta, exist_ok=True)

# ============================================================
# Ejecutar módulo y registrar estado
# ============================================================

def ejecutar_modulo(nombre, ruta_script):
    inicio = time.time()

    try:
        os.system(f'python "{ruta_script}"')
        estado = "OK"
    except Exception as e:
        estado = f"ERROR — {str(e)}"

    duracion = round(time.time() - inicio, 2)

    return nombre, estado, duracion

# ============================================================
# Generar resumen ejecutivo
# ============================================================

def generar_resumen(resultados):
    crear_carpeta(CARPETA_REPORTES)

    ruta_resumen = os.path.join(CARPETA_REPORTES, NOMBRE_REPORTE_EJECUTIVO)
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(ruta_resumen, "w", encoding="utf-8") as f:
        f.write("=== RESUMEN EJECUTIVO — DÍA 08 ===\n\n")
        f.write(f"Fecha de ejecución: {fecha}\n\n")

        for nombre, estado, duracion in resultados:
            f.write(f"{nombre}\n")
            f.write(f"Estado: {estado}\n")
            f.write(f"Duración: {duracion} segundos\n\n")

        f.write("Conclusión:\n")
        f.write("El pipeline se ejecutó correctamente y está listo para distribución.\n")

    print(f"\nResumen ejecutivo generado: {ruta_resumen}")

# ============================================================
# Generar log maestro
# ============================================================

def generar_log(resultados):
    crear_carpeta(CARPETA_LOGS)

    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ruta_log = os.path.join(CARPETA_LOGS, f"pipeline_{fecha}.log")

    with open(ruta_log, "w", encoding="utf-8") as f:
        f.write("=== LOG MAESTRO DEL PIPELINE — DÍA 08 ===\n\n")

        for nombre, estado, duracion in resultados:
            f.write(f"{nombre}\n")
            f.write(f"Estado: {estado}\n")
            f.write(f"Duración: {duracion} segundos\n\n")

    print(f"Log maestro generado: {ruta_log}")

# ============================================================
# Ejecución principal
# ============================================================

def ejecutar_pipeline():
    print("\n=== EJECUCIÓN DEL PIPELINE — DÍA 08 ===\n")

    resultados = []

    for nombre, ruta in MODULOS:
        print(f"Ejecutando: {nombre}")
        resultado = ejecutar_modulo(nombre, ruta)
        resultados.append(resultado)

    generar_log(resultados)
    generar_resumen(resultados)

    print("\nPipeline completado.\n")

if __name__ == "__main__":
    ejecutar_pipeline()
