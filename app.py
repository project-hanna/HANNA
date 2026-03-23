import streamlit as st
from datetime import datetime
import base64
import os

# --- 1. CONFIGURATION INITIALE ---
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

# --- 3. ARCHITECTURE CSS (CENTRAGE FORCÉ) ---
st.markdown("""
    <style>
    /* Force le centrage de tous les blocs Streamlit */
    [data-testid="stVerticalBlock"] > div {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
    }

    .block-container { 
        padding-top: 3rem; 
        max-width: 500px !important; 
    }
    
    /* Style du Header */
    .hanna-header { 
        width: 100%;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .hanna-logo-wrapper {
        display: flex;
        justify-content: center;
        margin-bottom: 15px;
        width: 100%;
    }

    .hanna-logo { 
        width: 120px; 
        height: auto;
    }
    
    .hanna-title { 
        font-family: 'Inter', sans-serif;
        font-weight: 200; 
        letter-spacing: 14px; 
        font-size: 52px; 
        color: #000; 
        margin: 0;
        line-height: 1.1;
        text-transform: uppercase;
        /* Compensation du letter-spacing pour le centrage visuel */
        padding-left: 14px; 
    }
    
    .hanna-sub { 
        font-family: 'Inter', sans-serif;
        font-weight: 300; 
        font-size: 8px; 
        color: #999; 
        letter-spacing: 2px; 
        text-transform: uppercase;
        margin-top: 10px;
    }

    /* Inputs & Boutons */
    div.stTextInput > div > div > input { 
        text-align: center !important; 
        border-radius: 8px; 
        height: 45px; 
    }
    
    .stButton > button { 
        width: 100%; 
        background: transparent; 
        color: #ccc; 
        border: 1px solid #eee; 
        font-size: 10px; 
    }

    #MainMenu, footer, header { visibility: hidden; }
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
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, {"time": ts, "text": entry})
        st.session_state.entry_input = "" 

# --- 6. ROUTAGE ---
if not st.session_state.auth:
    pwd = st.text_input("ACCÈS", type="password", placeholder="CODE D'ACCÈS", label_visibility="collapsed")
    if pwd == PASSWORD_SYSTEM:
        st.session_state.auth = True
        st.rerun()
    elif pwd:
        st.error("Accès refusé.")
else:
    st.text_input("CAPTURE", placeholder="Demandez à HANNA", label_visibility="collapsed", key="entry_input", on_change=handle_capture)
    
    st.write("---")
    
    for note in st.session_state.notes:
        st.markdown(f"""
            <div style="padding: 12px; border-radius: 10px; background: #F9F9F9; border: 1px solid #EEE; margin-bottom: 8px; width: 100%; text-align: left;">
                <small style="color: #007BFF;">{note['time']}</small> <br> {note['text']}
            </div>
        """, unsafe_allow_html=True)

    if st.button("QUITTER LA SESSION"):
        st.session_state.clear()
        st.rerun()
