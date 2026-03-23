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

# --- 2. ARCHITECTURE CSS (CENTRAGE TOTAL & MINIMALISME) ---
st.markdown(f"""
    <style>
    /* Centrage structurel profond */
    .stMainBlockContainer {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }}
    
    .block-container {{
        max-width: 500px !important;
        padding-top: 3rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    /* Header & Logo */
    .hanna-header {{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-bottom: 3rem;
    }}

    .hanna-logo {{
        width: 115px;
        height: auto;
        margin-bottom: 20px;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        letter-spacing: 12px;
        font-size: 42px;
        color: #1A1A1A;
        margin: 0;
        padding-left: 12px;
    }}

    .hanna-sub {{
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        font-size: 9px;
        color: #AAA;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 10px;
    }}

    /* Zone de Capture */
    div[data-baseweb="input"] {{ 
        border-radius: 14px !important; 
        width: 100% !important;
        background-color: #FDFDFD !important;
        border: 1px solid #EEE !important;
    }}
    input {{ text-align: center !important; font-size: 16px !important; color: #333 !important; }}
    
    /* Masquer les éléments natifs Streamlit */
    #MainMenu, footer, header {{ visibility: hidden; height: 0; }}
    .stDeployButton {{ display:none; }}
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

# --- 4. LOGIQUE DE CAPTURE ---
if 'notes' not in st.session_state: 
    st.session_state.notes = []

def handle_capture():
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        # Insertion en haut de liste
        st.session_state.notes.insert(0, {"time": ts, "text": entry})
        st.session_state.entry_input = "" 

# Champ de saisie unique
st.text_input("CAPTURE", placeholder="Capturer l'instant...", 
              label_visibility="collapsed", key="entry_input", on_change=handle_capture)

st.write("<br>", unsafe_allow_html=True)

# Affichage du flux (Feed)
for note in st.session_state.notes:
    st.markdown(f"""
        <div style="padding: 15px; border-radius: 12px; background: #FFFFFF; border: 1px solid #F2F2F2; margin-bottom: 12px; width: 100%; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
            <span style="color: #007BFF; font-weight: 600; font-size: 11px; font-family: 'Inter';">{note['time']}</span>
            <span style="color: #444; font-size: 14px; margin-left: 12px; font-family: 'Inter'; line-height: 1.4;">{note['text']}</span>
        </div>
    """, unsafe_allow_html=True)
