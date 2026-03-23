import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE DESIGN BLANC & COMPACT ---
st.markdown("""
    <style>
    /* Suppression de l'espace blanc en haut */
    .block-container { padding-top: 1rem !important; }
    
    /* Fond blanc pur et texte sombre */
    .stApp { background-color: #ffffff; color: #1e1e1e; font-family: 'Inter', 'Segoe UI', sans-serif; }
    
    /* Centrage parfait du logo */
    [data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }

    /* Titre HANNA : Élégant et aéré */
    .hanna-main-title { 
        font-weight: 200; 
        letter-spacing: 10px; 
        text-transform: uppercase; 
        font-size: 30px; 
        text-align: center; 
        color: #000000;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    
    /* Sous-titre complet */
    .hanna-sub-title {
        font-weight: 300;
        font-size: 10px;
        text-align: center;
        color: #999999;
        letter-spacing: 1px;
        margin-bottom: 30px;
        text-transform: uppercase;
    }

    /* Champ de saisie stylisé */
    div.stTextInput > div > div > input {
        text-align: center;
        background-color: #f8f9fa !important;
        border: 1px solid #eeeeee !important;
        border-radius: 4px !important;
        height: 45px !important;
        color: #000 !important;
    }
    
    /* Bouton ENTRER : Noir, sobre et élégant */
    .stButton > button {
        width: 100% !important;
        background-color: #000000 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 400 !important;
        letter-spacing: 3px !important;
        height: 45px !important;
        border-radius: 4px !important;
        text-transform: uppercase !important;
        transition: 0.3s;
    }
    .stButton > button:hover { background-color: #333333 !important; }

    /* Masquage des éléments Streamlit par défaut */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # Espacement minimal avant le logo
    st.write("")
    
    # Affichage du logo centré
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center;'>🛡️</h1>", unsafe_allow_html=True)

    # Nouveaux titres configurés
    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)
    
    # Champ de code d'accès
    pwd = st.text_input("Code", type="password", label_visibility="collapsed", placeholder="CODE D'ACCÈS")
    
    if st.button("ENTRER"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Accès refusé.")
    st.stop()

# --- INTERFACE PRINCIPALE (APRÈS CONNEXION) ---
st.markdown('<div class="hanna-main-title" style="text-align:left; font-size:22px; letter-spacing:4px;">HANNA</div>', unsafe_allow_html=True)
st.caption(f"Système Opérationnel | {datetime.now().strftime('%H:%M')}")

st.divider()

if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("NOUVELLE ENTRÉE", expanded=True):
    new_note = st.text_input("Donnée :", key="main_input", placeholder="Saisir ici...")
    if st.button("SYNCHRONISER"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
            st.success("Mémorisé.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

if st.button("QUITTER LA SESSION"):
    st.session_state.auth = False
    st.rerun()
