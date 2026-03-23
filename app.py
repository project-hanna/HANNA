import streamlit as st
from datetime import datetime

# --- CONFIGURATION HANNA ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_URL = "https://img.icons8.com/fluency/96/shield-with-keyhole.png"

st.set_page_config(page_title="HANNA Terminal", page_icon=LOGO_URL)

# --- VÉRIFICATION D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.image(LOGO_URL, width=80)
    st.title("🛡️ HANNA - Accès Restreint")
    
    pwd_input = st.text_input("Code d'accès :", type="password")
    if st.button("Authentification"):
        if pwd_input == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Code incorrect.")
    st.stop() # Arrête l'affichage ici si pas connecté

# --- INTERFACE SI CONNECTÉ ---
st.title("🛡️ HANNA Terminal - Opérationnel")
st.caption(f"Connecté | {datetime.now().strftime('%H:%M')}")

st.divider()

# Gestionnaire de Notes
if 'notes' not in st.session_state:
    st.session_state.notes = []

new_note = st.text_input("Ajouter à la mémoire :")
if st.button("Mémoriser"):
    if new_note:
        st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
        st.success("Donnée enregistrée.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.write(f"• {n}")

if st.button("🔒 Déconnexion"):
    st.session_state.auth = False
    st.rerun()
