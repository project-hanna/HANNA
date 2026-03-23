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

# --- 3. ARCHITECTURE CSS BDD8.8 (SOUS-TITRE AGRANDI & CURSEUR GAUCHE) ---
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

    [data-testid="stVerticalBlock"], 
    [data-testid="stVerticalBlock"] > div,
    [data-testid="stVerticalBlock"] > div > div {{
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }}

    .hanna-header {{
        width: 100% !important;
        text-align: center !important;
        margin-bottom: 3.5rem !important;
    }}

    .hanna-logo {{
        width: 120px !important;
        height: auto !important;
        margin-bottom: 25px !important;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        font-size: 52px;
        color: #000;
        text-transform: uppercase;
        margin: 0 !important;
        letter-spacing: 14px; 
        margin-right: -14px !important; 
        line-height: 1;
    }}

    .hanna-sub {{
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        font-size: 13px;
        color: #777;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 18px !important;
        margin-right: -3px !important;
        width: 100%;
        text-align: center;
    }}

    /* 4. CHAMP DE SAISIE : Curseur à GAUCHE */
    div.stTextInput {{
        width: 100% !important;
        max-width: 480px !important;
        margin: 0 auto !important;
    }}
    
    div.stTextInput input {{ 
        text-align: left !important; 
        padding-left: 20px !important; 
        border-radius: 12px !important; 
        border: 1px solid #EEE !important;
        height: 50px !important;
        background: #FDFDFD !important;
    }}

    ::placeholder {{ text-align: left !important; }}
    ::-webkit-input-placeholder {{ text-align: left !important; }}

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
        <img
