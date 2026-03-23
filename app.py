import streamlit as st
from datetime import datetime

# --- CONFIGURATION HANNA ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
# Lien direct vers votre logo sur GitHub (format raw pour l'affichage)
LOGO_URL = "https://raw.githubusercontent.com/project-hanna/HANNA/main/logo2.png"

# Configuration de la page
st.set_page_config(page_title="HANNA Terminal", layout="centered", page_icon=LOGO_URL)

# Style CSS pour l'ambiance Terminal
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; font-family: 'Courier New', monospace; }
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
    
    # Affichage du logo via l'URL GitHub
    st.image(LOGO_URL, width=150)
    st.title("🛡️ HANNA - Accès Restreint")
    
    pwd = st.text_input("Code d'accès :", type="password")
    
    if st.button("Authentification"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Code invalide.")
    st.stop()

# --- INTERFACE PRINCIPALE ---
st.image(LOGO_URL, width=60)
st.title("🛡️ HANNA Terminal")
st.caption(f"Système Opérationnel | {datetime.now().strftime('%H:%M')}")

st.divider()

# Gestionnaire de Notes
if 'notes' not in st.session_state:
    st.session_state.notes = []

new_note = st.text_input("Mémoriser une information :")
if st.button("Enregistrer"):
    if new_note:
        st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
        st.success("Donnée mémorisée.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.write(f"• {n}")

if st.button("🔒 Déconnexion"):
    st.session_state.auth = False
    st.rerun()
