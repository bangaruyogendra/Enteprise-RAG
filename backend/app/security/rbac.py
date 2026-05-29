from enum import Enum

class Role(str,Enum):
    ADMIN = "admin"
    COMPLIANCE = "compliance"
    FINANCE = "finance"
    ENGINEERING = "engineering"
    HR = "hr"
    EMPLOYEE = "employee"

ROLE_PERMISSIONS = {
    Role.ADMIN: {"public", "finance", "engineering", "hr", "compliance", "restricted"},
    Role.COMPLIANCE: {"public", "compliance", "restricted"},
    Role.FINANCE: {"public", "finance"},
    Role.ENGINEERING: {"public", "engineering"},
    Role.HR: {"public", "hr"},
    Role.EMPLOYEE: {"public"},
}

def get_allowed_scopes(role:str) -> set[List]:
    try:
        normalized_role = Role(role.lower())
    except ValueError:
         return {"public"}
    return ROLE_PERMISSIONS.get(normalized_role,{"public"})

def can_access(role: str, document_scope: str) -> bool:
    allowed_scopes = get_allowed_scopes(role)
    return document_scope in allowed_scopes

