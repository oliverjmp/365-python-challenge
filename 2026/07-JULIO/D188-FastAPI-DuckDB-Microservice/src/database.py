import os
import duckdb

# Ruta donde se almacenará el archivo de la base de datos DuckDB
DB_PATH = "corporative_analytics.duckdb"

def obtener_conexion_readonly() -> duckdb.DuckDBPyConnection:
    """
    Abre y devuelve una conexión a DuckDB estrictamente en modo Read-Only.
    Esto permite múltiples lecturas concurrentes sin bloquear la base de datos.
    """
    if not os.path.exists(DB_PATH):
        # Si la base de datos no existe aún, la inicializamos automáticamente
        inicializar_base_datos_prueba()
        
    return duckdb.connect(DB_PATH, read_only=True)

def inicializar_base_datos_prueba():
    """
    Crea la base de datos analítica de DuckDB y puebla datos sintéticos de prueba
    para que las consultas de los endpoints devuelvan resultados reales.
    """
    # Conexión en modo escritura exclusiva para la inicialización
    conn = duckdb.connect(DB_PATH)
    
    # Crear la tabla de ventas corporativas
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ventas_analiticas (
            id_transaccion INTEGER,
            departamento VARCHAR,
            pais VARCHAR,
            monto DOUBLE,
            estado VARCHAR
        )
    """)
    
    # Verificar si la tabla está vacía para insertar datos de prueba
    resultado = conn.execute("SELECT COUNT(*) FROM ventas_analiticas").fetchone()
    if resultado[0] == 0:
        conn.execute("""
            INSERT INTO ventas_analiticas VALUES
            (101, 'Ventas', 'España', 1500.50, 'COMPLETADO'),
            (102, 'Marketing', 'México', 850.00, 'COMPLETADO'),
            (103, 'IT', 'España', 3200.00, 'COMPLETADO'),
            (104, 'Ventas', 'Colombia', 1200.75, 'PENDIENTE'),
            (105, 'Finanzas', 'Chile', 4500.00, 'COMPLETADO'),
            (106, 'Marketing', 'España', 950.25, 'COMPLETADO'),
            (107, 'IT', 'México', 2700.50, 'COMPLETADO'),
            (108, 'Ventas', 'España', 3100.00, 'COMPLETADO'),
            (109, 'Finanzas', 'Colombia', 1800.00, 'CANCELADO'),
            (110, 'IT', 'Chile', 5100.00, 'COMPLETADO');
        """)
    
    conn.close()