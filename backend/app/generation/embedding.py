from langchain_huggingface import HuggingFaceEmbeddings

from langchain_classic.embeddings import CacheBackedEmbeddings  
from langchain_classic.storage import LocalFileStore 
import tempfile

model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings_model = HuggingFaceEmbeddings(model_name=model_name)


def cache_embedding(text: str):
    with tempfile.TemporaryDirectory(delete=False) as tmp_dir:
        store = LocalFileStore(root_path=tmp_dir)

        cached_embeddings = CacheBackedEmbeddings.from_bytes_store(
            underlying_embeddings=embeddings_model,
            document_embedding_cache=store,
            namespace="embedding_cache",
        )

        return cached_embeddings.embed_query(text)