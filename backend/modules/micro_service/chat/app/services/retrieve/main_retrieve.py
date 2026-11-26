
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.search_request import SearchRequest
from app.core.database import get_db
from app.services.retrieve.multimodal_service import multimodal_search_service
from app.core.models import SearchResult
from datetime import datetime
from sqlalchemy.orm import Session
from app.schemas.ask_request import AskRequest




def search_multimodal_endpoint(request: SearchRequest, db: Session = Depends(get_db)):
# db ets une sessiona la bdd on a directement une connection avec la bdd
    try:
        results = multimodal_search_service(
            db=db,
            query=request.query,
            k_text=request.k_text
        )

        if not results:
            raise HTTPException(status_code=404, detail="Aucun résultat trouvé")

        document_ids = [r["id"] for r in results if r["type"] == "text"]
        document_texts = [r["content"] for r in results if r["type"] == "text"]
        distances = [
            r.get("distance", None) if r["type"] == "text" else None
            for r in results
        ]

        new_search_result = SearchResult(
            query=request.query,
            k=request.k_text,
            document_ids=document_ids,
            document_texts=document_texts,
            distances=distances
        )

        db.add(new_search_result)
        db.commit()

        return {
            "search_result_id": str(new_search_result.id),
            "query": request.query,
            "results": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))