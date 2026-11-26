from sqlalchemy.orm import Session
from sqlalchemy import text


def pgvector_search(db: Session, query_embedding: list, k: int = 2):

    sql = text("""
        SELECT
            id,
            document_id,
            file_text,
            embedding <=> CAST(:embedding_query AS vector) AS distance 
        FROM document
        WHERE embedding IS NOT NULL
        ORDER BY distance ASC
        LIMIT :k;
    """)
    # ici embedding <=> CAST(:embedding_query AS vector) AS distance  
    # on cast embedding_query en vecteur 
    # <=> paramètre pgvector qui calcul dist entre "embedding" du et texte de la bdd et "embedding_query" de la question 
    # AS DISTANCE car le resulatt sera une distance
    # ORDER BY ASC du plus petit au plus grand on va prendre les k = 5 plus petites distance donc ou les sesn se rapprochent le plus

    rows = db.execute(sql, {# ici on execute la requete et on met les params
        "embedding_query": query_embedding,
        "k": k
    }).mappings().all()
    # .mappinngs transforme le resultat de la bdd de tuple a dict
    # .all c'est toute les lignes
    # en effet une bdd a ses info en lignes donc la majorité du temps python les transforme en tuple il crois que s'en est

    return [
        {
            "type": "text",
            "id": r["id"],
            "document_id": r["document_id"],
            "content": r["file_text"],
            "distance": float(r["distance"]),
            "score_semantic": 1 - float(r["distance"])
        }
        for r in rows
    ]

# ici équivalent a la forme resultat = [c for c in rows]
# le premier c ici c'est tout le dict
