import openai
from fastapi import HTTPException
from app.core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def get_query_embedding(query: str) -> list:
    try:
        response = openai.Embedding.create(
            model="text-embedding-3-large",
            input=query
        )
        embedding = response["data"][0]["embedding"]

        if len(embedding) != 3072:
            raise HTTPException(500, "Embedding dimension incorrecte")

        return embedding

    except Exception as e:
        raise HTTPException(500, f"Erreur embedding: {e}")
