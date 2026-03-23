import streamlit as st
from datetime import datetime
import base64
import os

# --- 1. CONFIGURATION INITIALE ---
st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo1.png"

@st.cache_data(show_spinner=False)
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- 2. ARCHITECTURE CSS (CENTRAGE ABSOLU & RESPONSIVE) ---
st.markdown(f"""
    <style>
    /* Forcer le centrage de TOUT le contenu Streamlit */
    .stMainBlockContainer {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }}
    
    .block-container {{
        padding-top: 2rem;
        max-width: 500px !important;
        margin: auto;
    }}

    /* Header & Logo */
    .hanna-header {{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-bottom: 2rem;
    }}

    .hanna-logo-container {{
        margin-bottom: 15px;
        display: block;
    }}

    .hanna-logo {{
        width: 110px;
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        letter-spacing: 12px;
        font-size: 42px;
        color: #1A1A1A;
        margin: 0;
        padding-left: 12px; /* Equilibre le letter-spacing */
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

    /* UI Elements */
    div[data-baseweb="input"] {{ border-radius: 12px !important; }}
    input {{ text-align: center !important; font-size: 16px !important; }}
    
    .stButton > button {{
        width: 100%;
        border-radius: 10px;
        border: 1px solid #EEE;
        color: #BBB;
        font-size: 10px;
        margin-top: 20px;
    }}

    #MainMenu, footer, header {{ visibility: hidden; height: 0; }}
    </style>
""", unsafe_allow_html=True)

# --- 3. RENDU DU HEADER ---
logo_html = f"<div class='hanna-logo-container'><img src='data:image/png;base64,{LOGO_B64}' class='hanna-logo'></div>" if LOGO_B64 else ""

st.markdown(f"""
    <div class="hanna-header">
        {logo_html}
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. GESTION DE LA SESSION & LOGIQUE ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'notes' not in st.session_state: st.session_state.notes = []

def handle_capture():
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, {{"time": ts, "text": entry}})
        st.session_state.entry_input = "" 

# --- 5. ROUTAGE (LE RESTE DU CODE) ---
if not st.session_state.auth:
    # Page Connexion
    pwd = st.text_input("ACCÈS", type="password", placeholder="CODE D'ACCÈS", label_visibility="collapsed")
    if pwd == PASSWORD_SYSTEM:
        st.session_state.auth = True
        st.rerun()
    elif pwd:
        st.caption("<p style='text-align:center; color:red;'>Accès refusé.</p>", unsafe_allow_html=True)
else:
    # Interface Capture
    st.text_input("CAPTURE", placeholder="Échanger avec HANNA...", label_visibility="collapsed", key="entry_input", on_change=handle_capture)
    
    st.write("<br>", unsafe_allow_html=True)
    
    for note in st.session_state.notes:
        st.markdown(f"""
            <div style="padding: 14px; border-radius: 12px; background: #F9F9F9; border: 1px solid #F0F0F0; margin-bottom: 10px; width: 100%;">
                <span style="color: #007BFF; font-weight: bold; font-size: 11px;">{note['time']}</span>
                <span style="color: #333; font-size: 14px; margin-left: 10px;">{note['text']}</span>
            </div>
        """, unsafe_allow_html=True)

    if st.button("TERMINER LA SESSION"):
        st.session_state.clear()
        st.rerun()
