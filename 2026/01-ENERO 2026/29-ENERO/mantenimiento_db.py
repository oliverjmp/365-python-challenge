import sqlite3
from pathlib import Path

def limpieza_mantenimiento_db():
    # 1. Rutas
    carpeta_actual = Path(__file__).parent
    ruta_db = carpeta_actual.parent / "23-ENERO" / "sistema_bi_oliver.db"

    print("\n" + "🧹 " * 15)
    print("MANTENIMIENTO DE BASE DE DATOS - DÍA 29")
    print("🧹 " * 15)

    if not ruta_db.exists():
        print("❌ Error: Base de datos no encontrada.")
        return

    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    # 2. Mostrar estado actual
    print("\n📊 Registros actuales antes de la limpieza:")
    cursor.execute("SELECT id, usuario, comentario FROM AlertasCriticas")
    for fila in cursor.fetchall():
        print(f"ID: {fila[0]} | {fila[1]}: {fila[2][:30]}...")

    # 3. Operación de Limpieza (Borrar por ID)
    try:
        print("\n" + "-"*30)
        id_a_eliminar = input("⚠️ Ingresa el ID del registro que deseas ELIMINAR (o 'q' para cancelar): ")

        if id_a_eliminar.lower() != 'q':
            # Ejecutar el borrado
            cursor.execute("DELETE FROM AlertasCriticas WHERE id = ?", (id_a_eliminar,))
            
            # 4. Re-ordenar (Opcional en SQL, pero importante confirmar)
            conexion.commit()
            
            if cursor.rowcount > 0:
                print(f"\n✅ Registro #{id_a_eliminar} eliminado correctamente.")
                print("♻️ La base de datos ahora está optimizada.")
            else:
                print("\n❌ No se encontró ningún registro con ese ID.")
                
    except Exception as e:
        print(f"❌ Error durante el mantenimiento: {e}")

    conexion.close()

if __name__ == "__main__":
    limpieza_mantenimiento_db()