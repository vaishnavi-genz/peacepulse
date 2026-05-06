import streamlit as st
import time
import random

def breathing_game():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🧘 Guided Breathing")
    st.write("Follow the prompt. Focus entirely on your breath.")
    
    start = st.button("Start 1-Minute Session")
    
    if start:
        placeholder = st.empty()
        cycles = 5 
        
        for _ in range(cycles):
            placeholder.markdown("<h2 style='text-align: center; color: #5db86f;'>Breathe In... (4s)</h2>", unsafe_allow_html=True)
            time.sleep(4)
            placeholder.markdown("<h2 style='text-align: center; color: #64748b;'>Hold... (4s)</h2>", unsafe_allow_html=True)
            time.sleep(4)
            placeholder.markdown("<h2 style='text-align: center; color: #5b86e5;'>Breathe Out... (4s)</h2>", unsafe_allow_html=True)
            time.sleep(4)
            
        placeholder.markdown("<h2 style='text-align: center; color: #333;'>Session Complete. Well done. 🌿</h2>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def positive_affirmations():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("✨ Positive Affirmations")
    
    affirmations = [
        "I am worthy of peace and calm.",
        "My feelings are valid, but they do not define me.",
        "I have survived every difficult day of my life so far.",
        "I am doing my best, and that is absolutely enough.",
        "I give myself permission to rest and heal.",
        "I choose to be kind to myself today.",
        "I am stronger than my anxious thoughts."
    ]
    
    if 'current_affirmation' not in st.session_state:
        st.session_state.current_affirmation = random.choice(affirmations)
        
    if st.button("Get a New Affirmation"):
        st.session_state.current_affirmation = random.choice(affirmations)
        
    st.markdown(f"""
        <div style='padding: 2rem; background: rgba(255,255,255,0.4); border-radius: 12px; text-align: center; margin-top: 1rem;'>
            <h3 style='color: #4A3f35; font-style: italic;'>"{st.session_state.current_affirmation}"</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def emoji_memory_game():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🧩 Calm Matching")
    st.write("A gentle, pressure-free cognitive exercise.")
    
    if 'memory_cards' not in st.session_state:
        emojis = ['🌸', '🌿', '🕊️', '🦋'] * 2
        random.shuffle(emojis)
        st.session_state.memory_cards = emojis
        st.session_state.flipped = []
        st.session_state.matched = []
        
    if st.button("Reset Game"):
        emojis = ['🌸', '🌿', '🕊️', '🦋'] * 2
        random.shuffle(emojis)
        st.session_state.memory_cards = emojis
        st.session_state.flipped = []
        st.session_state.matched = []
        st.rerun()

    cols = st.columns(4)
    for i in range(8):
        with cols[i % 4]:
            if i in st.session_state.matched or i in st.session_state.flipped:
                st.markdown(f"<div style='font-size: 2rem; text-align: center; padding: 10px; background: rgba(255,255,255,0.6); border-radius: 8px;'>{st.session_state.memory_cards[i]}</div>", unsafe_allow_html=True)
            else:
                if st.button("❓", key=f"card_{i}"):
                    if len(st.session_state.flipped) < 2:
                        st.session_state.flipped.append(i)
                        st.rerun()
                        
    if len(st.session_state.flipped) == 2:
        idx1, idx2 = st.session_state.flipped
        if st.session_state.memory_cards[idx1] == st.session_state.memory_cards[idx2]:
            st.session_state.matched.extend([idx1, idx2])
            st.session_state.flipped = []
            st.success("Match found! ✨")
            time.sleep(1)
            st.rerun()
        else:
            st.warning("Not quite. Take your time.")
            time.sleep(1)
            st.session_state.flipped = []
            st.rerun()
            
    if len(st.session_state.matched) == 8:
        st.balloons()
        st.success("Beautiful! You completed the gentle matching exercise.")
        
    st.markdown('</div>', unsafe_allow_html=True)

def grounding_exercise():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🌍 5-4-3-2-1 Grounding")
    st.write("This exercise helps bring you back to the present moment. Go at your own pace.")
    
    st.markdown("""
    - **5** things you can **see** around you. (e.g., a pen, a cloud, a plant)
    - **4** things you can **physically feel**. (e.g., your feet on the floor, the texture of your shirt)
    - **3** things you can **hear**. (e.g., traffic, birds, the hum of a fan)
    - **2** things you can **smell**. (e.g., coffee, fresh air, a candle)
    - **1** thing you can **taste**. (e.g., a sip of water, a mint)
    """)
    
    if st.button("I feel more grounded"):
        st.success("Wonderful. Carry this presence with you into your day. 🌿")
    st.markdown('</div>', unsafe_allow_html=True)
