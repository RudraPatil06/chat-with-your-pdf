from src.generation.rag_chain import build_rag_pipeline, ask_question

# Build RAG pipeline
retriever = build_rag_pipeline("data/uploads/sample.pdf")

# Ask a question
question = "What are the main features of Python?"

# Generate answer
result = ask_question(retriever, question)

print("\nQUESTION:")
print(result["question"])

print("\nGENERATED ANSWER:")
print(result["answer"])

print("\nSOURCES:")
for doc in result["sources"]:
    print("Page:", doc.metadata.get("page", "Unknown"))