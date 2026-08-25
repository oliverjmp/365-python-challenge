import mmap
import os
import time
from typing import List, Dict, Any

class MemoryMappedFileProcessor:
    """Procesador de archivos binarios masivos utilizando mapeo de memoria virtual del OS."""
    
    def __init__(self, file_path: str = "data_lake/binary_records.bin"):
        self.file_path = file_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self._generar_archivo_binario_si_no_existe()

    def _generar_archivo_binario_si_no_existe(self):
        """Genera un archivo binario estructurado de prueba si no se encuentra en el data lake."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, "wb") as f:
                registros = [
                    b"REC_001_DATA_AOK_SYSTEM_ONLINE",
                    b"REC_002_DATA_SEC_SECURE_NODE",
                    b"REC_003_DATA_VIP_PRIORITY_LOG",
                    b"REC_004_DATA_LOG_AUDIT_TRACE"
                ]
                for reg in registros:
                    f.write(reg)

    def buscar_patron_con_metricas(self, patron: bytes) -> Dict[str, Any]:
        """Busca un patrón midiendo latencia y mapeando directamente los offsets en memoria."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"El archivo binario no existe en: {self.file_path}")

        inicio_tiempo = time.time()
        coincidencias = []
        
        with open(self.file_path, "rb") as f:
            with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
                pos = mm.find(patron)
                while pos != -1:
                    coincidencias.append(pos)
                    pos = mm.find(patron, pos + 1)
                    
        duracion_ms = (time.time() - inicio_tiempo) * 1000
        
        return {
            "patron": patron.decode(),
            "coincidencias": coincidencias,
            "duracion_ms": round(duracion_ms, 4),
            "tamano_archivo_bytes": os.path.getsize(self.file_path)
        }

    def leer_bloque(self, inicio: int, longitud: int) -> bytes:
        """Lee un bloque específico de bytes directamente desde el mapa de memoria virtual."""
        with open(self.file_path, "rb") as f:
            with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
                return mm[inicio:inicio + longitud]