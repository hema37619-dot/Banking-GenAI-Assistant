import streamlit as st
import os
import shutil
import tempfile
from rag.ingest import ingest_pdf
from history.chat_history import get_all_history
from config import CHROMA_PATH

def admin_dashboard():
    st.title("🔧 Admin Dashboard")
    st.success(f"Welcome **{st.session_state['username']}**")

    tab1, tab2, tab3 = st.tabs(["📄 Upload PDF", "🗑️ Delete PDFs", "💬 Chat History"])

    with tab1:
        st.subheader("Upload Banking Policy PDF")
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
        if uploaded_file:
            if st.button("Ingest PDF"):
                with st.spinner("Ingesting PDF..."):
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                        tmp.write(uploaded_file.read())
                        tmp_path = tmp.name
                    result = ingest_pdf(tmp_path)
                    os.unlink(tmp_path)
                st.success(result)

    with tab2:
        st.subheader("🗑️ Delete All PDFs")
        st.warning("This will delete all ingested PDFs from the database. Upload new PDFs after deleting.")
        if st.button("Delete All PDFs"):
            try:
                # Step 1 - close ChromaDB connection first
                from rag.retriever import db
                db._client.reset()

                # Step 2 - delete files individually
                if os.path.exists(CHROMA_PATH):
                    for root, dirs, files in os.walk(CHROMA_PATH):
                        for file in files:
                            filepath = os.path.join(root, file)
                            try:
                                os.remove(filepath)
                            except Exception:
                                pass
                    # remove empty folders
                    shutil.rmtree(CHROMA_PATH, ignore_errors=True)
                    st.success("✅ All PDFs deleted successfully.")
                    st.info("⚠️ Please restart the app before uploading new PDFs.")
                else:
                    st.info("No PDFs found to delete.")

            except Exception as e:
                st.error(f"❌ Error: {e}")

    with tab3:
        st.subheader("All Chat History")
        history = get_all_history()
        if history:
            for row in history:
                st.markdown(f"**User:** {row['username']} | 🕒 {row['timestamp']}")
                st.markdown(f"**Q:** {row['question']}")
                st.markdown(f"**A:** {row['answer']}")
                st.divider()
        else:
            st.info("No chat history yet.")