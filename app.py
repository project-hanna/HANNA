import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo.png"

st.set_page_config(page_title="HANNA Terminal", layout="wide")

# Style CSS pour le look Terminal
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #1a1c24; color: #00ff41; border: 1px solid #00ff41; }
    .stButton>button { width: 100%; background-color: #00ff41; color: #0e1117; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_index=True)

# --- VÉRIFICATION D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        # Méthode d'affichage sécurisée : On vérifie l'existence ET la taille
        if os.path.exists(LOGO_FILE) and os.path.getsize(LOGO_FILE) > 0:
            try:
                st.image(LOGO_FILE, width=150)
            except Exception:
                st.title("🛡️ HANNA") # Secours si l'image est corrompue
        else:
            st.title("🛡️ HANNA")
            st.caption("Système en attente du logo...")

        st.subheader("Accès Restreint")
        pwd = st.text_input("Code d'accès :", type="password", key="login_pwd")
        
        if st.button("Authentification"):
            if pwd == PASSWORD_SYSTEM:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("❌ Code invalide.")
    st.stop()

# --- INTERFACE PRINCIPALE ---
st.title("🛡️ HANNA Terminal - Opérationnel")
st.caption(f"Système Sécurisé | {datetime.now().strftime('%H:%M')}")
st.divider()

# Gestionnaire de Notes
if 'notes' not in st.session_state:
    st.session_state.notes = []

new_note = st.text_input("Mémoriser :", key="note_input")
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
