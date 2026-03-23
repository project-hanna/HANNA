import streamlit as st
from datetime import datetime
import base64
import os

# --- 1. CONFIGURATION ÉTAPE 1 (DOIT ÊTRE AU DÉBUT) ---
st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

# --- 2. PARAMÈTRES & LOGO ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo1.png"

@st.cache_data(show_spinner=False)
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- 3. ARCHITECTURE CSS (CENTRAGE TOTAL) ---
st.markdown("""
    <style>
    /* Centrage du conteneur Streamlit */
    .block-container { 
        padding-top: 2rem; 
        max-width: 500px; 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
    }
    
    .hanna-header { 
        width: 100%;
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center;
        text-align: center; 
        margin-bottom: 2rem; 
    }
    
    .hanna-logo-wrapper {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 15px;
    }

    .hanna-logo { 
        width: 110px; 
        height: auto;
        display: block;
    }
    
    .hanna-title { 
        font-family: 'Inter', sans-serif;
        font-weight: 200; 
        letter-spacing: 12px; 
        font-size: 42px; 
        color: #1A1A1A; 
        margin: 0;
        line-height: 1.1;
        padding-left: 12px; /* Correction optique du centrage */
    }
    
    .hanna-sub { 
        font-family: 'Inter', sans-serif;
        font-weight: 300; 
        font-size: 9px; 
        color: #999; 
        letter-spacing: 1.5px; 
        text-transform: uppercase;
        margin-top: 8px;
    }

    div[data-baseweb="input"] { border-radius: 12px !important; border: 1px solid #EEE !important; }
    input { text-align: center !important; }
    
    .stButton > button { width: 100%; border-radius: 8px; color: #AAA; font-size: 11px; }

    #MainMenu, footer, header { visibility: hidden; height: 0; }
    </style>
""", unsafe_allow_html=True)

# --- 4. RENDU DU HEADER ---
logo_html = f"<div class='hanna-logo-wrapper'><img src='data:image/png;base64,{LOGO_B64}' class='hanna-logo'></div>" if LOGO_B64 else ""

st.markdown(f"""
    <div class="hanna-header">
        {logo_html}
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# --- 5. LOGIQUE DE SESSION ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'notes' not in st.session_state: st.session_state.notes = []

def handle_capture():
    entry
