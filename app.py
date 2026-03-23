import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo3.png"

# Configuration de base
st.set_page_config(page_title="HANNA Terminal", layout="centered")

# --- STYLE TERMINAL CORRIGÉ ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #00ff41 !important; text-align: center; }
    input { background-color: #1a1c24 !important; color: #00ff41 !important; border: 1px solid #00ff41 !important; }
    .stButton>button { width: 100%; background-color: #00ff41; color: #0e1117; font-weight: bold; border: none; }
    .logo-container { display: flex; justify-content: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.write("")
    
    # Affichage sécurisé du logo3.png
    if os.path.exists(LOGO_FILE):
        try:
            st.image(LOGO_FILE, width=180)
        except:
            st.markdown("<h1 style='font-size: 60px;'>🛡️</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='font-size: 60px;'>🛡️</h1>", unsafe_allow_html=True)
        st.caption("<p style='text-align: center;'>En attente de logo3.png...</p>", unsafe_allow_html=True)

    st.title("HANNA - ACCÈS RESTREINT")
    
    pwd = st.text_input("Veuillez entrer le code d'autorisation :", type="password")
    
    if st.button("Authentification"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Code invalide.")
    st.stop()

# --- INTERFACE OPÉRATIONNELLE ---
# Petit rappel du logo en haut du terminal
if os.path.exists(LOGO_FILE):
    try:
        st.image(LOGO_FILE, width=60)
    except:
        st.write("🛡️")

st.title("HANNA TERMINAL")
st.caption(f"Système Opérationnel | {datetime.now().strftime('%H:%M')}")

st.divider()

# Gestionnaire de Mémoire
if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("📝 Mémoriser une donnée", expanded=True):
    new_note = st.text_input("Saisir l'information :", key="main_input")
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
