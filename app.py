import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE ULTRA-COMPACT & RAFFINÉ ---
st.markdown("""
    <style>
    /* Nettoyage des marges Streamlit */
    .block-container { padding-top: 1.5rem !important; max-width: 350px !important; }
    .stApp { background-color: #ffffff; color: #333333; font-family: 'Inter', sans-serif; }
    
    /* Logo centré et discret */
    [data-testid="stImage"] { display: flex !important; justify-content: center !important; margin-bottom: -10px !important; }
    
    /* Titre HANNA : Épuré */
    .hanna-main-title { 
        font-weight: 200; 
        letter-spacing: 14px; 
        text-transform: uppercase; 
        font-size: 24px; 
        text-align: center; 
        color: #000000;
        margin-bottom: 2px;
    }
    
    /* Sous-titre : Micro-typographie */
    .hanna-sub-title {
        font-weight: 300;
        font-size: 9px;
        text-align: center;
        color: #bbbbbb;
        letter-spacing: 1px;
        margin-bottom: 25px;
        text-transform: uppercase;
    }

    /* Champ de saisie : Finition "Soft" */
    div.stTextInput > div > div > input {
        text-align: center;
        border: 1px solid #f2f2f2 !important;
        border-radius: 2px !important;
        height: 35px !important;
        font-size: 10px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase;
        background-color: #fafafa !important;
        color: #000 !important;
    }
    
    /* Bouton AUTHORIZE : Petit, Fin et Élégant */
    .stButton > button {
        width: 100%;
        background-color: #000000;
        color: #ffffff;
        border: none;
        font-weight: 200; /* Plus fin */
        letter-spacing: 4px; /* Plus d'espace entre les lettres */
        font-size: 9px !important; /* Taille très réduite */
        height: 32px !important; /* Plus fin en hauteur */
        border-radius: 2px;
        margin-top: -12px;
        text-transform: uppercase;
        transition: 0.4s;
    }
    .stButton > button:hover { background-color: #444444; color: #ffffff; }

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
            st.markdown("<h1 style='text-align:center;'>🛡️</h1>", unsafe_allow_html=True)

    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)
    
    pwd = st.text_input("ACCESS CODE", type="password", label_visibility="collapsed", placeholder="ENTER ACCESS CODE")
    
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
    new_note = st.text_input("Capture:", key="main_input", placeholder="..." )
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
