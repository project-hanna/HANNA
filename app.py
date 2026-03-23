import streamlit as st
from datetime import datetime
import os
import base64

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

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
            f"""<div style="display: flex; justify-content: center; align-items: center; width: 100%; margin-top: 10px; animation: fadeIn 0.8s;">
                <img src="data:image/png;base64,{logo_data}" style="width: {width_px}px; height: auto;">
            </div>""", unsafe_allow_html=True
        )

# --- STYLE DESIGN : BOUTON DANS LE CHAMP ---
st.markdown("""
    <style>
    @keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; max-width: 500px !important; }
    .stApp { background-color: #ffffff; color: #1e1e1e; font-family: 'Inter', sans-serif; }
    
    /* Titres */
    .hanna-main-title { font-weight: 200; letter-spacing: 12px; text-transform: uppercase; font-size: 30px; text-align: center; color: #000; margin-top: 15px; margin-bottom: 5px; animation: fadeIn 1s; }
    .hanna-sub-title { font-weight: 300; font-size: 10px; text-align: center; color: #aaa; letter-spacing: 2px; margin-bottom: 30px; text-transform: uppercase; animation: fadeIn 1.2s; }

    /* Masquer l'icône SHOW PASSWORD d'origine */
    button[aria-label="Show password"] { display: none !important; }

    /* Conteneur de l'input pour positionnement relatif */
    div[data-testid="stTextInput"] { position: relative; width: 100%; }

    /* Design du champ de saisie */
    div.stTextInput > div > div > input {
        text-align: left;
        padding-left: 20px !important;
        padding-right: 90px !important; /* Espace réservé pour le bouton */
        background-color: #fafafa !important;
        border: 1px solid #eeeeee !important;
        border-radius: 8px !important;
        height: 50px !important;
    }

    /* POSITIONNEMENT DU BOUTON ENTRER À LA PLACE DE L'OEIL */
    /* Le bouton Streamlit est normalement en dessous, on le remonte par-dessus l'input */
    .stButton > button {
        position: absolute;
        right: 5px;
        top: -45px; /* Ajustement vertical précis */
        width: 80px !important;
        height: 40px !important;
        background-color: #000000 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 400 !important;
        font-size: 11px !important;
        letter-spacing: 1px !important;
        z-index: 1000;
        transition: all 0.3s ease;
    }
    .stButton > button:hover { background-color: #333333 !important; }

    /* Nettoyage UI */
    #MainMenu, footer, header { visibility: hidden; }
    .stDeployButton { display:none; }
    </style>
    """, unsafe_allow_html=True)

def draw_header():
    display_centered_logo(120)
    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)

# --- LOGIQUE DE SESSION ---
if "auth" not in st.session_state:
    st.session_state.auth = False
if 'notes' not in st.session_state:
    st.session_state.notes = []

# --- PAGE DE CONNEXION ---
if not st.session_state.auth:
    st.write("")
    draw_header()
    
    pwd = st.text_input("CODE", type="password", label_visibility="collapsed", placeholder="CODE D'ACCÈS")
    # Ce bouton va se loger visuellement DANS l'input au-dessus de lui
    if st.button("ENTRER", key="login_btn"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Accès refusé.")
    st.stop()

# --- PAGE PRINCIPALE ---
draw_header()
st.divider()

new_note = st.text_input("CAPTURE", label_visibility="collapsed", placeholder="Demandez à HANNA")

# Même logique de bouton intégré pour la capture
if st.button("ENTRER", key="sync_btn"):
    if new_note:
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.notes.append(f"[{timestamp}] {new_note}")
        st.rerun()

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.markdown(f"""<div style="padding:12px; background:#f9f9f9; border-radius:8px; margin-bottom:8px; 
                    border-left:3px solid #000; font-size:14px; animation: fadeIn 0.5s;">{n}</div>""", 
                    unsafe_allow_html=True)

st.write("")
if st.button("QUITTER LA SESSION"):
    st.session_state.clear()
    st.rerun()
