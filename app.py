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

# --- 3. CSS FORCE-CENTER (CENTRAGE ABSOLU) ---
st.markdown(f"""
    <style>
    /* Centrage du bloc principal */
    .main .block-container {{
        max-width: 500px !important;
        padding-top: 2rem !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }}

    /* Force le centrage de tous les éléments internes de Streamlit */
    [data-testid="stVerticalBlock"] > div {{
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        text-align: center !important;
    }}

    /* Header HANNA */
    .hanna-header {{
        width: 100% !important;
        text-align: center !important;
        margin-bottom: 2rem !important;
    }}

    .hanna-logo {{
        width: 120px !important;
        display: block !important;
        margin: 0 auto 15px auto !important;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        letter-spacing: 14px;
        font-size: 52px;
        color: #000;
        text-transform: uppercase;
        margin: 0 !important;
        padding-left: 14px; /* Centrage visuel exact */
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

    /* Champ Saisie Centré */
    div.stTextInput {{ width: 100% !important; }}
    div.stTextInput input {{ 
        text-align: center !important; 
        border-radius: 10px !important; 
        border: 1px solid #EEE !important;
    }}

    /* Suppression Header/Footer Streamlit */
    #MainMenu, footer, header {{ visibility: hidden; height: 0; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. LOGIQUE CAPTURE ---
if 'notes' not in st.session_state: 
    st.session_state.notes = []

def handle_capture():
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, {"time": ts, "text": entry})
        st.session_state.entry_input = "" 

# --- 5. RENDU ---
# Header
st.markdown(f"""
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# Input principal
st.text_input("CAPTURE", placeholder="Demandez à HANNA", label_visibility="collapsed", key="entry_input", on_change=handle_capture)

st.write("<br>", unsafe_allow_html=True)

# Liste des captures
for note in st.session_state.notes:
    st.markdown(f"""
        <div style="padding: 12px; border-radius: 10px; background: #F9F9F9; border: 1px solid #EEE; margin-bottom: 10px; width: 100%; text-align: left;">
            <small style="color: #007BFF; font-weight: bold;">{note['time']}</small><br>
            <span style="color: #333;">{note['text']}</span>
        </div>
    """, unsafe_allow_html=True)
