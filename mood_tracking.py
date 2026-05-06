import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import insert_mood, get_user_moods

def log_mood():
    st.markdown("### How are you feeling today?")
    
    mood = st.selectbox("Select your mood", ["Neutral", "Happy", "Sad", "Angry", "Anxious"], key="mood_selector")
    comment = st.text_area("Any additional thoughts? (Optional)", placeholder="Write what's on your mind...")
    
    if st.button("Log Mood", use_container_width=True):
        user_email = st.session_state.user.get('email', 'guest@peacepulse.local')
        success = insert_mood(user_email, mood, comment)
        
        if success:
            st.session_state.current_mood = mood
            st.success("Mood logged successfully! Your environment is adapting to support you.")
            st.rerun()
        else:
            st.error("Failed to log mood. Please try again.")

def display_mood_trends():
    st.markdown("### Your Mood History")
    
    user_email = st.session_state.user.get('email', 'guest@peacepulse.local')
    df = get_user_moods(user_email)
    
    if not df.empty:
        # Display latest moods in cards
        st.markdown("#### Recent Entries")
        for _, row in df.head(3).iterrows():
            formatted_time = row['time'].strftime("%b %d, %Y - %H:%M")
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.4); padding: 10px; border-radius: 8px; margin-bottom: 10px; border: 1px solid rgba(255,255,255,0.3);">
                <strong>{row['mood']}</strong> <span style="color: #666; font-size: 0.8rem;">• {formatted_time}</span>
                {f'<p style="margin: 5px 0 0 0; font-size: 0.9rem;">"{row["comment"]}"</p>' if row['comment'] else ''}
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("---")
        
        # Simple trend plot
        df['date'] = df['time'].dt.date
        mood_counts = df.groupby(['date', 'mood']).size().unstack(fill_value=0)
        
        fig, ax = plt.subplots(figsize=(8, 4))
        # Ensure plot background is transparent to match glass cards
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
        
        mood_counts.plot(kind='line', marker='o', ax=ax, linewidth=2)
        ax.set_ylabel("Frequency", color='#333333')
        ax.set_xlabel("Date", color='#333333')
        ax.tick_params(colors='#333333')
        ax.spines['bottom'].set_color('#333333')
        ax.spines['left'].set_color('#333333')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Legend styling
        legend = ax.legend(frameon=False)
        plt.setp(legend.get_texts(), color='#333333')
        
        st.pyplot(fig)
    else:
        st.info("Log your mood to see your trends here.")
