from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    k_text: int = 2
  
