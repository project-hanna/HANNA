import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION & SÉCURITÉ ---
# Optimisation : Utiliser st.secrets pour le mot de passe en production
PASSWORD_SYSTEM = st.secrets.get("PASSWORD", "mtt.mallee@gmail.C94")
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

@st.cache_data(show_spinner=False)
def get_base64_logo(file_path):
    """Mise en cache optimisée du logo."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- CSS ARCHITECTURE BDD7.1 (ULTRA-CLEAN) ---
# Optimisation : Regroupement des styles et suppression du surplus
st.markdown(f"""
    <style>
    /* Reset & Container */
    .block-container {{ padding-top: 2rem; max-width: 500px; }}
    .stApp {{ background-color: #FFFFFF; }}
    
    /* Typography Premium */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400&display=swap');
    
    .hanna-header {{ text-align: center; margin-bottom: 2rem; pointer-events: none; }}
    .hanna-logo {{ width: 100px; filter: grayscale(100%); opacity: 0.9; transition: 0.5s; }}
    
    .hanna-title {{ 
        font-family: 'Inter', sans-serif;
        font-weight: 200; 
        letter-spacing: 12px; 
        font-size: clamp(30px, 10vw, 52px); 
        color: #000; 
        margin: 10px 0 0 0;
        line-height: 1;
    }}
    
    .hanna-sub {{ 
        font-family: 'Inter', sans-serif;
        font-weight: 300; 
        font-size: 9px; 
        color: #AAA; 
        letter-spacing: 1.5px; 
        text-transform: uppercase;
        margin-top: 8px;
    }}

    /* Inputs & UI Components */
    div[data-baseweb="input"] {{ border-radius: 12px !important; background: #F8F9FA !important; border: 1px solid #F0F0F0 !important; }}
    input {{ text-align: center !important; font-family: 'Inter', sans-serif !important; }}
    
    /* Bouton Quitter Discret */
    .stButton > button {{ 
        width: 100%; border-radius: 8px; border: 1px solid #F0F0F0; 
        background: white; color: #BBB; font-size: 11px; transition: 0.2s;
    }}
    .stButton > button:hover {{ color: #000; border-color: #000; background: #FAFAFA; }}

    /* Masquage des éléments natifs Streamlit */
    #MainMenu, footer, header {{ visibility: hidden; height: 0; }}
    </style>
    
    <div class="hanna-header">
        {"<img src='data:image/png;base64," + LOGO_B64 + "' class='hanna-logo'>" if LOGO_B64 else ""}
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# --- GESTION DE L'ÉTAT (SESSION STATE) ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'notes' not in st.session_state: st.session_state.notes = []

# --- LOGIQUE MÉTIER ---
def handle_capture():
    """Traitement de l'entrée utilisateur avec nettoyage."""
    entry = st.session_state.get('entry_input', '').strip()
    if entry:
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.insert(0, f"**{ts}** • {entry}") # Insert au début pour éviter le reversed()
        st.session_state.entry_input = "" 

# --- ROUTAGE DES PAGES ---
if not st.session_state.auth:
    # Zone de Connexion
    with st.container():
        pwd = st.text_input("ACCÈS", type="password", placeholder="PASSWORD", label_visibility="collapsed")
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        elif pwd:
            st.caption("Identifiant invalide.")
else:
    # Interface de Capture
    st.text_input("CAPTURE", 
                  placeholder="Échanger avec HANNA...", 
                  label_visibility="collapsed",
                  key="entry_input", 
                  on_change=handle_capture)

    # Affichage des flux (Optimisé)
    for note in st.session_state.notes:
        st.markdown(f"""
            <div style="padding: 12px; border-radius: 10px; background: #FBFBFB; 
            border-left: 2px solid #EEE; margin-bottom: 8px; font-size: 14px; color: #333;">
                {note}
            </div>
        """, unsafe_allow_html=True)

    # Footer Action
    st.write("<br>" * 2, unsafe_allow_html=True)
    if st.button("TERMINER LA SESSION"):
        st.session_state.clear()
        st.rerun()
