import sqlite3
from pathlib import Path

def limpieza_mantenimiento_db():
    # 1. LOCALIZADOR INTELIGENTE (Busca la DB en todo el reto 365)
    ruta_script = Path(__file__).resolve()
    try:
        raiz_proyecto = next(p for p in ruta_script.parents if p.name == "365-python-challenge")
    except StopIteration:
        raiz_proyecto = ruta_script.parent.parent.parent

    print("\n" + "🧹 " * 15)
    print("MANTENIMIENTO DE BASE DE DATOS - DÍA 29")
    print("🧹 " * 15)

    # Buscamos la base de datos de forma recursiva
    posibles_dbs = list(raiz_proyecto.rglob("sistema_bi_oliver.db"))

    if not posibles_dbs:
        print(f"❌ Error: No se encontró la base de datos en {raiz_proyecto}")
        return

    ruta_db = posibles_dbs[0]
    print(f"✅ Conectado para mantenimiento: {ruta_db.name}")

    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    # 2. Mostrar estado actual (Solo los últimos 10 para no saturar)
    print("\n📊 VISTA PREVIA DE REGISTROS ACTUALES:")
    print(f"{'ID':<5} | {'USUARIO':<15} | {'COMENTARIO'}")
    print("-" * 50)
    
    cursor.execute("SELECT id, usuario, comentario FROM AlertasCriticas ORDER BY id DESC LIMIT 10")
    for fila in cursor.fetchall():
        print(f"{fila[0]:<5} | {fila[1]:<15} | {fila[2][:40]}...")

    # 3. Operación de Limpieza (Borrado por ID)
    try:
        print("\n" + "-"*30)
        id_a_eliminar = input("⚠️ Ingresa el ID del registro que deseas ELIMINAR (o 'q' para cancelar): ")

        if id_a_eliminar.lower() == 'q':
            print("🚀 Mantenimiento cancelado. No se realizaron cambios.")
        else:
            # Verificación previa: ¿Existe el ID?
            cursor.execute("SELECT id FROM AlertasCriticas WHERE id = ?", (id_a_eliminar,))
            if not cursor.fetchone():
                print(f"\n❌ Error: No se encontró ningún registro con el ID: {id_a_eliminar}")
            else:
                # Ejecutar el borrado definitivo
                cursor.execute("DELETE FROM AlertasCriticas WHERE id = ?", (id_a_eliminar,))
                conexion.commit()
                
                if cursor.rowcount > 0:
                    print(f"\n✅ Registro #{id_a_eliminar} ELIMINADO correctamente.")
                    print("♻️ Espacio liberado y base de datos optimizada.")
                
    except Exception as e:
        print(f"❌ Error durante el mantenimiento: {e}")

    conexion.close()

if __name__ == "__main__":
    limpieza_mantenimiento_db()