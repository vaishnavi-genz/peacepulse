import streamlit as st
from database import get_user_moods

def display_wellness_suggestions():
    st.title("🌿 Wellness Suggestions")
    st.markdown("Gentle reminders and small steps to support your well-being today.")
    
    user_email = st.session_state.user.get('email', 'guest@peacepulse.local')
    df = get_user_moods(user_email)
    
    current_mood = st.session_state.get("current_mood", "Neutral")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.markdown("### Focus for Today")
    
    if current_mood == "Anxious":
        st.write("We sense you might be feeling overwhelmed. Here are gentle steps to regain your center:")
        st.markdown("- **Digital Detox**: Step away from screens for 15 minutes.")
        st.markdown("- **Box Breathing**: Try the Breathing Exercise in our Games section.")
        st.markdown("- **Physical Grounding**: Feel the texture of an object near you.")
    elif current_mood == "Sad":
        st.write("Take it easy on yourself today. Gentle self-care is your priority:")
        st.markdown("- **Warm Beverage**: Make a warm cup of tea or hot water.")
        st.markdown("- **Gentle Stretch**: Roll your shoulders and gently stretch your neck.")
        st.markdown("- **Kindness**: Read our Positive Affirmations in the Games section.")
    elif current_mood == "Angry":
        st.write("Your feelings are valid. Let's find a safe way to release this energy:")
        st.markdown("- **Journaling**: Write down exactly what is frustrating you, then tear up the paper.")
        st.markdown("- **Cool Down**: Splash some cold water on your face to reset your nervous system.")
        st.markdown("- **Movement**: Take a brisk 10-minute walk outside if possible.")
    elif current_mood == "Happy":
        st.write("It's wonderful that you're feeling good! Let's nurture this energy:")
        st.markdown("- **Gratitude**: Note down 3 small things that made you smile today.")
        st.markdown("- **Connect**: Share your good mood by sending a kind message to a friend.")
        st.markdown("- **Hydrate**: Drink a glass of water to keep your body feeling as good as your mind.")
    else:
        st.write("Balance is beautiful. Here are some daily habits to maintain your equilibrium:")
        st.markdown("- **Hydration Check**: Have you had a glass of water recently?")
        st.markdown("- **Posture Reset**: Sit up straight, drop your shoulders, and take one deep breath.")
        st.markdown("- **Micro-break**: Rest your eyes by looking at something 20 feet away for 20 seconds.")
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Analytics-driven suggestion
    if not df.empty and len(df) > 3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Insight-Driven Advice")
        
        mood_counts = df['mood'].value_counts()
        most_frequent = mood_counts.idxmax()
        
        if most_frequent == "Anxious":
            st.info("Based on your recent history, anxiety has been frequent. Consider scheduling a dedicated 10-minute 'worry time' each day, and keeping the rest of your day free from overthinking.")
        elif most_frequent == "Sad":
            st.info("We've noticed you've been feeling down over multiple sessions. Remember that it's okay to ask for professional help if these feelings persist. You don't have to carry it alone.")
        else:
            st.info("Your logging shows a great commitment to self-awareness! Continue tracking to build a stronger emotional map.")
            
        st.markdown('</div>', unsafe_allow_html=True)

def display_compact_wellness_suggestions(mood, df):
    st.markdown("#### 🌿 Focus for Today")
    
    if mood == "Anxious":
        st.write("We sense you might be feeling overwhelmed. Here are gentle steps to regain your center:")
        st.markdown("- **Digital Detox**: Step away from screens for 15 minutes.")
        st.markdown("- **Box Breathing**: Try the Breathing Exercise in our Games section.")
        st.markdown("- **Physical Grounding**: Feel the texture of an object near you.")
    elif mood == "Sad":
        st.write("Take it easy on yourself today. Gentle self-care is your priority:")
        st.markdown("- **Warm Beverage**: Make a warm cup of tea or hot water.")
        st.markdown("- **Gentle Stretch**: Roll your shoulders and gently stretch your neck.")
        st.markdown("- **Kindness**: Read our Positive Affirmations in the Games section.")
    elif mood == "Angry":
        st.write("Your feelings are valid. Let's find a safe way to release this energy:")
        st.markdown("- **Journaling**: Write down exactly what is frustrating you, then tear up the paper.")
        st.markdown("- **Cool Down**: Splash some cold water on your face to reset your nervous system.")
        st.markdown("- **Movement**: Take a brisk 10-minute walk outside if possible.")
    elif mood == "Happy":
        st.write("It's wonderful that you're feeling good! Let's nurture this energy:")
        st.markdown("- **Gratitude**: Note down 3 small things that made you smile today.")
        st.markdown("- **Connect**: Share your good mood by sending a kind message to a friend.")
        st.markdown("- **Hydrate**: Drink a glass of water to keep your body feeling as good as your mind.")
    else:
        st.write("Balance is beautiful. Here are some daily habits to maintain your equilibrium:")
        st.markdown("- **Hydration Check**: Have you had a glass of water recently?")
        st.markdown("- **Posture Reset**: Sit up straight, drop your shoulders, and take one deep breath.")
        st.markdown("- **Micro-break**: Rest your eyes by looking at something 20 feet away for 20 seconds.")
        
    # Analytics-driven suggestion
    if not df.empty and len(df) > 3:
        st.markdown("---")
        st.markdown("#### 📊 Insight-Driven Advice")
        
        mood_counts = df['mood'].value_counts()
        most_frequent = mood_counts.idxmax()
        
        if most_frequent == "Anxious":
            st.info("Based on your recent history, anxiety has been frequent. Consider scheduling a dedicated 10-minute 'worry time' each day, and keeping the rest of your day free from overthinking.")
        elif most_frequent == "Sad":
            st.info("We've noticed you've been feeling down over multiple sessions. Remember that it's okay to ask for professional help if these feelings persist. You don't have to carry it alone.")
        else:
            st.info("Your logging shows a great commitment to self-awareness! Continue tracking to build a stronger emotional map.")
