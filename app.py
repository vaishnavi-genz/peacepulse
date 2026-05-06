import streamlit as st

# MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="PeacePulse", page_icon="🌿", layout="wide")

import matplotlib.pyplot as plt
from theme_manager import apply_theme
from mood_tracking import log_mood, display_mood_trends
from educational_content import educational_resources
from community_forum import post_message, display_forum
from firebase_auth import login_signup
from games import breathing_game, positive_affirmations, emoji_memory_game
from database import init_db
from analytics import display_analytics
from chatbot import display_chatbot

# Initialize SQLite database
init_db()

# --- Session State Initialization ---
if 'current_mood' not in st.session_state:
    st.session_state.current_mood = "Neutral"

# Apply dynamic theme based on mood
apply_theme()

# --- Authentication ---
if 'user' not in st.session_state:
    login_signup()
    st.stop()

# --- Sidebar Navigation ---
st.sidebar.markdown("## 🌿 PeacePulse")
st.sidebar.write(f"Welcome back!")
st.sidebar.markdown("---")

menu = [
    "🏠 Dashboard", 
    "📝 Mood Tracking", 
    "📊 Analytics Dashboard",
    "🤖 AI Wellness Chat",
    "💬 Community Forum", 
    "🎮 Therapeutic Games",
    "📚 Educational Resources"
]
choice = st.sidebar.radio("Navigate", menu)

st.sidebar.markdown("---")
if st.sidebar.button("Log Out", use_container_width=True):
    st.session_state.pop("user")
    st.rerun()

# --- Page Routing ---
if choice == "🏠 Dashboard":
    st.title("Welcome to PeacePulse 🌿")
    st.markdown("Your modern, emotionally-intelligent mental wellness companion.")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Today's Check-in")
    log_mood()
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🧘 Breathe")
        st.write("Take a moment to center yourself with guided breathing.")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Analyze")
        st.write("Understand your emotional patterns over time.")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 💬 Connect")
        st.write("Share your thoughts in a safe community space.")
        st.markdown('</div>', unsafe_allow_html=True)

elif choice == "📝 Mood Tracking":
    st.title("📝 Mood Tracking")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    log_mood()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    display_mood_trends()
    st.markdown('</div>', unsafe_allow_html=True)

elif choice == "📊 Analytics Dashboard":
    display_analytics()

elif choice == "🤖 AI Wellness Chat":
    display_chatbot()

elif choice == "💬 Community Forum":
    st.title("💬 Community Forum")
    post_message()
    display_forum()

elif choice == "🎮 Therapeutic Games":
    st.title("🎮 Therapeutic Games")
    game_choice = st.selectbox("Choose an activity", ["Breathing Exercise", "Positive Affirmations", "Emoji Memory Game"])
    
    if game_choice == "Breathing Exercise":
        breathing_game()
    elif game_choice == "Positive Affirmations":
        positive_affirmations()
    elif game_choice == "Emoji Memory Game":
        emoji_memory_game()

elif choice == "📚 Educational Resources":
    st.title("📚 Educational Resources")
    educational_resources()