import time
import logging
import os
import pandas as pd
import json
from datetime import datetime

# --- CONFIGURACIÓN DE RUTAS AUTOMÁTICA ---
# Esto detecta la carpeta real donde está el archivo D14.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RULES_PATH = os.path.join(BASE_DIR, "rules.json")
WATCH_FOLDER = os.path.join(BASE_DIR, "watch_folder")
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(WATCH_FOLDER, exist_ok=True)

# --- IMPORTACIÓN LÓGICA DEL DÍA 13 ---
def cargar_reglas():
    if os.path.exists(RULES_PATH):
        with open(RULES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def validar_calidad(ruta_archivo, rules):
    try:
        df = pd.read_csv(ruta_archivo, encoding='utf-8-sig')
    except:
        df = pd.read_csv(ruta_archivo, encoding='latin1')
    
    dups = df.duplicated().sum()
    nulos = df.isnull().sum().sum()
    celdas_totales = df.size if df.size > 0 else 1
    
    health_score = max(0, 100 - ((nulos / celdas_totales) * 100) - ((dups / len(df)) * 100 if len(df)>0 else 0))
    return health_score, len(df)

# --- CONFIGURACIÓN DE LOGS ---
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "sistema_integrado.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def monitorear_y_validar(ruta, intervalo=3):
    rules = cargar_reglas()
    if not rules:
        print(f"❌ Error: No se encontró rules.json en: {RULES_PATH}")
        return

    print(f"🚀 SISTEMA ACTIVO")
    print(f"📂 Vigilando: {ruta}")
    print(f"⚙️ Reglas cargadas desde: {RULES_PATH}")
    
    estado_anterior = {f: os.path.getmtime(os.path.join(ruta, f)) 
                       for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))}

    try:
        while True:
            time.sleep(intervalo)
            archivos_actuales = os.listdir(ruta)
            estado_actual = {f: os.path.getmtime(os.path.join(ruta, f)) 
                             for f in archivos_actuales if os.path.isfile(os.path.join(ruta, f))}

            nuevos = set(estado_actual.keys()) - set(estado_anterior.keys())
            
            for archivo in nuevos:
                ruta_completa = os.path.join(ruta, archivo)
                print(f"\n🟢 NUEVO: {archivo}")
                
                if archivo.endswith(".csv"):
                    score, filas = validar_calidad(ruta_completa, rules)
                    color = "✅" if score > 80 else "⚠️"
                    print(f"{color} Calidad: {round(score,1)}% | Filas: {filas}")
                else:
                    print(f"ℹ️ Ignorado (No es CSV)")

            eliminados = set(estado_anterior.keys()) - set(estado_actual.keys())
            for archivo in eliminados:
                print(f"🔴 ELIMINADO: {archivo}")

            estado_anterior = estado_actual.copy()

    except KeyboardInterrupt:
        print("\n🛑 Monitoreo detenido.")

if __name__ == "__main__":
    monitorear_y_validar(WATCH_FOLDER)