from fastapi import APIRouter, Query
from backend.services.search_service import search_documents

router = APIRouter()

@router.get("/search")
async def search(query: str = Query(...)):
    results = search_documents(query)
    return results