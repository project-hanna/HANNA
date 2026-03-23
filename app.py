import streamlit as st
from datetime import datetime

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo.png"

st.set_page_config(page_title="HANNA Terminal", layout="wide")

# --- VÉRIFICATION D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        # Tentative d'affichage du logo sans faire planter l'app
        try:
            st.image(LOGO_FILE, width=150)
        except:
            st.warning("⚠️ Logo personnalisé introuvable sur GitHub (Vérifiez le nom logo.png)")
            st.title("🛡️ HANNA")
        
        st.subheader("Accès Restreint")
        pwd = st.text_input("Code d'accès :", type="password")
        if st.button("Authentification"):
            if pwd == PASSWORD_SYSTEM:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("❌ Code invalide.")
    st.stop()

# --- INTERFACE PRINCIPALE (DÉVERROUILLÉE) ---
try:
    st.image(LOGO_FILE, width=60)
except:
    pass

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
