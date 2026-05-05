import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state for mood tracking
if 'mood_data' not in st.session_state:
    st.session_state.mood_data = []

def log_mood():
    st.subheader("Log Your Mood")
    mood = st.selectbox("How are you feeling?", ["Happy", "Sad", "Angry", "Anxious", "Neutral"])
    comment = st.text_area("Any additional comments?")
    if st.button("Submit"):
        st.session_state.mood_data.append({"mood": mood, "comment": comment, "time": pd.Timestamp.now()})
        st.success("Mood logged successfully!")

def display_mood_trends():
    st.subheader("Mood Trends")
    if len(st.session_state.mood_data) > 0:
        df = pd.DataFrame(st.session_state.mood_data)
        df['date'] = df['time'].dt.date
        mood_counts = df.groupby(['date', 'mood']).size().unstack(fill_value=0)
        st.line_chart(mood_counts)

#log_mood()
#display_mood_trends()
