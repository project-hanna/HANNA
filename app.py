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

# --- 3. ARCHITECTURE CSS (CENTRAGE ABSOLU) ---
st.markdown("""
    <style>
    /* 1. Neutraliser les conteneurs Streamlit pour le centrage */
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
        margin: auto;
    }
    
    /* 2. Style du Header */
    .hanna-header { 
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-bottom: 2.5rem;
    }
    
    .hanna-logo-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-bottom: 15px;
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
        /* IMPORTANT : Le letter-spacing ajoute de l'espace à DROITE de chaque lettre. 
           Pour centrer HANNA, on ajoute le même espace à GAUCHE du mot complet. */
        padding-left: 14px; 
        width: 100%;
    }
    
    .hanna-sub { 
        font-family: 'Inter', sans-serif;
        font-weight: 300; 
        font-size: 8px; 
        color: #999; 
        letter-spacing: 2px; 
        text-transform: uppercase;
        margin-top: 10px;
        width: 100%;
    }

    /* 3. Inputs & Boutons */
    div.stTextInput > div > div > input { text-align: center !important; border-radius: 8px; }
    .stButton > button { width: 100%; border-radius: 8px; color: #BBB; border: 1px solid #EEE; }

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

# --- 5. LOGIQUE ---
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
else:
    st.text_input("CAPTURE", placeholder="Demandez à HANNA", label_visibility="collapsed", key="entry_input", on_change=handle_capture)
    
    for note in st.session_state.notes:
        st.markdown(f"""
            <div style="padding: 12px; border-radius: 10px; background: #F9F9F9; border: 1px solid #EEE; margin-top: 10px; width: 100%;">
                <small style="color: #007BFF; font-weight: bold;">{note['time']}</small><br>{note['text']}
            </div>
        """, unsafe_allow_html=True)

    if st.button("QUITTER LA SESSION"):
        st.session_state.clear()
        st.rerun()
