from pathlib import Path
from uuid import uuid4


def build_chunk_metadata(
    file_path: str,
    scope: str,
    source_type: str,
    owner_department: str,
) -> dict:
    path = Path(file_path)

    return {
        "chunk_id": str(uuid4()),
        "source_file": path.name,
        "source_type": source_type,
        "scope": scope,
        "owner_department": owner_department,
    }