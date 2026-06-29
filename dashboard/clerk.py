import streamlit as st
from rag.retriever import get_context
from rag.llm import ask_llm
from history.chat_history import save_history,get_user_ history

def clerk_dashboard():
    st.title("💬 Clerk Dashboard")
    st.success(f"Welcome **{st.session_state['username']}**")

    st.subheader("Ask a Banking Question")
    question = st.text_input("Enter your question:")

    if st.button("Ask"):
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Searching..."):
             try:
                context = get_context(question)
                answer = ask_llm(question, context)
                st.subheader("Answer:")
                st.write(answer)
                save_history(st.session_state["username"], question, answer)
             except Exception:
                st.error("⚠️ No documents found.Please ask Admin to upload a PDF first.")
    st.divider()
    st.subheader("Your Chat History")
    history = get_user_history(st.session_state["username"])
    if history:
        for row in history:
            st.markdown(f"**Q:** {row['question']}")
            st.markdown(f"**A:** {row['answer']}")
            st.divider()
    else:
        st.info("No history yet.")
