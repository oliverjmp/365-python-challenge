import os
import sqlite3
from pathlib import Path

def auditoria_final_mes1():
    raiz = Path(__file__).parent.parent
    
    # El inventario de tus logros
    componentes = {
        "Base de Datos SQL": raiz / "23-ENERO" / "sistema_bi_oliver.db",
        "Reporte Excel Pro": raiz / "30-ENERO" / "Reporte_Final_Enero.xlsx",
        "Dashboard Visual": raiz / "24-ENERO" / "reporte_gestion_sql.png",
        "Plantilla de Email": raiz / "22-ENERO" / "PLANTILLA_EMAIL_URGENTE.txt"
    }

    print("\n" + "🎊 " * 15)
    print("  FIN DEL MES 1: AUDITORÍA DE SISTEMA BI  ")
    print("🎊 " * 15)

    puntos_logrados = 0
    for nombre, ruta in componentes.items():
        if ruta.exists():
            print(f"✅ {nombre.ljust(20)} | DETECTADO")
            puntos_logrados += 1
        else:
            print(f"❌ {nombre.ljust(20)} | NO ENCONTRADO")

    print("\n" + "="*40)
    print(f"📊 NIVEL DE DESARROLLO: {(puntos_logrados/len(componentes))*100}%")
    
    if puntos_logrados == len(componentes):
        print("🏆 ESTADO: Oliver, eres un Ingeniero de BI certificado.")
    print("="*40)

    # 🚀 Un pequeño mensaje para el futuro
    print("\n🔜 PRÓXIMOS PASOS (MES 2):")
    print("* Automatización con APIs (Conectar con el mundo exterior).")
    print("* Web Scraping (Extraer datos de páginas web reales).")
    print("* Creación de Interfaces Gráficas (Apps de escritorio).")
    print("\n¡Nos vemos mañana para el Día 32!")

if __name__ == "__main__":
    auditoria_final_mes1()