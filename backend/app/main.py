from fastapi import FastAPI
from backend.app.api.query import router as query_router
from backend.app.api.ingestion import router as ingestion_router

app = FastAPI(
    title = "Enterprise RAG Application"   
)


app.include_router(query_router)
app.include_router(ingestion_router)


@app.get("/health")
def health_status():
    return {"status":"ok"}