import pyarrow.parquet as pq
import pandas as pd

class ParquetMetadataInspector:
    """Inspector programático de esquemas, metadatos y estadísticas de ficheros Parquet."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.parquet_file = pq.ParquetFile(file_path)

    def get_schema_info(self) -> list:
        """Extrae la estructura del esquema de columnas del fichero Parquet."""
        schema = self.parquet_file.schema_arrow
        fields_info = []
        for name in schema.names:
            field = schema.field(name)
            fields_info.append({
                "column_name": name,
                "data_type": str(field.type),
                "nullable": field.nullable
            })
        return fields_info

    def get_file_metadata(self) -> dict:
        """Extrae metadatos generales del archivo Parquet (filas, grupos de filas, versión)."""
        metadata = self.parquet_file.metadata
        return {
            "num_rows": metadata.num_rows,
            "num_row_groups": metadata.num_row_groups,
            "format_version": metadata.format_version,
            "serialized_size": metadata.serialized_size
        }

    def get_row_group_statistics(self) -> list:
        """Extrae estadísticas detalladas por grupo de filas (row groups)."""
        metadata = self.parquet_file.metadata
        stats = []
        for i in range(metadata.num_row_groups):
            rg = metadata.row_group(i)
            stats.append({
                "row_group_index": i,
                "num_rows": rg.num_rows,
                "total_byte_size": rg.total_byte_size,
                "num_columns": rg.num_columns
            })
        return stats