import streamlit as st
import pyrebase

firebase_config = {
    "apiKey": "AIzaSyBKfLSc3ZKsjA6OM7dHUafYxOvJmk6oZw8",
    "authDomain": "abc12-d032b.firebaseapp.com",
    "projectId": "abc12-d032b",
    "storageBucket": "abc12-d032b.firebasestorage.app",
    "messagingSenderId": "438964381085",
    "appId": "1:438964381085:web:fc871649e3f88cbe60fb74",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login_signup():
    st.title("🔐 Login / Signup")

    choice = st.selectbox("Login/Signup", ["Login", "Signup"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if not email or not password:
        st.warning("Please enter email and password")
        return

    if choice == "Signup":
        if st.button("Create Account"):
            try:
                auth.create_user_with_email_and_password(email, password)
                st.success("Account created! Please login")
            except Exception as e:
                st.error(f"Signup failed: {e}")

    if choice == "Login":
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.user = user
                st.success("Login successful!")
            except Exception as e:
                st.error(f"Login failed: {e}")