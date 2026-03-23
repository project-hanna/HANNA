import streamlit as st
from datetime import datetime
import base64
import os

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

# --- 2. GESTION DU LOGO ---
LOGO_FILE = "logo1.png"
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- 3. ARCHITECTURE CSS BDD9 (ALIGNEMENT VERTICAL FORCÉ) ---
st.markdown(f"""
    <style>
    .main .block-container {{
        max-width: 550px !important;
        padding: 4rem 1rem !important;
        margin: 0 auto !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }}

    [data-testid="stVerticalBlock"] {{
        align-items: center !important;
        width: 100% !important;
    }}

    .hanna-header {{
        width: 100% !important;
        margin-bottom: 3.5rem !important;
        text-align: center !important;
    }}

    .hanna-logo {{
        width: 120px !important;
        margin-bottom: 25px !important;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        font-size: 52px;
        color: #000;
        text-transform: uppercase;
        letter-spacing: 14px; 
        margin-right: -14px !important; 
        line-height: 1;
    }}

    /* CHAMP DE SAISIE */
    div.stTextInput {{
        width: 100% !important;
        max-width: 480px !important;
    }}
    
    div.stTextInput input {{ 
        text-align: left !important; 
        padding: 0 20px !important;
        border-radius: 12px !important; 
        border: 1px solid #EEE !important;
        
        /* ALIGNEMENT VERTICAL STRICT */
        height: 50px !important;
        line-height: 50px !important; 
    }}

    /* PLACEHOLDER AU CENTRE */
    div.stTextInput input::placeholder {{ 
        text-align: center !important;
        line-height: 50px !important;
    }}
    div.stTextInput input::-webkit-input-placeholder {{ 
        text-align: center !important;
        line-height: 50px !important;
    }}

    #MainMenu, footer, header {{ visibility: hidden; display: none !important; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. LOGIQUE DE CAPTURE ---
if 'notes' not in st.session_state: 
    st.session_state.notes = []

def handle_capture():
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, {"time": ts, "text": entry})
        st.session_state.entry_input = "" 

# --- 5. RENDU ---
st.markdown(f"""
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">HANNA</h1>
        <p style="font-family: 'Inter'; font-weight: 300; font-size: 9px; color: #9
