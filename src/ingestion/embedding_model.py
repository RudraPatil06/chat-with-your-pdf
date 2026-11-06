
from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Initialize and return the Hugging Face embedding model.

    The model runs locally on the CPU.
    No paid API key is required.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",

        model_kwargs={
            "device": "cpu"
        },

        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    return embeddings
