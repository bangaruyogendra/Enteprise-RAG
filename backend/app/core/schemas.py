from pydantic import BaseModel


class QueryRequest(BaseModel):
    question:str
    user_id:str
    role:str
    department:str


class AuditTrace(BaseModel):
    user_id: str
    role: str
    department: str
    allowed_scopes: list[str]
    retrieved_document_ids: list[str]

class Citation(BaseModel):
    document_id:str
    title:str
    scope:str

class QueryResponse(BaseModel):
    answer:str
    citations:list[Citation]
    confidence:float
    audit_trace:AuditTrace

