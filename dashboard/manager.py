import streamlit as st
from collections import Counter
from rag.retriever import get_context
from rag.llm import ask_llm
from history.chat_history import get_all_history
from auth.login import add_clerk

def manager_dashboard():
    st.title("📊 Manager Dashboard")
    st.success(f"Welcome **{st.session_state['username']}**")

    tab1, tab2, tab3 = st.tabs(["💬 Ask Question", "📋 View Reports", "👤 Add Clerk"])

    with tab1:
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

    with tab2:
        st.subheader("All Clerk Activity")
        history = get_all_history()
        if history:
            users = [row["username"] for row in history]
            counts = Counter(users)
            st.subheader("Questions Asked Per Clerk")
            for user, count in counts.items():
                st.markdown(f"- **{user}**: {count} questions")
            st.divider()
            st.subheader("Full Chat Log")
            for row in history:
                st.markdown(f"**User:** {row['username']} | 🕒 {row['timestamp']}")
                st.markdown(f"**Q:** {row['question']}")
                st.markdown(f"**A:** {row['answer']}")
                st.divider()
        else:
            st.info("No activity yet.")

    with tab3:
        st.subheader("👤 Add New Clerk")
        new_username = st.text_input("New Clerk Username")
        new_password = st.text_input("New Clerk Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Add Clerk"):
            if new_username.strip() == "" or new_password.strip() == "":
                st.warning("⚠️ Username and password cannot be empty.")
            elif new_password != confirm_password:
                st.error("❌ Passwords do not match.")
            else:
                success, message = add_clerk(new_username, new_password)
                if success:
                    st.success(message)
                else:
                    st.error(message)