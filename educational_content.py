import streamlit as st

def educational_resources():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("We've curated these trusted resources to help you learn more about mental well-being.")
    
    st.markdown("### 🌐 Trusted Organizations")
    st.write("- [Mental Health Foundation](https://www.mentalhealth.org.uk/)")
    st.write("- [National Institute of Mental Health](https://www.nimh.nih.gov/)")
    
    st.markdown("### 🧘‍♀️ Practices & Exercises")
    st.write("- [Mindfulness Exercises](https://www.mindful.org/)")
    
    st.markdown("### 📞 Emergency Support")
    st.warning("**If you are in immediate distress, please contact emergency services or a crisis hotline in your area.**")
    st.markdown('</div>', unsafe_allow_html=True)
