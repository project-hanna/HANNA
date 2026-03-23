import streamlit as st
from datetime import datetime
import base64
import os

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

# --- 2. LOGO ---
LOGO_FILE = "logo1.png"
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- 3. CSS BDD8.7 (FORCE-CENTER TOTAL) ---
st.markdown(f"""
    <style>
    /* Centrage du bloc principal */
    .main .block-container {{
        max-width: 550px !important;
        padding: 4rem 1rem !important;
        margin: 0 auto !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }}

    /* Force le centrage Streamlit */
    [data-testid="stVerticalBlock"] {{
        align-items: center !important;
        width: 100% !important;
    }}

    /* Header HANNA */
    .hanna-header {{
        width: 100% !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        margin-bottom: 3.5rem !important;
    }}

    .hanna-logo {{
        width: 120px !important;
        margin-bottom: 25px !important;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        font-size: 52px;
        letter-spacing: 14px; 
        margin-right: -14px !important; 
        text-transform: uppercase;
        line-height: 1;
        width: 100%;
        text-align: center;
    }}

    /* --- CORRECTION ULTIME DU CHAMP DE SAISIE --- */
    div.stTextInput {{
        width: 100% !important;
        max-width: 480px !important;
    }}

    /* Forçage chirurgical de l'input et du placeholder */
    div.stTextInput input {{ 
        text-align: center !important; 
        padding-left: 0 !important;
        padding-right: 0 !important;
        border-radius: 12px !important; 
        height: 50px !important;
        width: 100% !important;
    }}

    /* Forçage spécifique du placeholder pour TOUS les navigateurs */
    ::placeholder {{ text-align: center !important; opacity: 1; }}
    :-ms-input-placeholder {{ text-align: center !important; }}
    ::-ms-input-placeholder {{ text-align: center !important; }}
    ::-webkit-input-placeholder {{ text-align: center !important; }}
    ::-moz-placeholder {{ text-align: center !important; }}

    #MainMenu, footer, header {{ visibility: hidden; display: none !important; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. LOGIQUE ---
if 'notes' not in st.session_state: st.session_state.notes = []

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
        <p style="font-size: 9px; color: #999; letter-spacing: 2.5px; text-transform: uppercase; margin-top: 15px; margin-right: -2.5px;">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

st.text_input("CAPTURE", 
              placeholder="Demandez à HANNA", 
              label_visibility="collapsed", 
              key="entry_input", 
              on_change=handle_capture)

st.write("<br>", unsafe_allow_html=True)

for note in st.session_state.notes:
    st.markdown(f"""
        <div style="padding: 15px; border-radius: 12px; background: #FAFAFA; border: 1px solid #F0F0F0; margin-bottom: 12px; text-align: left; width: 100%;">
            <small style="color: #007BFF; font-weight: 800;">{note['time']}</small><br>{note['text']}
        </div>
    """, unsafe_allow_html=True)
