import streamlit as st
from rag.retriever import get_context
from rag.llm import ask_llm
from history.chat_history import save_history

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
                context = get_context(question)
                answer = ask_llm(question, context)
            st.subheader("Answer:")
            st.write(answer)
            save_history(st.session_state["username"], question, answer)

    st.divider()
    st.subheader("Your Chat History")
    from history.chat_history import get_user_history
    history = get_user_history(st.session_state["username"])
    if history:
        for row in history:
            st.markdown(f"**Q:** {row['question']}")
            st.markdown(f"**A:** {row['answer']}")
            st.divider()
    else:
        st.info("No history yet.")