import streamlit as st
from auth.login import authenticate
from history.chat_history import init_chat_db
from dashboard.admin import admin_dashboard
from dashboard.clerk import clerk_dashboard
from dashboard.manager import manager_dashboard

init_chat_db()

st.set_page_config(page_title="🏦 Banking AI Assistant", layout="wide")

# Initialize form key counter
if "form_key" not in st.session_state:
    st.session_state["form_key"] = 0

if st.session_state.get("logged_in"):
    st.sidebar.success(f"Logged in as **{st.session_state['username']}**")
    st.sidebar.write(f"Role: `{st.session_state['role']}`")

    if st.sidebar.button("Logout"):
        st.session_state["form_key"] += 1  # ✅ changes key → fields reset
        for key in ["logged_in", "username", "role"]:
            st.session_state.pop(key, None)
        st.rerun()

    role = st.session_state["role"]
    if role == "admin":
        admin_dashboard()
    elif role == "clerk":
        clerk_dashboard()
    elif role == "manager":
        manager_dashboard()
    else:
        st.error("Unknown role. Contact administrator.")

else:
    st.title("🏦 Banking GenAI Assistant")
    st.info("👈 Please login from the sidebar to continue")

    st.sidebar.header("🔐 Login")
    # ✅ Dynamic key forces fresh empty widget after logout
    username = st.sidebar.text_input("Username", key=f"username_{st.session_state['form_key']}")
    password = st.sidebar.text_input("Password", type="password", key=f"password_{st.session_state['form_key']}")

    if st.sidebar.button("Login", key=f"login_{st.session_state['form_key']}"):
        role = authenticate(username, password)
        if role:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = role
            st.rerun()
        else:
            st.error("❌ Invalid Username or Password")