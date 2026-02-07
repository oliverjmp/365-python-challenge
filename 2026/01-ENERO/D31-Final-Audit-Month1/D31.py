import os
import sqlite3
from pathlib import Path

def auditoria_final_mes1():
    # 1. Localización inteligente de la raíz
    ruta_script = Path(__file__).resolve()
    try:
        raiz = next(p for p in ruta_script.parents if p.name == "365-python-challenge")
    except StopIteration:
        raiz = ruta_script.parent.parent.parent
    
    # 2. El inventario de tus logros (Búsqueda por nombre de archivo)
    componentes = {
        "Base de Datos SQL": "sistema_bi_oliver.db",
        "Reporte Excel Pro": "Reporte_Final_Enero_Oliver.xlsx",
        "Dashboard Visual": "reporte_gestion_sql.png",
        "Plantilla Email": "PLANTILLA_EMAIL_URGENTE.txt"
    }

    print("\n" + "🎊 " * 15)
    print("   FIN DEL MES 1: AUDITORÍA DE SISTEMA BI   ")
    print("🎊 " * 15)

    puntos_logrados = 0
    for nombre, archivo in componentes.items():
        # Buscamos el archivo en todo el proyecto
        hallado = list(raiz.rglob(archivo))
        if hallado:
            print(f"✅ {nombre.ljust(20)} | DETECTADO en: {hallado[0].parent.name}")
            puntos_logrados += 1
        else:
            print(f"❌ {nombre.ljust(20)} | NO ENCONTRADO")

    print("\n" + "="*45)
    print(f"📊 NIVEL DE DESARROLLO: {(puntos_logrados/len(componentes))*100}%")
    
    if puntos_logrados == len(componentes):
        print("🏆 ESTADO: ¡Oliver, eres un Ingeniero de BI Certificado!")
        print("   Has completado el pipeline de datos de extremo a extremo.")
    print("="*45)

    # 🚀 Preparación para el Mes 2 (Febrero)
    print("\n🔜 PRÓXIMOS PASOS (MES 2):")
    print("🔹 APIs & JSON: Conexión con servicios en la nube.")
    print("🔹 Web Scraping: Tu primera araña para extraer datos de la web.")
    print("🔹 GUI: De la consola a las ventanas con botones.")
    
    # Crear carpeta de Febrero automáticamente
    ruta_feb = raiz / "2026" / "02-FEBRERO"
    ruta_feb.mkdir(parents=True, exist_ok=True)
    print(f"\n📂 Carpeta de Febrero lista para mañana en: {ruta_feb.name}")
    
    print("\n¡Nos vemos mañana para el Día 32! El reto sigue... 🚀")

if __name__ == "__main__":
    auditoria_final_mes1()