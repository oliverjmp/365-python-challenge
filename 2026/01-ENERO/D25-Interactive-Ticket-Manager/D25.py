import sqlite3
from pathlib import Path

def gestionar_tickets():
    # 1. LOCALIZADOR INTELIGENTE (Busca la DB en todo el proyecto)
    ruta_script = Path(__file__).resolve()
    # Buscamos la carpeta raíz del reto
    raiz_proyecto = next((p for p in ruta_script.parents if p.name == "365-python-challenge"), ruta_script.parent.parent)
    
    print("\n" + "🛠️ " * 15)
    print("SISTEMA DE GESTIÓN DE TICKETS - DÍA 25")
    print("🛠️ " * 15)

    # Buscamos el archivo de la base de datos
    posibles_dbs = list(raiz_proyecto.rglob("sistema_bi_oliver.db"))

    if not posibles_dbs:
        print(f"❌ Error: No se encontró la base de datos en {raiz_proyecto}")
        print("👉 Asegúrate de haber ejecutado el Día 23 primero.")
        return

    ruta_db = posibles_dbs[0]
    print(f"✅ Base de datos conectada en: {ruta_db.name}")

    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    # 2. Mostrar tickets pendientes
    print("\n📋 TICKETS ACTUALMENTE PENDIENTES:")
    cursor.execute("SELECT id, usuario, comentario FROM AlertasCriticas WHERE estado = 'PENDIENTE'")
    pendientes = cursor.fetchall()

    if not pendientes:
        print("✅ ¡Felicidades! No hay tickets pendientes.")
        conexion.close()
        return

    for p in pendientes:
        print(f"ID: {p[0]} | Usuario: {p[1]} | Comentario: {p[2][:50]}...")

    # 3. Interacción: Resolver un ticket
    try:
        entrada = input("\n➡️ Ingresa el ID del ticket para marcar como RESUELTO (o 'q' para salir): ")
        
        if entrada.lower() == 'q':
            print("Saliendo del sistema...")
        else:
            # 4. Actualizar la Base de Datos
            cursor.execute("UPDATE AlertasCriticas SET estado = 'RESUELTO' WHERE id = ?", (entrada,))
            
            if cursor.rowcount > 0:
                conexion.commit()
                print(f"🎉 ¡Éxito! El ticket #{entrada} ahora está RESUELTO.")
            else:
                print(f"⚠️ No se encontró ningún ticket con el ID: {entrada}")

    except Exception as e:
        print(f"❌ Error durante la operación: {e}")

    conexion.close()

if __name__ == "__main__":
    gestionar_tickets()