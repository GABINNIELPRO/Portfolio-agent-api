from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.search_request import SearchRequest
from app.core.database import get_db
from app.services.retrieve.multimodal_service import multimodal_search_service
from app.core.models import SearchResult
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.ask_request import AskRequest
from app.core.database import get_db
from app.services.generative_service import generate_response_from_search_result

router = APIRouter()


@router.post("/ask/")
async def ask_question(request: AskRequest, db: Session = Depends(get_db)):
    try:
        result = generate_response_from_search_result(db=db,query=request.query,)
        return result

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur interne (Generative): {str(e)}"
        )
    
