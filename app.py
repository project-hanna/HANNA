import streamlit as st
from datetime import datetime
import base64
import os

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

LOGO_FILE = "logo1.png"

@st.cache_data(show_spinner=False)
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- 2. ARCHITECTURE CSS (CENTRAGE TOTAL & SUPPRESSION UI) ---
st.markdown(f"""
    <style>
    /* Force le centrage vertical et horizontal du bloc principal */
    .stMainBlockContainer {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }}
    
    .block-container {{
        max-width: 500px !important;
        padding-top: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    /* Header & Logo Centré */
    .hanna-header {{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-bottom: 2.5rem;
    }}

    .hanna-logo {{
        width: 110px;
        height: auto;
        margin-bottom: 15px;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        letter-spacing: 12px;
        font-size: 42px;
        color: #1A1A1A;
        margin: 0;
        padding-left: 12px; /* Equilibre le letter-spacing pour un centrage optique */
    }}

    .hanna-sub {{
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        font-size: 9px;
        color: #999;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 8px;
    }}

    /* Input & Notes */
    div[data-baseweb="input"] {{ 
        border-radius: 12px !important; 
        width: 100% !important;
    }}
    input {{ text-align: center !important; }}
    
    .stButton > button {{
        width: 100%;
        border-radius: 10px;
        border: 1px solid #EEE;
        color: #CCC;
        font-size: 10px;
        margin-top: 40px;
    }}

    /* Masquer les éléments natifs Streamlit */
    #MainMenu, footer, header {{ visibility: hidden; height: 0; }}
    </style>
""", unsafe_allow_html=True)

# --- 3. RENDU DU HEADER ---
logo_html = f"<img src='data:image/png;base64,{LOGO_B64}' class='hanna-logo'>" if LOGO_B64 else ""

st.markdown(f"""
    <div class="hanna-header">
        {logo_html}
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. LOGIQUE DE CAPTURE (SANS CONNEXION) ---
if 'notes' not in st.session_state: 
    st.session_state.notes = []

def handle_capture():
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, {"time": ts, "text": entry})
        st.session_state.entry_input = "" 

# Zone de saisie directe
st.text_input("CAPTURE", placeholder="Capturez une idée ou une commande...", 
              label_visibility="collapsed", key="entry_input", on_change=handle_capture)

st.write("<br>", unsafe_allow_html=True)

# Affichage des flux
for note in st.session_state.notes:
    st.markdown(f"""
        <div style="padding: 14px; border-radius: 12px; background: #FBFBFB; border: 1px solid #F0F0F0; margin-bottom: 10px; width: 100%; text-align: left;">
            <span style="color: #007BFF; font-weight: bold; font-size: 11px;">{note['time']}</span>
            <span style="color: #333; font-size: 14px; margin-left: 10px;">{note['text']}</span>
        </div>
    """, unsafe_allow_html=True)

# Bouton de reset de session
if st.button("RÉINITIALISER LA SESSION"):
    st.session_state.clear()
    st.rerun()
