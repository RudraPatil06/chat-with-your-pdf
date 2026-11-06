
import streamlit as st
from pathlib import Path
from src.generation.rag_chain import build_rag_pipeline, ask_question

# Page configuration
st.set_page_config(
    page_title="Chat with Your PDF",
    page_icon="📄",
    layout="wide"
)

# Application title
st.title("📄 Chat with Your PDF")
st.write("Upload a PDF and ask questions about its content.")

# Session state
if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# PDF upload
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("Process PDF"):
        upload_dir = Path("data/uploads")
        upload_dir.mkdir(parents=True, exist_ok=True)

        pdf_path = upload_dir / uploaded_file.name
        pdf_path.write_bytes(uploaded_file.getvalue())

        with st.spinner("Processing PDF..."):
            st.session_state.retriever = build_rag_pipeline(str(pdf_path))
            st.session_state.messages = []

        st.success("PDF processed successfully!")

# Chat interface
if st.session_state.retriever is not None:

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask a question about your PDF...")

    if question:
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Generating answer..."):
                result = ask_question(
                    st.session_state.retriever,
                    question
                )

                answer = result["answer"]
                st.markdown(answer)

                with st.expander("View sources"):
                    for doc in result["sources"]:
                        page = doc.metadata.get("page", "Unknown")
                        st.write(f"Page: {page + 1}")
                        st.write(doc.page_content[:500])
                        st.divider()

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })
