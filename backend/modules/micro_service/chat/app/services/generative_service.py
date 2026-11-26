from sqlalchemy.orm import Session

from app.services.context_service import prepare_multimodal_context
from app.services.llm_service import generate_multimodal_response
from app.services.retrieve.multimodal_service import multimodal_search_service


def generate_response_from_search_result(db: Session, query: str, k_text: int = 2):
    # 1) Retrieval : appel direct de la fonction, sans HTTP
    results = multimodal_search_service(db=db, query=query, k_text=k_text)
    if not results:
        return {"answer": "Je n'ai pas trouvé d'information à ce sujet.", "sources": []}

    # 2) Contexte
    context = prepare_multimodal_context(results)

    # 3) LLM
    answer = generate_multimodal_response(query=query, context=context)

    # 4) Retour avec les sources
    return {
        "answer": answer,
        "sources": [
            {"id": str(r["id"]), "extrait": r["content"][:200]}
            for r in results if r["type"] == "text"
        ],
    }