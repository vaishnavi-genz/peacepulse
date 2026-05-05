import streamlit as st
import random

def display_wearable_data():
    st.subheader("Wearable Data")
    heart_rate = random.randint(60, 100)  # Simulate heart rate data
    sleep_hours = random.uniform(4, 9)  # Simulate sleep data
    st.write(f"Heart Rate: {heart_rate} bpm")
    st.write(f"Sleep Duration: {sleep_hours:.2f} hours")
    
    if heart_rate > 90:
        st.warning("Your heart rate is higher than normal. Consider taking a break or doing a relaxation exercise.")
    if sleep_hours < 6:
        st.warning("You slept less than usual. Ensure you get enough rest.")

# Call the function to display wearable data
display_wearable_data()
