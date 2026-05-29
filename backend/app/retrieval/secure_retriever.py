from backend.app.retrieval.documents import ENTERPRISE_DOCUMENTS
from backend.app.security.rbac import get_allowed_scopes


def secure_authorised_retrieval(question:str,role:str)->list[dict]:
    allowed_scopes = get_allowed_scopes(role)
    question_terms = set(question.split())

    for document in ENTERPRISE_DOCUMENTS:
        if document['scope'] not in allowed_scopes:
            continue
        
        results =[]

        searchable_text  = f"{document['title']} {document['content']}".lower()
        score = sum(1 for terms in question_terms if terms in searchable_text)

        if score >0:
            results.append({**document,"score":score})

    return sorted(results,key=lambda item:item['score'],reverse=True)

