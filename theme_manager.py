import streamlit as st

def apply_theme():
    if "current_mood" not in st.session_state:
        st.session_state.current_mood = "Neutral"
    
    mood = st.session_state.current_mood
    
    # Define aesthetic pastel themes
    themes = {
        "Happy": {
            "bg": "linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%)", # Fallback base
            "app_bg": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
            "sidebar": "rgba(255, 227, 204, 0.85)",
            "text": "#4A3f35",
            "text_secondary": "#6A5A4A",
            "accent": "#ff9a76",
            "card_bg": "rgba(255, 255, 255, 0.55)"
        },
        "Sad": {
            "app_bg": "linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%)",
            "sidebar": "rgba(212, 222, 249, 0.85)",
            "text": "#2b406e",
            "text_secondary": "#4A6296",
            "accent": "#5b86e5",
            "card_bg": "rgba(255, 255, 255, 0.5)"
        },
        "Angry": {
            "app_bg": "linear-gradient(135deg, #e3c5eb 0%, #a9c1ed 100%)",
            "sidebar": "rgba(216, 204, 242, 0.85)",
            "text": "#2d2942",
            "text_secondary": "#4B446B",
            "accent": "#8f73d6",
            "card_bg": "rgba(255, 255, 255, 0.55)"
        },
        "Anxious": {
            "app_bg": "linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%)",
            "sidebar": "rgba(203, 242, 196, 0.85)",
            "text": "#2e4d34",
            "text_secondary": "#486B50",
            "accent": "#5db86f",
            "card_bg": "rgba(255, 255, 255, 0.5)"
        },
        "Neutral": {
            "app_bg": "linear-gradient(135deg, #fdfbfb 0%, #e2ebf0 100%)",
            "sidebar": "rgba(235, 240, 245, 0.85)",
            "text": "#1e293b",
            "text_secondary": "#475569",
            "text_muted": "#64748b",
            "accent": "#64748b",
            "card_bg": "rgba(241, 245, 249, 0.65)"
        }
    }
    
    t = themes.get(mood, themes["Neutral"])
    
    custom_css = f"""
    <style>
        /* Import Google Fonts safely */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
        
        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif !important;
        }}
        
        /* App Background */
        [data-testid="stAppViewContainer"] {{
            background: {t['app_bg']} !important;
            background-attachment: fixed !important;
            transition: background 0.8s ease-in-out;
        }}
        
        [data-testid="stHeader"] {{
            background: transparent !important;
        }}
        
        /* Sidebar Background */
        [data-testid="stSidebar"] {{
            background-color: {t['sidebar']} !important;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-right: 1px solid rgba(255, 255, 255, 0.3);
            transition: background-color 0.8s ease-in-out;
        }}
        
        /* Global Text Colors - Aggressive override for readability */
        h1, h2, h3, h4, h5, h6, 
        [data-testid="stMarkdownContainer"] > p,
        [data-testid="stMarkdownContainer"] > ul,
        [data-testid="stMarkdownContainer"] > ol,
        [data-testid="stMarkdownContainer"] > li,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label,
        [data-testid="stMetricValue"],
        label, .st-emotion-cache-1wmy9hl {{
            color: {t['text']} !important;
        }}
        
        /* Secondary Text Elements */
        small, [data-testid="stMetricLabel"], [data-testid="stMetricDelta"] {{
            color: {t.get('text_secondary', t['text'])} !important;
        }}
        
        .glass-card, .glass-card * {{
            color: {t['text']};
        }}
        
        /* Buttons */
        .stButton > button {{
            background-color: {t['accent']} !important;
            color: white !important;
            border-radius: 20px !important;
            border: none !important;
            padding: 0.5rem 1.5rem !important;
            font-weight: 500 !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: all 0.3s ease !important;
        }}
        .stButton > button * {{
            color: white !important;
        }}
        .stButton > button:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1) !important;
            filter: brightness(1.05);
        }}
        
        /* Inputs */
        .stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div > div {{
            background-color: rgba(255, 255, 255, 0.85) !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.6) !important;
            color: #1e293b !important;
        }}
        
        /* Custom UI Component Classes */
        .glass-card {{
            background: {t['card_bg']};
            border-radius: 16px;
            padding: 1.5rem;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.08);
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease;
        }}
        .glass-card:hover {{
            transform: translateY(-2px);
        }}
        
        /* Chat messages styling */
        [data-testid="stChatMessage"] {{
            background: {t['card_bg']};
            border-radius: 16px;
            padding: 1rem;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 24px 0 rgba(0, 0, 0, 0.06);
            margin-bottom: 1rem;
        }}
        [data-testid="stChatMessage"] * {{
            color: {t['text']} !important;
        }}
        
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
