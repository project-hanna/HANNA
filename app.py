import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE MICRO-DESIGN ABSOLU ---
st.markdown("""
    <style>
    /* Compression maximale du bloc central */
    .block-container { padding-top: 1rem !important; max-width: 280px !important; }
    .stApp { background-color: #ffffff; color: #333333; font-family: 'Inter', sans-serif; }
    
    /* Logo centré et discret */
    [data-testid="stImage"] { display: flex !important; justify-content: center !important; margin-bottom: -20px !important; }
    
    /* Titre HANNA : Minimalisme pur */
    .hanna-main-title { 
        font-weight: 100; 
        letter-spacing: 18px; 
        text-transform: uppercase; 
        font-size: 18px; 
        text-align: center; 
        color: #000000;
        margin-bottom: 0px;
    }
    
    /* Sous-titre invisible ou presque */
    .hanna-sub-title {
        font-weight: 300;
        font-size: 7px;
        text-align: center;
        color: #dddddd;
        letter-spacing: 0.5px;
        margin-bottom: 20px;
        text-transform: uppercase;
    }

    /* Champ de saisie : Ligne ultra-fine */
    div.stTextInput > div > div > input {
        text-align: center;
        border: 1px solid #f8f8f8 !important;
        border-bottom: 1px solid #eeeeee !important; /* Effet ligne */
        border-radius: 0px !important;
        height: 28px !important;
        font-size: 8px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        background-color: #ffffff !important;
        color: #000 !important;
    }
    
    /* Bouton AUTHORIZE : Micro-Typographie (Le plus petit possible) */
    .stButton > button {
        width: 100% !important;
        background-color: #000000 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 200 !important; 
        letter-spacing: 10px !important; /* Espacement extrême pour le chic */
        font-size: 6px !important; /* TAILLE ULTRA-MICRO */
        height: 24px !important; /* Hauteur minimaliste */
        border-radius: 0px !important;
        margin-top: -18px !important;
        text-transform: uppercase !important;
        transition: 0.5s;
        padding-left: 10px !important; /* Pour compenser l'espacement à droite */
    }
    .stButton > button:hover { background-color: #444444 !important; letter-spacing: 12px !important; }

    /* Masquage interface Streamlit */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, use_container_width=True)
        else:
            st.write("") # Espace si logo absent

    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)
    
    pwd = st.text_input("ACCESS CODE", type="password", label_visibility="collapsed", placeholder="CODE")
    
    if st.button("AUTHORIZE"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("DENIED")
    st.stop()

# --- INTERFACE PRINCIPALE ---
st.markdown('<div style="font-weight:100; letter-spacing:8px; font-size:14px; text-align:center;">HANNA</div>', unsafe_allow_html=True)
st.divider()

if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("ENTRY", expanded=True):
    new_note = st.text_input("Data:", key="main_input", placeholder="..." )
    if st.button("SYNC"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
            st.success("OK")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

if st.button("EXIT"):
    st.session_state.auth = False
    st.rerun()
