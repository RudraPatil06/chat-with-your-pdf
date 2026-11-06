
from src.ingestion.pdf_loader import load_pdf

documents = load_pdf("data/uploads/sample.pdf")

# Inspect pages around the reference section
for doc in documents:
    page = doc.metadata.get("page", -1)

    if 25 <= page <= 30:
        print(f"\n{'=' * 50}")
        print(f"PAGE: {page + 1}")
        print("=" * 50)

        for line in doc.page_content.splitlines()[:15]:
            print(repr(line))
