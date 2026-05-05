import streamlit as st
import matplotlib.pyplot as plt
from mood_tracking import log_mood, display_mood_trends
from mindfulness_tools import guided_meditation, deep_breathing_exercise
from educational_content import educational_resources
from community_forum import post_message, display_forum
from wearable_integration import display_wearable_data

# ✅ ADD THIS (VERY IMPORTANT)
if 'mood_data' not in st.session_state:
    st.session_state.mood_data = []

st.title("AI-Powered Mental Health App")

menu = ["Mood Tracking", "Mindfulness Tools", "Educational Resources", "Community Forum", "Wearable Integration", "play game"]
choice = st.sidebar.selectbox("Select a feature", menu)

if choice == "Mood Tracking":
    log_mood()
    display_mood_trends()
elif choice == "Mindfulness Tools":
    guided_meditation()
    deep_breathing_exercise()
elif choice == "Educational Resources":
    educational_resources()
elif choice == "Community Forum":
    post_message()
    display_forum()
elif choice == "Wearable Integration":
    display_wearable_data()