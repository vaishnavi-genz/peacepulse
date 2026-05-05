import streamlit as st
import pandas as pd 
if 'forum_posts' not in st.session_state:
    st.session_state.forum_posts = []

def post_message():
    st.subheader("Community Forum")
    username = st.text_input("Username")
    message = st.text_area("Message")
    if st.button("Post"):
        st.session_state.forum_posts.append({"username": username, "message": message, "time": pd.Timestamp.now()})
        st.success("Message posted successfully!")

def display_forum():
    st.subheader("Forum Messages")
    for post in st.session_state.forum_posts:
        st.write(f"**{post['username']}** ({post['time']}): {post['message']}")

post_message()
display_forum()