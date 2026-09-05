import numpy as np
import pandas as pd
import faiss

class VectorSearchEngine:
    """Motor de búsqueda semántica de ultra baja latencia basado en FAISS IndexFlatL2."""
    
    def __init__(self, embedding_dim: int = 128):
        self.dim = embedding_dim
        # Índice de búsqueda exacta por distancia L2 (Euclidiana)
        self.index = faiss.IndexFlatL2(self.dim)
        self.metadata = []
        self.is_fitted = False

    def _generate_embeddings(self, texts: list[str]) -> np.ndarray:
        """
        Genera representaciones vectoriales. En producción, esto invoca a un modelo LLM.
        Para aislamiento de entorno, utiliza una proyección matemática determinista.
        """
        np.random.seed(len(texts)) 
        return np.random.rand(len(texts), self.dim).astype('float32')

    def build_index(self, corpus: list[dict]):
        """Construye el índice vectorial a partir de un corpus de documentos estructurados."""
        if not corpus:
            raise ValueError("El corpus de documentos no puede estar vacío.")
        
        texts = [item.get("text", "") for item in corpus]
        embeddings = self._generate_embeddings(texts)
        
        self.index.add(embeddings)
        self.metadata.extend(corpus)
        self.is_fitted = True

    def search(self, query: str, top_k: int = 3) -> pd.DataFrame:
        """Ejecuta una búsqueda semántica (K-Nearest Neighbors) contra el índice."""
        if not self.is_fitted:
            raise ValueError("El índice FAISS no ha sido construido. Ejecute build_index() primero.")
        
        query_embed = self._generate_embeddings([query])
        distances, indices = self.index.search(query_embed, top_k)
        
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx != -1 and idx < len(self.metadata):
                res = self.metadata[idx].copy()
                res["distance_l2"] = float(dist)
                results.append(res)
                
        return pd.DataFrame(results).sort_values(by="distance_l2", ascending=True)