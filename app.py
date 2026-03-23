import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

# --- LOGO ---
LOGO_FILE = "logo1.png"
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""
LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- CSS BDD 8.8 (HAUTEUR AJUSTÉE À 60PX) ---
st.markdown(f"""
    <style>
    .main .block-container {{
        max-width: 550px !important; padding: 4rem 1rem !important; margin: 0 auto !important;
        display: flex !important; flex-direction: column !important; align-items: center !important;
    }}
    [data-testid="stVerticalBlock"] {{ align-items: center !important; width: 100% !important; }}
    .hanna-header {{ width: 100% !important; text-align: center !important; margin-bottom: 3.5rem !important; }}
    .hanna-logo {{ width: 120px !important; margin-bottom: 25px !important; }}
    .hanna-title {{
        font-family: 'Inter', sans-serif; font-weight: 200; font-size: 52px;
        letter-spacing: 14px; margin-right: -14px !important; text-transform: uppercase; line-height: 1;
    }}
    div.stTextInput {{ width: 100% !important; max-width: 480px !important; }}
    div.stTextInput input {{ 
        text-align: left !important; padding: 0 20px !important;
        border-radius: 12px !important; border: 1px solid #EEE !important;
        height: 60px !important; /* HAUTEUR PASSÉE À 60PX */
        width: 100% !important;
    }}
    ::placeholder {{ text-align: left !important; }}
    #MainMenu, footer, header {{ visibility: hidden; display: none !important; }}
    </style>
""", unsafe_allow_html=True)

# --- LOGIQUE ---
if 'notes' not in st.session_state: st.session_state.notes = []

def handle_capture():
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, {"time": ts, "text": entry})
        st.session_state.entry_input = "" 

# --- RENDU ---
st.markdown(f"""
    <div class="hanna-header" style="display: flex; flex-direction: column; align-items: center;">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">HANNA</h1>
        <p style="font-family: 'Inter'; font-size: 9px; color: #999; letter-spacing: 2.5px; text-transform: uppercase; margin-top: 15px;">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

st.text_input("CAPTURE", placeholder="Demander à HANNA", label_visibility="collapsed", key="entry_input", on_change=handle_capture)

st.write("<br>", unsafe_allow_html=True)

for note in st.session_state.notes:
    st.markdown(f"""
        <div style="padding: 15px; border-radius: 12px; background: #FAFAFA; border: 1px solid #F0F0F0; margin-bottom: 12px; width: 100%; text-align: left;">
            <small style="color: #007BFF; font-weight: 800; font-size: 11px;">{note['time']}</small><br>
            <span style="color: #222; font-size: 15px;">{note['text']}</span>
        </div>
    """, unsafe_allow_html=True)
