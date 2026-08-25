import duckdb

class SpatialQueryRunner:
    """Gestor de consultas geoespaciales utilizando la extensión spatial de DuckDB."""

    def __init__(self):
        self.conn = duckdb.connect(database=":memory:")
        self._inicializar_extension()

    def _inicializar_extension(self):
        """Carga e instala la extensión spatial en DuckDB."""
        try:
            self.conn.execute("INSTALL spatial;")
            self.conn.execute("LOAD spatial;")
        except Exception as e:
            raise RuntimeError(f"No se pudo cargar la extensión spatial de DuckDB: {e}")

    def crear_datos_prueba(self):
        """Crea una tabla con geometrías de puntos (coordenadas de ciudades/puntos de interés)."""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS puntos_interes (
                id INT,
                nombre VARCHAR,
                lat FLOAT,
                lon FLOAT
            );
        """)
        self.conn.execute("""
            INSERT INTO puntos_interes VALUES 
            (1, 'Madrid Centro', 40.4168, -3.7038),
            (2, 'Alcobendas Tech', 40.5472, -3.6420),
            (3, 'Barcelona Sants', 41.3784, 2.1406);
        """)

    def ejecutar_consulta_espacial(self) -> list:
        """Transforma coordenadas en geometrías espaciales y calcula distancias o puntos."""
        self.crear_datos_prueba()
        query = """
            SELECT 
                id,
                nombre,
                lat,
                lon,
                ST_AsText(ST_Point(lon, lat)) AS geometria_wkt
            FROM puntos_interes;
        """
        result = self.conn.execute(query).fetchall()
        return result