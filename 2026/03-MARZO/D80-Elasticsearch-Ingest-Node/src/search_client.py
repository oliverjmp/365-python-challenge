from elasticsearch import Elasticsearch
from typing import Dict, Any, List

class LogSearchClient:
    def __init__(self, client: Elasticsearch, index_name: str = "logs-index"):
        self.client = client
        self.index_name = index_name

    def create_index(self) -> Dict[str, Any]:
        """Crea el índice en Elasticsearch si no existe."""
        if not self.client.indices.exists(index=self.index_name):
            return self.client.indices.create(index=self.index_name)
        return {"acknowledged": False, "message": "Index already exists"}

    def index_log(self, log_id: str, log_data: Dict[str, Any]) -> Dict[str, Any]:
        """Indexa un registro de log estructurado."""
        return self.client.index(index=self.index_name, id=log_id, document=log_data)

    def search_logs(self, query_text: str) -> List[Dict[str, Any]]:
        """Realiza una búsqueda de texto completo sobre los logs indexados."""
        query = {
            "query": {
                "match": {
                    "message": query_text
                }
            }
        }
        response = self.client.search(index=self.index_name, body=query)
        return [hit["_source"] for hit in response["hits"]["hits"]]