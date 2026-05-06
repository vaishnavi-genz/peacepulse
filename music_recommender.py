import streamlit as st

def get_music_recommendations(mood):
    # Curated, non-autoplay generic relaxing tracks
    music_map = {
        "Sad": [
            {"title": "Uplifting Acoustic Morning", "url": "https://www.youtube.com/watch?v=-qY_rI6Y15c", "desc": "Gentle, hopeful acoustic guitars to slowly lift your spirits."},
        ],
        "Anxious": [
            {"title": "Deep Calming Piano", "url": "https://www.youtube.com/watch?v=lFcSrYw-ARY", "desc": "Soft, slow piano to help slow your breathing and calm your racing thoughts."},
        ],
        "Angry": [
            {"title": "Relaxing Ambient Rain", "url": "https://www.youtube.com/watch?v=mPZkdNFkNps", "desc": "Cooling rain sounds and soft ambient tones to help release tension."},
        ],
        "Happy": [
            {"title": "Upbeat Lofi Chill", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk", "desc": "Energetic but relaxed lofi beats to celebrate your positive mood."},
        ],
        "Neutral": [
            {"title": "Peaceful Lofi Beats", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk", "desc": "A balanced, chill background track for focusing or relaxing."}
        ]
    }
    
    return music_map.get(mood, music_map["Neutral"])

def display_music_therapy():
    st.title("🎵 Music Therapy")
    st.markdown("Immerse yourself in sounds carefully selected for your emotional state.")
    
    current_mood = st.session_state.get("current_mood", "Neutral")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(f"### Curated for your mood: **{current_mood}**")
    
    recs = get_music_recommendations(current_mood)
    
    for rec in recs:
        st.markdown(f"#### {rec['title']}")
        st.write(rec['desc'])
        # Streamlit st.video automatically prevents autoplay and is mobile responsive
        st.video(rec['url'])
        st.markdown("<br>", unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.info("💡 **Tip:** Listen with headphones and take a few slow, deep breaths while the music plays.")
    st.markdown('</div>', unsafe_allow_html=True)
