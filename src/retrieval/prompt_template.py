
from langchain_core.prompts import ChatPromptTemplate


def get_rag_prompt():

    template = """
    You are a helpful AI assistant that answers
    questions based on the provided PDF context.

    Follow these rules:
    1. Answer using only the provided context.
    2. Do not make up or assume information.
    3. If the answer is not present in the context,
       say "The answer is not available in the
       uploaded document."
    4. Give clear and easy-to-understand answers.
    5. Keep the answer relevant to the question.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    prompt = ChatPromptTemplate.from_template(template)

    return prompt
