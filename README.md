<div align="center">
  <h1>🌿 PeacePulse</h1>
  <p><strong>Your modern, emotionally-intelligent mental wellness companion.</strong></p>
  <p>
    An AI-powered, adaptive digital wellness platform designed to provide a calming, supportive, and immersive experience for tracking moods, managing anxiety, and fostering daily mindfulness.
  </p>
</div>

<hr>

## 🌟 Overview
PeacePulse is not just a mood tracker; it is a holistic mental wellness ecosystem. Inspired by premium platforms like Calm and Headspace, PeacePulse features dynamic **glassmorphic** themes that visually adapt to your current mood, creating a seamless and empathetic environment. With integrated Gemini AI, curated music therapy, and interactive grounding exercises, PeacePulse helps you navigate your emotions safely and securely.

## ✨ Key Features
- **🎨 Emotionally Adaptive Themes**: The entire application UI dynamically shifts its colors, gradients, and styling to match your logged mood (e.g., cool blues for Sad, warm energetic pastels for Happy).
- **🤖 Gemini AI Wellness Chat**: A highly empathetic, non-judgmental AI companion powered by `gemini-1.5-flash` that contextually understands your current mood and offers gentle support and active listening.
- **📊 Intelligent Analytics**: Beautiful, transparent visual dashboards built with Matplotlib that track your emotional journey and offer data-driven, actionable wellness advice based on your historical trends.
- **🎵 Music Therapy**: Hand-curated, non-intrusive embedded audio therapy tailored specifically to elevate or calm your current emotional state.
- **🎮 Interactive Wellness Games**: 
  - **Guided Breathing**: A soothing 4-4-4-4 box breathing animation.
  - **5-4-3-2-1 Grounding**: A structured sensory exercise to anchor you in the present moment.
  - **Calm Matching**: A lightweight, cognitive cognitive memory game using serene emojis.
  - **Positive Affirmations**: A randomized, supportive quote generator.
- **🗣️ Safe Community Forum**: An anonymous, supportive digital space to share thoughts and realize you are not alone.
- **🔐 Secure Persistence**: All chats, moods, and forum posts are securely stored locally via SQLite, completely decoupled from the UI for enterprise-grade stability and future scalability. 

## 🛠️ Technology Stack
- **Frontend/UI**: [Streamlit](https://streamlit.io/) (with custom CSS injected for Glassmorphism)
- **AI Engine**: [Google Gemini API](https://aistudio.google.com/) (`gemini-1.5-flash`)
- **Database**: SQLite (built-in persistent local storage)
- **Authentication**: Firebase Authentication (with graceful Guest Session fallbacks)
- **Data Visualization**: Matplotlib & Pandas

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/peacepulse.git
   cd peacepulse
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Secrets:**
   Create a `.streamlit/secrets.toml` file in the root directory and add your API keys:
   ```toml
   GEMINI_API_KEY = "your_google_gemini_api_key_here"
   
   # Optional: Firebase Config if using full authentication
   [firebase]
   apiKey = "your_firebase_api_key"
   authDomain = "your_firebase_domain"
   databaseURL = "your_firebase_db_url"
   projectId = "your_firebase_project_id"
   storageBucket = "your_firebase_bucket"
   messagingSenderId = "your_sender_id"
   appId = "your_app_id"
   ```

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

## 🔒 Privacy & Security
PeacePulse is designed with privacy at its core. 
- **No API keys or passwords** are ever stored in the SQLite database. 
- The `.gitignore` is pre-configured to strictly ignore `secrets.toml` and `peacepulse.db` to prevent accidental data leaks.
- The AI chat strictly enforces a non-medical disclaimer and is programmed to recommend professional help in times of crisis.

## 🔮 Future Roadmap
- Integration with external cloud databases (e.g., Supabase, Firestore) for cross-device syncing.
- Wearable device integration for real-time biometric stress tracking.
- Voice-based journal entries.

<hr>
<div align="center">
  <i>"Peace is a journey of a thousand miles and it must be taken one step at a time."</i>
</div>
