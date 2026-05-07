import streamlit as st
from database import insert_chat_log, get_recent_chat_history

# Handle import gracefully
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

def initialize_chatbot():
    """Configures the Gemini API."""
    if not GENAI_AVAILABLE or "GEMINI_API_KEY" not in st.secrets:
        return None
    
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
        return model
    except Exception as e:
        print(f"Error configuring Gemini: {e}")
        return None

def get_system_prompt():
    """Generates the empathetic system prompt based on user's current mood."""
    current_mood = st.session_state.get("current_mood", "Neutral")
    
    prompt = f"""
You are the PeacePulse AI Wellness Assistant. Your primary role is to provide warm, calming, and emotionally supportive conversation.
The user's current mood is: {current_mood}.

Guidelines:
1. Tone: Warm, empathetic, non-judgmental, and naturally conversational. Avoid sounding like a robotic AI or overly formal.
2. Length: Keep responses short to medium (1-3 brief paragraphs).
3. Actions: Gently encourage positive thinking. Occasionally suggest brief breathing exercises, taking breaks, hydration, journaling, or listening to calming music if it fits the context.
4. Disclaimer: You are NOT a therapist. Do not provide medical diagnoses or dangerous advice. 
5. Crisis Handling: If the user expresses severe emotional distress, self-harm, or crisis, immediately and calmly encourage them to seek help from a trusted friend, family member, or professional mental health hotline. Do not attempt to counsel a crisis yourself.

Respond to the user with these guidelines in mind.
"""
    return prompt

def display_chatbot():
    st.title("🤖 AI Wellness Chat")
    
    st.markdown('<div class="glass-card" style="padding: 1rem; margin-bottom: 2rem;">', unsafe_allow_html=True)
    st.info("⚠️ **Disclaimer:** This chatbot provides emotional support only and is not a replacement for professional mental health care.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    model = initialize_chatbot()
    if not model:
        st.warning("⚠️ AI chatbot is currently unavailable. Please configure the Gemini API key in Streamlit secrets or install the required `google-generativeai` package.")
        return
        
    user_email = st.session_state.user.get('email', 'guest@peacepulse.local')
    
    # Initialize chat history in session state
    if "chat_messages" not in st.session_state:
        history = get_recent_chat_history(user_email, limit=20)
        if history:
            st.session_state.chat_messages = history
        else:
            # Add a welcoming initial message
            welcome_msg = "Hello! I'm here to listen and support you. How are you feeling right now?"
            st.session_state.chat_messages = [{"role": "assistant", "content": welcome_msg}]
            insert_chat_log(user_email, "assistant", welcome_msg)

    # Display chat messages from history
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Share your thoughts here..."):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Add user message to chat history
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        insert_chat_log(user_email, "user", prompt)
        
        # Enforce session state limit to prevent memory bloat
        if len(st.session_state.chat_messages) > 20:
            st.session_state.chat_messages = st.session_state.chat_messages[-20:]

        # Generate response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            # Build a text-based history log to safely pass context to Gemini
            # Keep only the last 6 messages to avoid memory bloat and save tokens
            conversation_log = ""
            recent_msgs = st.session_state.chat_messages[-7:-1] 
            for msg in recent_msgs:
                role_name = "AI" if msg["role"] == "assistant" else "User"
                conversation_log += f"{role_name}: {msg['content']}\n"
            
            prompt_with_context = f"""{get_system_prompt()}
            
Recent Conversation:
{conversation_log}

User: {prompt}
AI: """
            
            try:
                with st.spinner("Thinking gently..."):
                    response = model.generate_content(prompt_with_context)
                
                # --- TEMPORARY DEBUG OUTPUT ---
                with st.expander("🚨 DEBUG: Raw Gemini Response Structure", expanded=True):
                    st.write("**Response Type:**", str(type(response)))
                    try:
                        st.write("**Response Text:**", response.text)
                    except Exception as e:
                        st.write("**Response Text Error:**", str(e))
                    try:
                        st.write("**Candidates:**", response.candidates)
                        if len(response.candidates) > 0:
                            st.write("**Finish Reason:**", response.candidates[0].finish_reason)
                            st.write("**Safety Ratings:**", response.candidates[0].safety_ratings)
                    except Exception as e:
                        st.write("**Candidates Access Error:**", str(e))
                    try:
                        st.write("**Parts:**", response.parts)
                    except Exception as e:
                        st.write("**Parts Access Error:**", str(e))
                # ------------------------------

                # Robust response extraction
                full_response = None
                
                try:
                    if hasattr(response, 'text') and response.text:
                        full_response = response.text
                    elif hasattr(response, 'candidates') and len(response.candidates) > 0:
                        candidate = response.candidates[0]
                        if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts') and len(candidate.content.parts) > 0:
                            full_response = candidate.content.parts[0].text
                    elif hasattr(response, 'parts') and len(response.parts) > 0:
                        full_response = response.parts[0].text
                except Exception as parse_err:
                    st.error(f"🚨 DEBUG PARSE EXCEPTION: {str(parse_err)}")
                
                # Handle safety blocks or empty content
                if not full_response:
                    is_blocked = False
                    try:
                        if hasattr(response, 'candidates') and len(response.candidates) > 0:
                            finish_reason = getattr(response.candidates[0], 'finish_reason', None)
                            if finish_reason and getattr(finish_reason, 'name', str(finish_reason)) == 'SAFETY':
                                is_blocked = True
                            elif str(finish_reason) == '3': # Safety code
                                is_blocked = True
                    except:
                        pass
                        
                    if is_blocked:
                        full_response = "I hear you. That sounds really heavy, and while I want to be here for you, I'm an AI and have some limits on what I can discuss safely. If you're in distress, please reach out to a trusted professional."
                    else:
                        full_response = "I felt your message, but my response didn't come through clearly. Could we try again gently?"

                message_placeholder.markdown(full_response)
                
                # Add assistant response to chat history
                st.session_state.chat_messages.append({"role": "assistant", "content": full_response})
                insert_chat_log(user_email, "assistant", full_response)
                
                # Enforce session state limit
                if len(st.session_state.chat_messages) > 20:
                    st.session_state.chat_messages = st.session_state.chat_messages[-20:]
                
            except Exception as e:
                import traceback
                err_str = str(e)
                tb_str = traceback.format_exc()
                
                # --- TEMPORARY DEBUG OUTPUT ---
                with st.expander("🚨 DEBUG: API Exception Details", expanded=True):
                    st.write(f"**Error Type:** {type(e).__name__}")
                    st.write(f"**Error Message:** {err_str}")
                    st.code(tb_str, language='python')
                # ------------------------------

                if "API_KEY_INVALID" in err_str or "API key not valid" in err_str:
                    error_msg = "It seems my API key isn't configured correctly. Please check the Streamlit secrets."
                elif "Quota exceeded" in err_str or "429" in err_str or "Resource has been exhausted" in err_str:
                    error_msg = "I'm receiving a lot of thoughts right now and need a short break. Please take a slow, deep breath and try again in a minute."
                elif "DeadlineExceeded" in err_str or "503" in err_str or "Timeout" in err_str:
                    error_msg = "The connection is a bit slow right now. Let's take a deep breath and try again in a moment."
                else:
                    error_msg = "I couldn't quite process that. Could we try again gently?"
                    
                message_placeholder.error(error_msg)
