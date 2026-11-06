from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    if not documents:
        raise ValueError("No documents provided for splitting.")

    documents = [
        doc for doc in documents
        if doc.page_content.strip()
    ]

    if not documents:
        raise ValueError("No readable text found in the PDF.")

    print(f"Pages retained: {len(documents)}")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)

    if not chunks:
        raise ValueError("No text chunks were generated.")

    print(f"Successfully created {len(chunks)} chunks.")

    return chunks