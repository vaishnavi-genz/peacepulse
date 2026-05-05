import streamlit as st

def guided_meditation():
    st.subheader("Guided Meditation")
    st.video("https://www.youtube.com/watch?v=inpok4MKVLM")

def deep_breathing_exercise():
    st.subheader("Deep Breathing Exercise")
    st.write("Inhale deeply for 4 seconds, hold for 7 seconds, and exhale for 8 seconds.")
    if st.button("Start Exercise"):
        st.write("Starting deep breathing exercise...")

guided_meditation()
deep_breathing_exercise()
