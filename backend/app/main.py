from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.query import router as query_router
from backend.app.api.ingestion import router as ingestion_router
from backend.app.api.generate_embedding import router as embedding_router

app = FastAPI(
    title = "Enterprise RAG Application"   
)

origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router)
app.include_router(ingestion_router)
app.include_router(embedding_router)


@app.get("/health")
def health_status():
    return {"status":"ok"}