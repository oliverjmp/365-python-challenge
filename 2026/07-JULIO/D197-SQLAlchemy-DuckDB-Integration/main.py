from orm_engine import DuckDBORMManager

def main():
    print("🚀 Iniciando integración de SQLAlchemy con DuckDB...")
    
    # Instanciamos el gestor (creará la base de datos en data_lake/orm_warehouse.db por defecto)
    manager = DuckDBORMManager()
    
    # 1. Guardar algunos clientes de prueba
    print("\n📝 Guardando clientes...")
    id_1 = manager.guardar_cliente(nombre="Empresa Alpha S.A.", segmento="Corporativo", limite_credito=50000.0)
    id_2 = manager.guardar_cliente(nombre="Comercial Beta", segmento="Pyme", limite_credito=15000.5)
    
    print(f"   -> Cliente 1 guardado con ID: {id_1}")
    print(f"   -> Cliente 2 guardado con ID: {id_2}")
    
    # 2. Consultar todos los clientes registrados
    print("\n🔍 Consultando base de datos...")
    clientes = manager.obtener_todos_los_clientes()
    
    print("\n📊 Listado de Clientes:")
    for cliente in clientes:
        print(f"   - ID: {cliente['id']} | Nombre: {cliente['nombre']} | Segmento: {cliente['segmento']} | Límite: ${cliente['limite_credito']:,.2f}")
        
    print("\n✨ ¡Proceso ejecutado con éxito!")

if __name__ == "__main__":
    main()