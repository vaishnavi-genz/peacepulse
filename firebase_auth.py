import streamlit as st
try:
    import pyrebase
    PYREBASE_AVAILABLE = True
except ImportError:
    PYREBASE_AVAILABLE = False

# Fallback mechanism for Firebase
try:
    if PYREBASE_AVAILABLE and "FIREBASE_API_KEY" in st.secrets:
        firebase_config = {
            "apiKey": st.secrets["FIREBASE_API_KEY"],
            "authDomain": "abc12-d032b.firebaseapp.com",
            "projectId": "abc12-d032b",
            "storageBucket": "abc12-d032b.firebasestorage.app",
            "messagingSenderId": "438964381085",
            "appId": "1:438964381085:web:fc871649e3f88cbe60fb74",
            "databaseURL": ""
        }
        firebase = pyrebase.initialize_app(firebase_config)
        auth = firebase.auth()
    else:
        auth = None
except Exception:
    auth = None

def login_signup():
    st.markdown('<div style="height: 10vh;"></div>', unsafe_allow_html=True) # Spacer
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>Welcome to PeacePulse 🌿</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666; margin-bottom: 2rem;'>Your journey to a calmer mind begins here.</p>", unsafe_allow_html=True)
        
        if auth is None:
            st.warning("⚠️ Authentication system is currently unavailable (Missing Firebase API Key). You can use a temporary guest session for now.")
            if st.button("Continue as Guest", use_container_width=True):
                st.session_state.user = {"email": "guest@peacepulse.local"}
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            return

        choice = st.radio("Select Action", ["Login", "Signup"], horizontal=True, label_visibility="collapsed")
        st.markdown("<hr style='margin: 1rem 0; border-color: rgba(0,0,0,0.1);'>", unsafe_allow_html=True)

        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")

        if choice == "Signup":
            if st.button("Create Account", use_container_width=True):
                if not email or not password:
                    st.warning("Please enter email and password")
                else:
                    try:
                        auth.create_user_with_email_and_password(email, password)
                        st.success("Account created successfully! You can now switch to Login.")
                    except Exception as e:
                        error_msg = str(e)
                        if "EMAIL_EXISTS" in error_msg:
                            st.error("Email already in use. Please switch to Login.")
                        else:
                            st.error(f"Signup failed: {e}")

        elif choice == "Login":
            if st.button("Login", use_container_width=True):
                if not email or not password:
                    st.warning("Please enter email and password")
                else:
                    try:
                        user = auth.sign_in_with_email_and_password(email, password)
                        st.session_state.user = user
                        st.success("Login successful!")
                        st.rerun()
                    except Exception as e:
                        st.error("Login failed: Invalid credentials or account does not exist.")
        
        st.markdown('</div>', unsafe_allow_html=True)