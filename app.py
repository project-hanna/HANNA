import streamlit st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE MICRO-TYPOGRAPHIE ---
st.markdown("""
    <style>
    /* Suppression des marges pour un bloc compact */
    .block-container { padding-top: 1.5rem !important; max-width: 320px !important; }
    .stApp { background-color: #ffffff; color: #333333; font-family: 'Inter', sans-serif; }
    
    /* Logo centré */
    [data-testid="stImage"] { display: flex !important; justify-content: center !important; margin-bottom: -15px !important; }
    
    /* Titre HANNA */
    .hanna-main-title { 
        font-weight: 100; 
        letter-spacing: 16px; 
        text-transform: uppercase; 
        font-size: 20px; 
        text-align: center; 
        color: #000000;
        margin-bottom: 2px;
    }
    
    /* Sous-titre micro */
    .hanna-sub-title {
        font-weight: 300;
        font-size: 8px;
        text-align: center;
        color: #cccccc;
        letter-spacing: 0.8px;
        margin-bottom: 25px;
        text-transform: uppercase;
    }

    /* Champ de saisie : Très fin */
    div.stTextInput > div > div > input {
        text-align: center;
        border: 1px solid #f5f5f5 !important;
        border-radius: 0px !important;
        height: 30px !important;
        font-size: 9px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase;
        background-color: #ffffff !important;
    }
    
    /* Bouton AUTHORIZE : Le plus fin possible */
    .stButton > button {
        width: 100% !important;
        background-color: #000000 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 200 !important; 
        letter-spacing: 6px !important; /* Espacement extrême pour l'élégance */
        font-size: 7.5px !important; /* Taille minuscule pour le chic */
        height: 28px !important; /* Hauteur très fine */
        border-radius: 0px !important;
        margin-top: -15px !important;
        text-transform: uppercase !important;
        transition: 0.5s;
    }
    .stButton > button:hover { background-color: #555555 !important; }

    /* Masquage interface Streamlit */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 1.1, 1])
    with col2:
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center;'>🛡️</h1>", unsafe_allow_html=True)

    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)
    
    pwd = st.text_input("ACCESS CODE", type="password", label_visibility="collapsed", placeholder="ENTER CODE")
    
    if st.button("AUTHORIZE"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("DENIED")
    st.stop()

# --- INTERFACE PRINCIPALE ---
st.markdown('<div style="font-weight:100; letter-spacing:5px; font-size:16px;">HANNA</div>', unsafe_allow_html=True)
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
