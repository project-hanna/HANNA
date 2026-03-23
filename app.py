import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION & SÉCURITÉ ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

@st.cache_data(show_spinner=False)
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- ARCHITECTURE CSS (CENTRAGE & DESIGN) ---
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; max-width: 500px; }
    .stApp { background-color: #FFFFFF; }
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400&display=swap');
    
    /* Centrage Absolu avec Flexbox */
    .hanna-header { 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center;
        text-align: center; 
        margin-bottom: 2rem; 
    }
    
    .hanna-logo-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 15px;
    }

    .hanna-logo { 
        width: 110px; 
        height: auto;
        filter: none;
        opacity: 1;
    }
    
    .hanna-title { 
        font-family: 'Inter', sans-serif;
        font-weight: 200; 
        letter-spacing: 12px; 
        font-size: 42px; 
        color: #1A1A1A; 
        margin: 0;
        line-height: 1.1;
        padding-left: 12px; /* Correction optique du letter-spacing */
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

    /* Champs de saisie */
    div[data-baseweb="input"] { 
        border-radius: 12px !important; 
        background: #FFFFFF !important; 
        border: 1px solid #EAEAEA !important; 
    }
    input { text-align: center !important; font-family: 'Inter', sans-serif !important; }
    
    /* Boutons */
    .stButton > button { 
        width: 100%; border-radius: 8px; border: 1px solid #EEE; 
        background: white; color: #AAA; font-size: 11px; margin-top: 20px;
    }
    .stButton > button:hover { color: #FF4B4B; border-color: #FF4B4B; }

    #MainMenu, footer, header { visibility: hidden; height: 0; }
    </style>
""", unsafe_allow_html=True)

# --- RENDU DU HEADER ---
logo_html = f"<div class='hanna-logo-container'><img src='data:image/png;base64,{LOGO_B64}' class='hanna-logo'></div>" if LOGO_B64 else ""

st.markdown(f"""
    <div class="hanna-header">
        {logo_html}
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# --- LOGIQUE DE SESSION ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'notes' not in st.session_state: st.session_state.notes = []

def handle_capture():
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, {"time": ts, "text": entry})
        st.session_state.entry_input = "" 

# --- ROUTAGE ---
if not st.session_state.auth:
    # Page de Connexion
    pwd = st.text_input("ACCÈS", type="password", placeholder="PASSWORD", label_visibility="collapsed")
    if pwd == PASSWORD_SYSTEM:
        st.session_state.auth = True
        st.rerun()
    elif pwd:
        st.caption("<p style='text-align:center; color:#FF4B4B;'>Accès refusé.</p>", unsafe_allow_html=True)
else:
    # Page de Capture
    st.text_input("CAPTURE", placeholder="Échanger avec HANNA...", label_visibility="collapsed", key="entry_input", on_change=handle_capture)
    
    st.write("<br>", unsafe_allow_html=True)
    
    for note in st.session_state.notes:
        st.markdown(f"""
            <div style="padding: 14px; border-radius: 12px; background: #F9F9F9; border: 1px solid #F0F0F0; margin-bottom: 10px;">
                <span style="color: #007BFF; font-weight: bold; font-size: 12px;">{note['time']}</span>
                <span style="color: #333; font-size: 14px; margin-left: 10px;">{note['text']}</span>
            </div>
        """, unsafe_allow_html=True)

    if st.button("TERMINER LA SESSION"):
        st.session_state.clear()
        st.rerun()
