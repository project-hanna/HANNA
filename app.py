import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE DESIGN BLANC & COMPACT (GLOBAL) ---
st.markdown("""
    <style>
    /* Suppression de l'espace blanc en haut de page */
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    
    /* Fond blanc pur et texte sombre */
    .stApp { background-color: #ffffff; color: #1e1e1e; font-family: 'Inter', 'Segoe UI', sans-serif; }
    
    /* Centrage du logo */
    [data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }

    /* Titre HANNA : Élégant */
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
    
    /* Sous-titre / Status */
    .hanna-sub-title {
        font-weight: 300;
        font-size: 9px;
        text-align: center;
        color: #999999;
        letter-spacing: 1.5px;
        margin-bottom: 25px;
        text-transform: uppercase;
    }

    /* Champ de saisie stylisé */
    div.stTextInput > div > div > input {
        text-align: center;
        background-color: #fcfcfc !important;
        border: 1px solid #f0f0f0 !important;
        border-radius: 4px !important;
        height: 40px !important;
        color: #000 !important;
        font-size: 14px !important;
    }
    
    /* Boutons Noirs : ENTRER, SYNCHRONISER, QUITTER */
    .stButton > button {
        width: 100% !important;
        background-color: #000000 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 400 !important;
        letter-spacing: 2px !important;
        height: 40px !important;
        border-radius: 4px !important;
        text-transform: uppercase !important;
        font-size: 12px !important;
        transition: 0.3s;
    }
    .stButton > button:hover { background-color: #333333 !important; }

    /* Style des notes mémorisées (Stinfo) */
    .stAlert {
        background-color: #f8f9fa !important;
        color: #333 !important;
        border: none !important;
        border-left: 2px solid #000 !important;
        font-size: 13px !important;
    }

    /* Masquage des éléments Streamlit par défaut */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # --- PAGE D'ACCUEIL ---
    st.write("")
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center;'>🛡️</h1>", unsafe_allow_html=True)

    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)
    
    pwd = st.text_input("Code", type="password", label_visibility="collapsed", placeholder="CODE D'ACCÈS")
    
    if st.button("ENTRER"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Accès refusé.")
    st.stop()

# --- INTERFACE PRINCIPALE (APRÈS CONNEXION) ---
# En-tête compacte
col_logo, col_text = st.columns([0.2, 0.8])
with col_logo:
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=50)

st.markdown('<div class="hanna-main-title" style="text-align:left; font-size:22px; letter-spacing:4px; margin-top:0px;">HANNA</div>', unsafe_allow_html=True)
st.markdown(f'<div class="hanna-sub-title" style="text-align:left; margin-bottom:10px;">RÉSEAU OPÉRATIONNEL | {datetime.now().strftime("%H:%M")}</div>', unsafe_allow_html=True)

st.divider()

# Gestion de la mémoire
if 'notes' not in st.session_state:
    st.session_state.notes = []

# Section d'entrée
with st.container():
    new_note = st.text_input("CAPTURE DE DONNÉE :", label_visibility="collapsed", placeholder="Saisir une information à mémoriser...")
    if st.button("SYNCHRONISER"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
            st.rerun() # Rafraîchir pour afficher la note immédiatement

# Affichage des notes
if st.session_state.notes:
    st.write("")
    for n in reversed(st.session_state.notes):
        st.info(n)

st.write("")
st.write("")
# Bouton de sortie
if st.button("QUITTER LA SESSION"):
    st.session_state.auth = False
    st.rerun()
