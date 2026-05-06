import streamlit as st
import pandas as pd 
from database import insert_forum_post, get_forum_posts

def post_message():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### ✍️ Share your thoughts")
    st.info("💡 **Community Guidelines:** This is a safe space. Please be kind, supportive, and respectful to others.")
    
    username = st.text_input("Username (Leave blank to post anonymously)")
    message = st.text_area("Your Message")
    
    if st.button("Post Message"):
        display_name = username if username.strip() else "Anonymous"
        if message.strip():
            success = insert_forum_post(display_name, message, is_anonymous=(not bool(username.strip())))
            if success:
                st.success("Message posted successfully!")
                st.rerun()
            else:
                st.error("Failed to post message.")
        else:
            st.error("Message cannot be empty.")
    st.markdown('</div>', unsafe_allow_html=True)

def display_forum():
    st.markdown("### 🗣️ Community Voices")
    posts = get_forum_posts()
    
    if not posts:
        st.write("No messages yet. Be the first to share!")
    
    # Iterate from newest to oldest based on fetched order (if ASC, reverse it)
    for post in reversed(posts):
        time_str = post['timestamp']
        if isinstance(time_str, str) and '.' in time_str:
            time_str = time_str.split('.')[0] # Remove microseconds if any
            
        st.markdown(f"""
        <div class="glass-card" style="padding: 1rem; margin-bottom: 1rem;">
            <strong>{post['username']}</strong> <span style="font-size: 0.8rem; color: #666;">• {time_str}</span>
            <p style="margin-top: 0.5rem; margin-bottom: 0;">{post['message']}</p>
        </div>
        """, unsafe_allow_html=True)