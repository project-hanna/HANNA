import streamlit as st
from datetime import datetime
import os
import base64

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA", layout="centered")

# --- OPTIMISATION VITESSE : CACHE ---
@st.cache_data
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

def display_centered_logo(width_px=120):
    logo_data = get_base64_logo(LOGO_FILE)
    if logo_data:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; width: 100%; margin-top: 10px;">
                <img src="data:image/png;base64,{logo_data}" style="width: {width_px}px; height: auto;">
            </div>
            """,
            unsafe_allow_html=True
        )

# --- STYLE DESIGN ULTRA-ÉPURÉ ---
st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    .stApp { background-color: #ffffff; color: #1e1e1e; font-family: 'Inter', sans-serif; }
    
    .hanna-main-title { 
        font-weight: 200; 
        letter-spacing: 10px; 
        text-transform: uppercase; 
        font-size: 28px; 
        text-align: center; 
        color: #000000;
        margin-top: 10px;
        margin-bottom: 2px;
    }
    
    .hanna-sub-title {
        font-weight: 300;
        font-size: 10px;
        text-align: center;
        color: #999999;
        letter-spacing: 1.5px;
        margin-bottom: 25px;
        text-transform: uppercase;
    }

    div.stTextInput > div > div > input {
        text-align: center;
        background-color: #fcfcfc !important;
        border: 1px solid #f0f0f0 !important;
        border-radius: 8px !important;
        height: 45px !important;
    }

    .stButton > button {
        width: 100% !important;
        background-color: transparent !important;
        color: #ccc !important;
        border: 1px solid #eee !important;
        font-size: 10px !important;
        letter-spacing: 1px !important;
        height: 35px !important;
    }
    .stButton > button:hover { color: #000 !important; border-color: #000 !important; }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE DE SESSION ---
if "auth" not in st.session_state:
    st.session_state.auth = False
if 'notes' not in st.session_state:
    st.session_state.notes = []

# --- FONCTION DE CAPTURE (CALLBACK) ---
def handle_capture():
    val = st.session_state.input_note
    if val:
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.notes.append(f"[{timestamp}] {val}")
        # On vide le champ proprement
        st.session_state.input_note = ""

# --- PAGE DE CONNEXION ---
if not st.session_state.auth:
    st.write("")
    display_centered_logo(120)
    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)
    
    pwd = st.text_input("Code", type="password", label_visibility="collapsed", placeholder="CODE D'ACCÈS")
    if pwd:
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Accès refusé.")
    st.stop()

# --- PAGE PRINCIPALE ---
display_centered_logo(120)
st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)

st.divider()

# Utilisation du paramètre on_change pour valider sans bouton
st.text_input("CAPTURE", label_visibility="collapsed", placeholder="Demandez à HANNA", 
              key="input_note", on_change=handle_capture)

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

st.write("")
if st.button("QUITTER LA SESSION"):
    st.session_state.clear()
    st.rerun()
