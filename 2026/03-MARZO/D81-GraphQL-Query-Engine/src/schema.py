import strawberry
from typing import List, Optional

@strawberry.type
class LogEntry:
    id: strawberry.ID
    level: str
    message: str

fake_database = [
    LogEntry(id="1", level="INFO", message="Servidor iniciado correctamente"),
    LogEntry(id="2", level="ERROR", message="Fallo en la conexión con la base de datos"),
    LogEntry(id="3", level="WARNING", message="Alto consumo de memoria RAM detectado")
]

@strawberry.type
class Query:
    @strawberry.field
    def logs(self, level: Optional[str] = None) -> List[LogEntry]:
        if level:
            return [log for log in fake_database if log.level.upper() == level.upper()]
        return fake_database

    @strawberry.field
    def log(self, id: strawberry.ID) -> Optional[LogEntry]:
        for log in fake_database:
            if log.id == id:
                return log
        return None

schema = strawberry.Schema(query=Query)