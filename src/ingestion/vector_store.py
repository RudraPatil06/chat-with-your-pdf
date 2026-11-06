
from pathlib import Path
import hashlib

from langchain_chroma import Chroma


def create_vector_store(
    chunks,
    embedding_model,
    persist_directory="data/vectorstore",
    collection_name="pdf_documents"
):
    """
    Create or update a persistent ChromaDB vector database.
    """

    # Step 1: Validate input
    if not chunks:
        raise ValueError("No document chunks provided.")

    # Step 2: Create storage directory
    Path(persist_directory).mkdir(
        parents=True,
        exist_ok=True
    )

    # Step 3: Generate stable IDs
    ids = [
        hashlib.sha256(
            chunk.page_content.encode("utf-8")
        ).hexdigest()
        for chunk in chunks
    ]

    # Step 4: Remove duplicate chunks within this batch
    unique_chunks = {}
    for chunk_id, chunk in zip(ids, chunks):
        unique_chunks[chunk_id] = chunk

    ids = list(unique_chunks.keys())
    documents = list(unique_chunks.values())

    # Step 5: Initialize ChromaDB
    vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=embedding_model,
        persist_directory=persist_directory
    )

    # Step 6: Insert or update documents
    vector_store._collection.upsert(
        ids=ids,
        documents=[doc.page_content for doc in documents],
        metadatas=[doc.metadata for doc in documents]
    )

    print(f"Successfully stored {len(documents)} unique chunks.")

    return vector_store
