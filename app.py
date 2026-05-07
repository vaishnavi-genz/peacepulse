import streamlit as st

# MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="PeacePulse", page_icon="🌿", layout="wide")

import matplotlib.pyplot as plt
from theme_manager import apply_theme
from mood_tracking import log_mood, display_mood_trends
from educational_content import educational_resources
from community_forum import post_message, display_forum
from firebase_auth import login_signup
from games import display_contextual_activity
from database import init_db, get_user_moods
from analytics import display_analytics
from chatbot import display_chatbot
from music_recommender import display_compact_music_section
from wellness_recommendations import display_compact_wellness_suggestions

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
    "🏠 Welcome",
    "📝 Mood & Wellness Hub",
    "📊 Analytics Dashboard",
    "🤖 AI Wellness Chat",
    "💬 Community Forum", 
    "📚 Educational Resources"
]
choice = st.sidebar.radio("Navigate", menu)

st.sidebar.markdown("---")
if st.sidebar.button("Log Out", use_container_width=True):
    st.session_state.pop("user")
    st.rerun()

# --- Page Routing ---
if choice == "🏠 Welcome":
    import random
    
    quotes = [
        "You deserve the same kindness you give to others.",
        "Healing is not linear, and that's okay.",
        "Small peaceful moments matter.",
        "Breathe gently. You are doing your best.",
        "Rest is productive too."
    ]
    
    if 'current_quote' not in st.session_state:
        st.session_state.current_quote = random.choice(quotes)
        
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='text-align: center; animation: fadeIn 2s ease-in-out;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>🌿</div>
            <h1 style='font-weight: 300; margin-bottom: 0.5rem;'>Welcome to PeacePulse</h1>
            <p style='font-size: 1.2rem; opacity: 0.8;'>Your Safe Space for Emotional Wellness</p>
            <br><br>
            <div style='max-width: 650px; margin: 0 auto; padding: 2.5rem; background: rgba(255,255,255,0.3); border-radius: 24px; backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.4); box-shadow: 0 10px 40px rgba(0,0,0,0.03); transition: all 0.5s ease;'>
                <h3 style='font-weight: 400; font-style: italic; line-height: 1.6; margin: 0; opacity: 0.9;'>"{st.session_state.current_quote}"</h3>
            </div>
            <br><br><br>
            <p style='opacity: 0.6; font-size: 0.9rem; letter-spacing: 0.5px;'>Navigate from the sidebar when you're ready.</p>
        </div>
        <style>
            @keyframes fadeIn {{
                0% {{ opacity: 0; transform: translateY(15px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>
    """, unsafe_allow_html=True)

elif choice == "📝 Mood & Wellness Hub":
    st.title("📝 Mood & Wellness Hub")
    st.markdown("Your modern, emotionally-intelligent mental wellness companion.")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Today's Check-in")
    log_mood()
    st.markdown('</div>', unsafe_allow_html=True)
    
    current_mood = st.session_state.get("current_mood", "Neutral")
    
    st.markdown("---")
    st.markdown(f"### 🌟 Your {current_mood} Support Hub")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🎵 Sounds", "🎮 Activities", "🌿 Insights", "📈 Trends"])
    
    with tab1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        display_compact_music_section(current_mood)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with tab2:
        display_contextual_activity(current_mood)
        
    with tab3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        user_email = st.session_state.user.get('email', 'guest@peacepulse.local')
        df = get_user_moods(user_email)
        display_compact_wellness_suggestions(current_mood, df)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with tab4:
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

elif choice == "📚 Educational Resources":
    st.title("📚 Educational Resources")
    educational_resources()