import streamlit as st
import requests
import whisper
import torch
import os
import speech_recognition as sr
from dotenv import load_dotenv  # Environment variables parhne ke liye

# --- SECURE CONFIG LOADING ---
load_dotenv()  # Ye .env file se keys uthaye ga

# Chabiyaan variables mein rakhein (GitHub par nazar nahi aayengi)
API_KEY = os.getenv("ANYTHINGLLM_API_KEY")
BASE_URL = os.getenv("ANYTHINGLLM_BASE_URL")


# --- MODELS (M4 Optimized) ---
@st.cache_resource
def load_whisper():
    # Apple M4 chip ki taqat use karne ke liye MPS (Metal Performance Shaders)
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    return whisper.load_model("base").to(device)


model = load_whisper()

# --- PAGE SETUP ---
st.set_page_config(page_title="Pashto AI Pro", page_icon="🇵🇰", layout="wide")

# --- INITIALIZE SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "voice_text" not in st.session_state:
    st.session_state.voice_text = ""

# --- UI STYLING (Eye-Friendly) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #f9fafb; }
    section[data-testid="stSidebar"] { background-color: #064e3b !important; color: #ecfdf5 !important; }
    .user-bubble {
        background-color: #065f46; color: white; padding: 18px;
        border-radius: 20px 20px 4px 20px; margin-bottom: 12px;
        text-align: right; direction: RTL; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-left: 15%;
    }
    .ai-bubble {
        background-color: white; color: #1f2937; padding: 18px;
        border-radius: 20px 20px 20px 4px; margin-bottom: 12px;
        text-align: right; direction: RTL; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-right: 15%; border: 1px solid #e5e7eb;
    }
    .stTextInput input { border-radius: 12px !important; padding: 12px !important; border: 1px solid #d1d5db !important; }
    .main-header { text-align: center; background: white; padding: 2rem; border-radius: 24px; box-shadow: 0 10px 25px rgba(0,0,0,0.03); margin-bottom: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    # Local asset use karna professional hai
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/32/Flag_of_Pakistan.svg", width=100)
    st.title("🗂️ Loci_Vault")
    st.file_uploader("Upload Pashto Documents", type=["pdf", "txt"])
    st.markdown("---")
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()
    st.caption(f"**Developer:** Mujahid Ur Rehman\n**Engine:** M4 Apple Silicon")

# --- HEADER ---
st.markdown(
    '<div class="main-header"><h1 style="color: #064e3b; margin:0;">🇵🇰 پښتو هوښيار مرستندوی</h1><p style="color: #6b7280;">High-Performance Local Intelligence</p></div>',
    unsafe_allow_html=True)


# --- VOICE LOGIC ---
def record_voice():
    r = sr.Recognizer()
    # Path ko root folder par rakha hai taake cleanup asaan ho
    temp_path = os.path.join(os.getcwd(), "temp.wav")

    with sr.Microphone() as source:
        st.toast("🎤 Listening to Pashto...")
        audio = r.listen(source, phrase_time_limit=7)
        with open(temp_path, "wb") as f:
            f.write(audio.get_wav_data())

    # Whisper Transcription
    result = model.transcribe(temp_path, language="ps", fp16=False)

    # Cleanup: Audio file delete karna security ke liye zaruri hai
    if os.path.exists(temp_path):
        os.remove(temp_path)

    return result['text']


# --- CHAT DISPLAY ---
chat_container = st.container()
with chat_container:
    for msg in st.session_state.messages:
        div_class = "user-bubble" if msg["role"] == "user" else "ai-bubble"
        icon = "👤" if msg["role"] == "user" else "🤖"
        st.markdown(
            f'<div class="{div_class}"><b>{icon} {"تاسو" if msg["role"] == "user" else "AI"}:</b><br>{msg["content"]}</div>',
            unsafe_allow_html=True)

# --- INPUT AREA ---
st.markdown("---")
with st.container():
    col1, col2, col3 = st.columns([0.5, 4, 0.5])
    with col1:
        if st.button("🎤"):
            voice_result = record_voice()
            st.session_state.voice_text = voice_result
            st.rerun()
    with col2:
        user_input = st.text_input("خپله پوښتنه دلته ولیکئ...", value=st.session_state.voice_text,
                                   placeholder="Type or use Mic...", label_visibility="collapsed")
    with col3:
        send_btn = st.button("🚀")

if send_btn and user_input:
    st.session_state.voice_text = ""
    st.session_state.messages.append({"role": "user", "content": user_input})
  
    with st.spinner("AI thinking..."):
        # API call using Secure Variables
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        try:
            response = requests.post(BASE_URL, headers=headers, json={"message": user_input, "mode": "chat"})
            if response.status_code == 200:
                ans = response.json().get('textResponse')
                st.session_state.messages.append({"role": "assistant", "content": ans})
                st.rerun()
            else:
                st.error("Error: Could not connect to local AI server.")
        except Exception as e:
            st.error(f"Connection Error: {e}")