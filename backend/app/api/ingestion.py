from fastapi import APIRouter,File,Form,UploadFile
from pydantic import BaseModel

from backend.app.Ingestion.chunker import chunk_text
from backend.app.Ingestion.metadata import build_chunk_metadata
from backend.app.Ingestion.parsers import parse_file


router = APIRouter(prefix="/api/ingestion",tags = ['ingestion'])

class IngestionResponse(BaseModel):
    filename:str
    scope:str
    source_type:str
    owner_department:str
    chunk_count:int
    sample_chunk:str | None
    sample_metadata:dict | None


@router.post("/upload",response_model = IngestionResponse)
async def upload_enterprise_data(
    file:UploadFile = File(...),
    scope:str = Form(...),
    source_type:str = Form(...),
    owner_department:str = Form(...)
):
    temp_path = f"backend/app/ingestion/tmp_{file.filename}"

    with open(temp_path, "wb") as output_file:
        output_file.write(await file.read())

    parsed_text = parse_file(temp_path)
    chunks = chunk_text(parsed_text)

    sample_metadata = (
        build_chunk_metadata(
            file_path=temp_path,
            scope=scope,
            source_type=source_type,
            owner_department=owner_department,
        )
        if chunks
        else None
    )

    return IngestionResponse(
        filename=file.filename,
        scope=scope,
        source_type=source_type,
        owner_department=owner_department,
        chunk_count=len(chunks),
        sample_chunk=chunks[0] if chunks else None,
        sample_metadata=sample_metadata,
    )




