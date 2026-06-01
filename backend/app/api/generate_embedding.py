from fastapi import APIRouter
from backend.app.generation.embedding import cache_embedding
from backend.app.core.schemas import EmbeddingRequest, EmbeddingResponse
from fastapi import UploadFile, File, Form

router = APIRouter(prefix="/api/embedding",tags = ['embedding'])



@router.post("/cache",response_model = EmbeddingResponse)

async def cache_embedding_endpoint(request:EmbeddingRequest):
    embedding = cache_embedding(request.text)
    return EmbeddingResponse(embedding=embedding)
