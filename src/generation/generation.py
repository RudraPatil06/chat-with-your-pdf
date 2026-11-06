
from langchain_ollama import ChatOllama
from src.retrieval.prompt_template import get_rag_prompt


def get_llm():
    """
    Initialize the local Ollama language model.
    """

    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )

    return llm


def generate_answer(context: str, question: str) -> str:
    """
    Generate an answer using retrieved PDF context.
    """

    prompt = get_rag_prompt()
    llm = get_llm()

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content
