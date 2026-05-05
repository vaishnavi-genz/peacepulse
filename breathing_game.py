import streamlit as st
import time

def breathing_game():
    st.title("🧘 Breathing Exercise")

    st.write("Follow the circle and breathe calmly")

    start = st.button("Start Breathing")

    if start:
        for i in range(5):  # 5 cycles

            # Inhale
            st.markdown(
                "<h3 style='text-align: center; color: green;'>Inhale...</h3>",
                unsafe_allow_html=True
            )
            circle = st.empty()

            for size in range(50, 200, 10):
                circle.markdown(
                    f"""
                    <div style="
                        width:{size}px;
                        height:{size}px;
                        border-radius:50%;
                        background-color:#6EC6FF;
                        margin:auto;
                        transition:0.1s;">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                time.sleep(0.1)

            # Hold
            st.markdown(
                "<h3 style='text-align: center;'>Hold...</h3>",
                unsafe_allow_html=True
            )
            time.sleep(2)

            # Exhale
            st.markdown(
                "<h3 style='text-align: center; color: red;'>Exhale...</h3>",
                unsafe_allow_html=True
            )

            for size in range(200, 50, -10):
                circle.markdown(
                    f"""
                    <div style="
                        width:{size}px;
                        height:{size}px;
                        border-radius:50%;
                        background-color:#90CAF9;
                        margin:auto;
                        transition:0.1s;">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                time.sleep(0.1)

        st.success("Great job! You completed the breathing exercise 💙")