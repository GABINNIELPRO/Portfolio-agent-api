from app.services.retrieve.embeddings_service import get_query_embedding
from app.services.retrieve.semantic_service import pgvector_search

def multimodal_search_service(db, query, k_text=2):
    
    embedding_query = get_query_embedding(query)

    semantic_text = pgvector_search(db, embedding_query, k=k_text)

    result = semantic_text[:k_text]

    return result