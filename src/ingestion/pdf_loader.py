
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    """
    Load a PDF and extract its text page by page.

    Args:
        file_path: Location of the PDF file.

    Returns:
        List of LangChain Document objects.
    """

    pdf_path = Path(file_path)

    # Check if file exists
    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF file not found: {file_path}"
        )

    # Check file extension
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    # Load PDF
    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    # Check extracted content
    if not documents:
        raise ValueError("No content could be extracted from PDF.")

    print(f"Successfully loaded {len(documents)} pages.")

    return documents
