import sqlite3
from pathlib import Path

def gestionar_tickets():
    # 1. Rutas y Conexión
    carpeta_actual = Path(__file__).parent
    ruta_db = carpeta_actual.parent / "23-ENERO" / "sistema_bi_oliver.db"

    if not ruta_db.exists():
        print("❌ Error: Base de datos no encontrada.")
        return

    print("\n" + "🛠️ " * 15)
    print("SISTEMA DE GESTIÓN DE TICKETS - DÍA 25")
    print("🛠️ " * 15)

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
        print(f"ID: {p[0]} | Usuario: {p[1]} | Comentario: {p[2][:40]}...")

    # 3. Interacción: Resolver un ticket
    try:
        ticket_id = input("\n➡️ Ingresa el ID del ticket que deseas marcar como RESUELTO (o 'q' para salir): ")
        
        if ticket_id.lower() == 'q':
            print("Saliendo del sistema...")
        else:
            # 4. Actualizar la Base de Datos (SQL UPDATE)
            cursor.execute("UPDATE AlertasCriticas SET estado = 'RESUELTO' WHERE id = ?", (ticket_id,))
            
            if cursor.rowcount > 0:
                conexion.commit()
                print(f"🎉 ¡Éxito! El ticket #{ticket_id} ha sido actualizado a RESUELTO.")
            else:
                print("⚠️ No se encontró ningún ticket con ese ID.")

    except Exception as e:
        print(f"❌ Error durante la actualización: {e}")

    conexion.close()

if __name__ == "__main__":
    gestionar_tickets()