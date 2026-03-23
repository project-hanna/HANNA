import streamlit as st
from datetime import datetime
import base64
import os

# --- 1. CONFIGURATION ---
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

# --- 2. ARCHITECTURE CSS : LE "FORCE-CENTER" ---
st.markdown(f"""
    <style>
    /* Écrasement total des marges Streamlit */
    .main .block-container {{
        max-width: 500px !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }}

    /* Forcer chaque élément vertical au centre */
    [data-testid="stVerticalBlock"] > div {{
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }}

    /* Header Design */
    .hanna-container {{
        text-align: center !important;
        width: 100% !important;
        margin-bottom: 2rem;
    }}

    .hanna-logo {{
        width: 120px;
        margin: 0 auto 15px auto;
        display: block;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        letter-spacing: 14px;
        font-size: 52px;
        color: #000;
        text-transform: uppercase;
        margin: 0 !important;
        padding-left: 14px; /* Compensation cruciale du letter-spacing */
        line-height: 1.1;
    }}

    .hanna-sub {{
        font-weight: 300;
        font-size: 8px;
        color: #999;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 10px !important;
    }}

    /* Inputs & Boutons centrés */
    div.stTextInput {{ width: 100% !important; }}
    div.stTextInput > div > div > input {{
        text-align: center !important;
        border-radius: 10px !important;
    }}

    .stButton > button {{
        width: 100% !important;
        border-radius: 10px !important;
        background: transparent;
        color: #BBB;
        border: 1px solid #EEE;
        font-size: 10px;
        transition: 0.3s;
    }}
    .stButton > button:hover {{ color: #000; border-color: #000; }}

    /* Nettoyage UI */
    #MainMenu, footer, header {{ visibility: hidden; height: 0; }}
    </style>
""", unsafe_allow_html=True)

# --- 3. RENDU DU HEADER (CENTRÉ VIA DIV) ---
st.markdown(f"""
    <div class="hanna-container">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. LOGIQUE SESSION ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'notes' not in st.session_state: st.session_state.notes = []

def handle_capture():
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, {"time": ts, "text": entry})
        st.session_state.entry_input = "" 

# --- 5. ROUTAGE ---
if not st.session_state.auth:
    pwd = st.text_input("ACCÈS", type="password", placeholder="CODE D'ACCÈS", label_visibility="collapsed")
    if pwd == PASSWORD_SYSTEM:
        st.session_state.auth = True
        st.rerun()
    elif pwd:
        st.caption("<p style='text-align:center; color:red;'>Accès refusé.</p>", unsafe_allow_html=True)
else:
    st.text_input("CAPTURE", placeholder="Demandez à HANNA", label_visibility="collapsed", key="entry_input", on_change=handle_capture)
    
    st.write("<br>", unsafe_allow_html=True)
    
    for note in st.session_state.notes:
        st.markdown(f"""
            <div style="padding: 12px; border-radius: 10px; background: #F9F9F9; border: 1px solid #EEE; margin-bottom: 10px; width: 100%; text-align: left;">
                <small style="color: #007BFF; font-weight: bold;">{note['time']}</small><br>
                <span style="color: #333;">{note['text']}</span>
            </div>
        """, unsafe_allow_html=True)

    if st.button("QUITTER LA SESSION"):
        st.session_state.clear()
        st.rerun()
