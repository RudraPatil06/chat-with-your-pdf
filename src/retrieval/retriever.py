
from typing import List
from langchain_core.documents import Document


def get_retriever(vector_store, k: int = 5):

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": 15,
            "lambda_mult": 0.7
        }
    )

    return retriever


def retrieve_documents(retriever, query: str) -> List[Document]:
    """
    Retrieve relevant documents based on user query.

    Args:
        retriever: LangChain retriever.
        query: User's question.

    Returns:
        List of relevant document chunks.
    """

    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    results = retriever.invoke(query)

    return results
