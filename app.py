import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION & SÉCURITÉ ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo1.png"

st.set_page_config(
    page_title="HANNA", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

@st.cache_data(show_spinner=False)
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- ARCHITECTURE CSS RESPONSIVE (MOBILE & DESKTOP) ---
st.markdown("""
    <style>
    /* Reset général */
    .block-container { padding-top: 1.5rem; max-width: 450px; padding-left: 1rem; padding-right: 1rem; }
    .stApp { background-color: #FFFFFF; }
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400&display=swap');
    
    /* Centrage Header */
    .hanna-header { 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        text-align: center; 
        margin-bottom: 2rem; 
    }
    
    .hanna-logo-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 15px;
    }

    .hanna-logo { width: 90px; height: auto; }
    
    /* Titre Adaptatif */
    .hanna-title { 
        font-family: 'Inter', sans-serif;
        font-weight: 200; 
        letter-spacing: 12px; 
        font-size: 38px; 
        color: #1A1A1A; 
        margin: 0;
        line-height: 1.1;
        padding-left: 12px;
    }
    
    /* Media Query pour Mobile */
    @media (max-width: 480px) {
        .hanna-title { 
            font-size: 28px; 
            letter-spacing: 8px; 
            padding-left: 8px;
        }
        .hanna-logo { width: 75px; }
        .hanna-sub { font-size: 7px !important; }
    }
    
    .hanna-sub { 
        font-family: 'Inter', sans-serif;
        font-weight: 300; 
        font-size: 9px; 
        color: #999; 
        letter-spacing: 1.5px; 
        text-transform: uppercase;
        margin-top: 10px;
    }

    /* Style des Inputs */
    div[data-baseweb="input"] { 
        border-radius: 12px !important; 
        background: #F9FAFB !important; 
        border: 1px solid #EDEDED !important; 
    }
    input { text-align: center !important; font-size: 16px !important; } /* 16px évite le zoom auto sur iOS */
    
    /* Bouton Quitter */
    .stButton > button { 
        width: 100%; border-radius: 10px; border: 1px solid #F0F0F0; 
        background: white; color: #CCC; font-size: 10px; margin-top: 30px;
        height: 40px;
    }
    
    #MainMenu, footer, header { visibility: hidden; height: 0; }
    </style>
""", unsafe_allow_html=True)

# --- RENDU ---
logo_html = f"<div class='hanna-logo-container'><img src='data:image/png;base64,{LOGO_B64}' class='hanna-logo'></div>" if LOGO_B64 else ""

st.markdown(f"""
    <div class="hanna-header">
        {logo_html}
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# --- LOGIQUE ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'notes' not in st.session_state: st.session_state.notes = []

def handle_capture():
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, {"time": ts, "text": entry})
        st.session_state.entry_input = "" 

if not st.session_state.auth:
    pwd = st.text_input("ACCÈS", type="password", placeholder="CODE D'ACCÈS", label_visibility="collapsed")
    if pwd == PASSWORD_SYSTEM:
        st.session_state.auth = True
        st.rerun()
    elif pwd:
        st.caption("<p style='text-align:center; color:#FF4B4B;'>Accès refusé.</p>", unsafe_allow_html=True)
else:
    st.text_input("CAPTURE", placeholder="Notez ou demandez...", label_visibility="collapsed", key="entry_input", on_change=handle_capture)
    
    for note in st.session_state.notes:
        st.markdown(f"""
            <div style="padding: 12px; border-radius: 10px; background: #FFFFFF; border: 1px solid #F0F0F0; margin-top: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                <span style="color: #007BFF; font-weight: 600; font-size: 11px; font-family: 'Inter';">{note['time']}</span>
                <span style="color: #333; font-size: 14px; margin-left: 10px; font-family: 'Inter';">{note['text']}</span>
            </div>
        """, unsafe_allow_html=True)

    if st.button("QUITTER"):
        st.session_state.clear()
        st.rerun()
