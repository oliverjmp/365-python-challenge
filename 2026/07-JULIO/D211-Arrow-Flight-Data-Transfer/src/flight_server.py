import pyarrow as pa
import pyarrow.flight as fl
import pandas as pd

class SimpleFlightServer(fl.FlightServerBase):
    """Servidor ultrarrápido basado en Apache Flight para transferencia in-memory de DataFrames."""

    def __init__(self, location="grpc://localhost:8815", **kwargs):
        super(SimpleFlightServer, self).__init__(location, **kwargs)
        self.flights = {}

    def populate_table(self, name: str, df: pd.DataFrame):
        table = pa.Table.from_pandas(df)
        self.flights[name] = table

    def do_get(self, context, ticket):
        ticket_key = ticket.ticket.decode('utf-8')
        if ticket_key in self.flights:
            table = self.flights[ticket_key]
            return fl.RecordBatchStream(table)
        raise KeyError(f"Dataset '{ticket_key}' no encontrado en el servidor Flight.")

    def list_flights(self, context, criteria):
        for name, table in self.flights.items():
            descriptor = fl.FlightDescriptor.for_path(name)
            yield fl.FlightInfo(table.schema, descriptor, [], table.num_rows, table.nbytes)