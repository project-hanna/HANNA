import streamlit as st
from datetime import datetime

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"

# Configuration de base robuste
st.set_page_config(page_title="HANNA Terminal", layout="centered")

# Style CSS minimaliste pour éviter les conflits
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; font-family: monospace; }
    .stTextInput>div>div>input { background-color: #1a1c24; color: #00ff41; border: 1px solid #00ff41; }
    .stButton>button { width: 100%; background-color: #00ff41; color: #0e1117; border: none; font-weight: bold; }
    h1, h2, h3 { color: #00ff41 !important; text-align: center; }
    </style>
    """, unsafe_allow_index=True)

# --- VÉRIFICATION D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.write("")
    st.write("")
    # Logo textuel sécurisé
    st.markdown("<h1 style='font-size: 60px;'>🛡️</h1>", unsafe_allow_index=True)
    st.title("HANNA - ACCÈS RESTREINT")
    st.caption("<p style='text-align: center;'>Système de Navigation Adaptatif Hybride</p>", unsafe_allow_index=True)
    
    st.divider()
    
    pwd = st.text_input("Code d'autorisation :", type="password", key="login_pass")
    
    if st.button("Authentification"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Code invalide.")
    st.stop()

# --- INTERFACE PRINCIPALE (OPÉRATIONNELLE) ---
st.markdown("### 🛡️ HANNA Terminal")
st.caption(f"Connecté | Mode Sécurisé | {datetime.now().strftime('%H:%M')}")

st.divider()

# Gestionnaire de Mémoire simple
if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("📝 Enregistrer une donnée", expanded=True):
    new_note = st.text_input("Saisir l'information :", key="note_input")
