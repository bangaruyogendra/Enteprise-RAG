from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.core.schemas import QueryRequest,QueryResponse,AuditTrace,Citation
from backend.app.security.rbac import get_allowed_scopes
from backend.app.retrieval.secure_retriever import secure_authorised_retrieval

router = APIRouter(prefix = "/api",tags = ["query"])

@router.post("/query",response_model = QueryResponse)
def query_enterprise_data(request:QueryRequest):

    allowed_scopes = get_allowed_scopes(request.role)
    documents = secure_authorised_retrieval(request.question,request.role)

    audit_trace = AuditTrace(
        user_id=request.user_id,
        role=request.role,
        department=request.department,
        allowed_scopes=allowed_scopes,
        retrieved_document_ids=[doc["id"] for doc in documents]
    )

    if not documents:
        return QueryResponse(
            answer="I could not find revalent answer",
            citations=[],
            confidence =0.0,
            allowed_scopes = allowed_scopes
        )
    
    citations = [
        Citation(
            document_id = doc['id'],
            title = doc['title'],
            scope = doc['scope']
        ) for doc in documents
    ]
    content = "".join(doc['content'] for doc in documents)

    return QueryResponse(
        answer=f"authorised_role_answer:{content}",
        citations=citations,
        confidence=0.65,
        audit_trace = audit_trace
    )

