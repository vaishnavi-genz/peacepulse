import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import get_user_moods

def display_analytics():
    st.title("📊 Analytics & Insights")
    st.markdown("Understand your emotional patterns over time.")
    
    user_email = st.session_state.user.get('email', 'guest@peacepulse.local')
    df = get_user_moods(user_email)
    
    if df.empty:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.info("Not enough data to generate analytics. Start logging your moods in the Mood Tracking page!")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Total entries
    total_logs = len(df)
    
    # Most frequent mood
    mood_counts = df['mood'].value_counts()
    most_frequent_mood = mood_counts.idxmax()
    latest_mood = df.iloc[0]['mood']
    
    # Top metrics
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Logs", total_logs)
    col2.metric("Most Frequent", most_frequent_mood)
    col3.metric("Latest Mood", latest_mood)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Emotional Insights (Rule-based)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 💡 Wellness Insights")
    
    if most_frequent_mood == "Anxious":
        st.write("We noticed you've been feeling anxious frequently. Remember to take deep breaths. Our **Breathing Exercise** in the Therapeutic Games section might help ground you.")
    elif most_frequent_mood == "Sad":
        st.write("It seems you've been feeling down lately. Please remember to be kind to yourself. Reading **Positive Affirmations** might offer a small spark of comfort.")
    elif most_frequent_mood == "Angry":
        st.write("You've experienced a lot of anger recently. Finding a healthy outlet for this energy, or trying our **Breathing Exercise**, could be beneficial.")
    elif most_frequent_mood == "Happy":
        st.write("You've been having a lot of happy moments! That is wonderful. Take a moment to reflect on what's contributing to this joy and keep nurturing it.")
    else:
        st.write("Your moods are balanced. Consistency is key to emotional well-being. Keep logging to discover deeper patterns!")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Visualizations
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### Mood Distribution")
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        fig1.patch.set_alpha(0.0)
        ax1.patch.set_alpha(0.0)
        
        # Pastel colors for pie chart
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
        
        ax1.pie(mood_counts.values, labels=mood_counts.index, autopct='%1.1f%%', 
                startangle=90, colors=colors[:len(mood_counts)],
                textprops={'color': "#333333"})
        ax1.axis('equal')  
        st.pyplot(fig1)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_chart2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### Frequency by Mood")
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        fig2.patch.set_alpha(0.0)
        ax2.patch.set_alpha(0.0)
        
        mood_counts.plot(kind='bar', ax=ax2, color='#6EB5FF', edgecolor='none')
        ax2.set_ylabel("Count", color='#333333')
        ax2.tick_params(colors='#333333')
        ax2.spines['bottom'].set_color('#333333')
        ax2.spines['left'].set_color('#333333')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        
        # Rotate x labels for readability
        plt.xticks(rotation=45, ha='right')
        
        st.pyplot(fig2)
        st.markdown('</div>', unsafe_allow_html=True)
