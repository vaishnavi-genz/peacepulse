import streamlit as st
import time
import random

def breathing_game():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🧘 Breathing Exercise")
    st.write("Follow the circle and breathe calmly. This simple exercise helps lower your heart rate and reduce stress.")

    start = st.button("Start Breathing")

    if start:
        for i in range(5):  # 5 cycles
            # Inhale
            st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Inhale...</h3>", unsafe_allow_html=True)
            circle = st.empty()

            for size in range(50, 200, 10):
                circle.markdown(
                    f"""
                    <div style="
                        width:{size}px;
                        height:{size}px;
                        border-radius:50%;
                        background-color:rgba(110, 198, 255, 0.6);
                        margin:auto;
                        transition:0.1s;">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                time.sleep(0.1)

            # Hold
            st.markdown("<h3 style='text-align: center; color: #757575;'>Hold...</h3>", unsafe_allow_html=True)
            time.sleep(2)

            # Exhale
            st.markdown("<h3 style='text-align: center; color: #FF9800;'>Exhale...</h3>", unsafe_allow_html=True)

            for size in range(200, 50, -10):
                circle.markdown(
                    f"""
                    <div style="
                        width:{size}px;
                        height:{size}px;
                        border-radius:50%;
                        background-color:rgba(144, 202, 249, 0.4);
                        margin:auto;
                        transition:0.1s;">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                time.sleep(0.1)

        st.success("Great job! You completed the breathing exercise 💙")
    st.markdown('</div>', unsafe_allow_html=True)

def positive_affirmations():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("✨ Positive Affirmations")
    st.write("Take a moment to read and internalize these thoughts.")
    
    affirmations = [
        "You are capable of amazing things.",
        "Your worth is not defined by your productivity.",
        "It's okay to take a break and rest.",
        "You are stronger than you think.",
        "Every day is a new beginning.",
        "You are loved and appreciated.",
        "Your feelings are valid.",
        "Focus on progress, not perfection."
    ]
    
    if st.button("Get an Affirmation"):
        st.info(random.choice(affirmations))
    st.markdown('</div>', unsafe_allow_html=True)

def emoji_memory_game():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🧠 Mindfulness Memory")
    st.write("A gentle game to help focus your mind and distract from anxious thoughts.")
    
    # Simple placeholder for now to ensure it works
    st.write("This game is in development! Check back later for a soothing memory experience.")
    
    st.markdown('</div>', unsafe_allow_html=True)
