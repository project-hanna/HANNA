import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE ÉLÉGANT & CENTRAGE ABSOLU ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #333333; font-family: 'Inter', sans-serif; }
    
    /* Centrage horizontal du logo et du conteneur d'image */
    .stImage {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }
    .stImage > div {
        display: flex !important;
        justify-content: center !important;
    }
    
    /* Titre HANNA : Espacement large */
    .hanna-main-title { 
        font-weight: 200; 
        letter-spacing: 12px; 
        text-transform: uppercase; 
        font-size: clamp(24px, 5vw, 32px); 
        text-align: center; 
        color: #000000;
        margin-top: 20px;
        margin-bottom: 5px;
        width: 100%;
    }
    
    /* Sous-titre complet */
    .hanna-sub-title {
        font-weight: 300;
        font-size: clamp(10px, 3vw, 11px);
        text-align: center;
        color: #999999;
        letter-spacing: 1.5px;
        margin-bottom: 40px;
        text-transform: uppercase;
        width: 100%;
    }

    /* Input et Boutons centrés */
    div.stTextInput > div > div > input {
        text-align: center;
        border: 1px solid #eeeeee !important;
        border-radius: 4px !important;
        height: 45px;
    }
    
    .stButton > button {
        width: 100%;
        background-color: #000000;
        color: #ffffff;
        border: none;
        font-weight: 300;
        letter-spacing: 2px;
        height: 45px;
        border-radius: 4px;
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
    st.write("")
    st.write("")
    
    # Affichage du logo centré (Page 1)
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=160)
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
            st.error("Invalid credentials.")
    st.stop()

# --- INTERFACE PRINCIPALE (Page 2 - MISE EN PAGE IDENTIQUE) ---

# Rappel du Logo (Légèrement réduit pour plus d'espace de travail)
if os.path.exists(LOGO_FILE):
    st.image(LOGO_FILE, width=110)
else:
    st.markdown("<h1 style='text-align:center;'>🛡️</h1>", unsafe_allow_html=True)

# Rappel du Titre et Sous-titre
st.markdown('<div class="hanna-main-title" style="font-size:26px; letter-spacing:8px; margin-top:10px;">HANNA</div>', unsafe_allow_html=True)
st.markdown('<div class="hanna-sub-title" style="margin-bottom:20px;">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)

st.divider()

if 'notes' not in st.session_state:
    st.session_state.notes = []

# Section de capture de données
with st.expander("NEW DATA ENTRY", expanded=True):
    new_note = st.text_input("Capture:", key="main_input", placeholder="Type information here...")
    if st.button("SYNCHRONIZE"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
            st.success("Entry recorded.")

# Affichage des données
if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

st.write("")
# Bouton de sortie
if st.button("TERMINATE SESSION"):
    st.session_state.auth = False
    st.rerun()
