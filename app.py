import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE ÉLITE COMPACT ---
st.markdown("""
    <style>
    /* Suppression totale des marges Streamlit */
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; max-width: 400px !important; }
    .stApp { background-color: #ffffff; color: #333333; font-family: 'Inter', sans-serif; }
    
    /* Logo centré */
    [data-testid="stImage"] { display: flex !important; justify-content: center !important; margin-bottom: -15px !important; }
    
    /* Titre HANNA : Minimaliste */
    .hanna-main-title { 
        font-weight: 200; 
        letter-spacing: 12px; 
        text-transform: uppercase; 
        font-size: 28px; 
        text-align: center; 
        color: #000000;
        margin-top: 0px;
        margin-bottom: 2px;
    }
    
    /* Sous-titre : Très fin */
    .hanna-sub-title {
        font-weight: 300;
        font-size: 10px;
        text-align: center;
        color: #aaaaaa;
        letter-spacing: 1.2px;
        margin-bottom: 25px;
        text-transform: uppercase;
    }

    /* Champ de saisie : Compact & Élégant */
    div.stTextInput > div > div > input {
        text-align: center;
        border: 1px solid #f0f0f0 !important;
        border-radius: 2px !important;
        height: 38px !important;
        font-size: 12px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase;
        background-color: #fafafa !important;
    }
    
    /* Bouton AUTHORIZE : Compact */
    .stButton > button {
        width: 100%;
        background-color: #000000;
        color: #ffffff;
        border: none;
        font-weight: 300;
        letter-spacing: 3px;
        font-size: 11px !important;
        height: 38px !important;
        border-radius: 2px;
        margin-top: -10px;
        text-transform: uppercase;
    }
    .stButton > button:hover { background-color: #222222; color: #ffffff; }

    /* Masquage interface Streamlit */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # Logo réduit (50% de la largeur du bloc central)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center;'>🛡️</h1>", unsafe_allow_html=True)

    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)
    
    # Champ de texte compact
    pwd = st.text_input("ACCESS CODE", type="password", label_visibility="collapsed", placeholder="ENTER ACCESS CODE")
    
    # Bouton compact
    if st.button("AUTHORIZE"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("ACCESS DENIED")
    st.stop()

# --- INTERFACE PRINCIPALE ---
st.markdown('<div style="font-weight:200; letter-spacing:5px; font-size:18px;">HANNA</div>', unsafe_allow_html=True)
st.caption(f"System Ready | {datetime.now().strftime('%H:%M')}")
st.divider()

if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("NEW DATA ENTRY", expanded=True):
    new_note = st.text_input("Capture:", key="main_input", placeholder="...")
    if st.button("SYNCHRONIZE"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
            st.success("Synchronized.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

if st.button("TERMINATE SESSION"):
    st.session_state.auth = False
    st.rerun()
