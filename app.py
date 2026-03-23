import streamlit as st
from datetime import datetime
import base64
import os

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

# --- 2. GESTION DU LOGO ---
LOGO_FILE = "logo1.png"
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- 3. ARCHITECTURE CSS BDD8.5 (CENTRAGE ABSOLU & RIGIDE) ---
st.markdown(f"""
    <style>
    /* Neutralisation des marges Streamlit pour le centrage horizontal */
    .main .block-container {{
        max-width: 550px !important;
        padding: 4rem 1rem !important;
        margin: 0 auto !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: flex-start !important;
    }}

    /* Forcer l'alignement central de tous les composants injectés */
    [data-testid="stVerticalBlock"] {{
        align-items: center !important;
        width: 100% !important;
    }}

    /* Header HANNA - Alignement Géométrique */
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
        height: auto !important;
        margin-bottom: 25px !important;
        display: block !important;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        font-size: 52px;
        color: #000;
        text-transform: uppercase;
        margin: 0 !important;
        line-height: 1;
        
        /* Compensation mathématique du letter-spacing */
        letter-spacing: 14px; 
        margin-right: -14px !important; 
        
        display: block !important;
        width: 100% !important;
    }}

    .hanna-sub {{
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        font-size: 9px;
        color: #999;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-top: 15px !important;
        margin-right: -2.5px !important;
    }}

    /* Champ de Saisie */
    div.stTextInput {{ width: 100% !important; max-width: 480px !important; }}
    div.stTextInput input {{ 
        text-align: center !important; 
        border-radius: 12px !important; 
        border: 1px solid #EEE !important;
        height: 50px !important;
        background: #FDFDFD !important;
    }}

    /* UI Clean-up */
    #MainMenu, footer, header {{ visibility: hidden; display: none !important; }}
    </style>
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

# --- 5. RENDU INTERFACE ---
# En-tête centré
st.markdown(f"""
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# Zone de saisie
st.text_input("CAPTURE", 
              placeholder="Demandez à HANNA", 
              label_visibility="collapsed", 
              key="entry_input", 
              on_change=handle_capture)

st.write("<br>", unsafe_allow_html=True)

# Flux des captures
for note in st.session_state.notes:
    st.markdown(f"""
        <div style="padding: 15px; border-radius: 12px; background: #FAFAFA; border: 1px solid #F0F0F0; margin-bottom: 12px; width: 100%; text-align: left;">
            <small style="color: #007BFF; font-weight: 800; font-size: 11px;">{note['time']}</small><br>
            <span style="color: #222; font-size: 15px; font-family: 'Inter'; line-height: 1.5;">{note['text']}</span>
        </div>
    """, unsafe_allow_html=True)
