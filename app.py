import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

# Configuration de base robuste
st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE ÉLÉGANT ET LISIBLE ---
st.markdown("""
    <style>
    /* Fond blanc et typographie claire */
    .stApp { background-color: #ffffff; color: #1e1e1e; font-family: 'Segoe UI', sans-serif; }
    
    /* Centrage du logo */
    [data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }

    /* Titre HANNA */
    .hanna-main-title { 
        font-weight: 200; 
        letter-spacing: 8px; 
        text-transform: uppercase; 
        font-size: 32px; 
        text-align: center; 
        color: #000000;
        margin-top: 20px;
    }
    
    /* Sous-titre complet */
    .hanna-sub-title {
        font-weight: 300;
        font-size: 11px;
        text-align: center;
        color: #888888;
        letter-spacing: 1px;
        margin-bottom: 30px;
        text-transform: uppercase;
    }

    /* Champs de saisie */
    input { 
        background-color: #f0f2f6 !important; 
        color: #1e1e1e !important; 
        border: 1px solid #dcdfe6 !important; 
        text-align: center;
        height: 45px !important;
    }
    
    /* Bouton AUTHORIZE Standard et Propre */
    .stButton>button { 
        width: 100%; 
        background-color: #000000; 
        color: #ffffff; 
        border-radius: 4px; 
        border: none; 
        font-weight: bold; 
        height: 3em;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.write("")
    
    # Affichage du logo
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center;'>🛡️</h1>", unsafe_allow_html=True)

    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)
    
    pwd = st.text_input("Code d'accès", type="password", label_visibility="collapsed", placeholder="ENTER ACCESS CODE")
    
    if st.button("AUTHORIZE"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Code invalide.")
    st.stop()

# --- INTERFACE PRINCIPALE ---
st.markdown("## HANNA TERMINAL")
st.caption(f"Système Opérationnel | {datetime.now().strftime('%H:%M')}")

st.divider()

if 'notes' not in st.session_state:
    st.session_state.notes = []

new_note = st.text_input("Mémoriser une information :")
if st.button("Enregistrer"):
    if new_note:
        st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
        st.success("Donnée mémorisée.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

if st.button("🔒 Déconnexion"):
    st.session_state.auth = False
    st.rerun()
