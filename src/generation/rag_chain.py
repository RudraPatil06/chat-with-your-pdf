
from src.ingestion.pdf_loader import load_pdf
from src.ingestion.text_splitter import split_documents
from src.ingestion.embedding_model import get_embedding_model
from src.ingestion.vector_store import create_vector_store

from src.retrieval.retriever import get_retriever, retrieve_documents
from src.generation.generation import generate_answer


def build_rag_pipeline(pdf_path):
    """
    Build the complete RAG pipeline from a PDF.
    """

    # Step 1: Load PDF
    documents = load_pdf(pdf_path)

    # Step 2: Split documents into chunks
    chunks = split_documents(documents)

    # Step 3: Load embedding model
    embeddings = get_embedding_model()

    # Step 4: Store embeddings in ChromaDB
    vector_db = create_vector_store(chunks, embeddings)

    # Step 5: Create retriever
    retriever = get_retriever(vector_db, k=5)

    return retriever


def ask_question(retriever, question):
    """
    Retrieve relevant context and generate an answer.
    """

    # Validate question
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    # Step 1: Retrieve relevant documents
    retrieved_docs = retrieve_documents(retriever, question)

    if not retrieved_docs:
        return {
            "question": question,
            "answer": "No relevant information found in the document.",
            "sources": []
        }

    # Step 2: Remove duplicate chunks
    unique_docs = []
    seen_content = set()

    for doc in retrieved_docs:
        content = doc.page_content.strip()

        if content and content not in seen_content:
            unique_docs.append(doc)
            seen_content.add(content)

    # Step 3: Combine retrieved text
    context = "\n\n".join(
        doc.page_content for doc in unique_docs
    )

    # Step 4: Generate answer
    answer = generate_answer(context, question)

    return {
        "question": question,
        "answer": answer,
        "sources": unique_docs
    }
