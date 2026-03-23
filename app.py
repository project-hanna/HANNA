import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE HANNA ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"

# Détection du logo local
LOGO_PATH = "logo.png"
if not os.path.exists(LOGO_PATH):
    # Image de secours si le fichier n'est pas trouvé
    LOGO_PATH = "https://img.icons8.com/fluency/96/shield-with-keyhole.png"

st.set_page_config(page_title="HANNA Terminal", layout="wide", page_icon=LOGO_URL if 'http' in str(LOGO_PATH) else None)

# Style CSS
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #1a1c24; color: #00ff41; border: 1px solid #00ff41; }
    .stButton>button { width: 100%; background-color: #00ff41; color: #0e1117; border: none; font-weight: bold; }
    h1, h2, h3 { color: #00ff41 !important; }
    </style>
    """, unsafe_allow_index=True)

# --- VÉRIFICATION D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        # Affichage de VOTRE logo
        st.image(LOGO_PATH, width=150)
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
st.image(LOGO_PATH, width=60)
st.title("🛡️ HANNA Terminal")
st.caption(f"Système Sécurisé | {datetime.now().strftime('%H:%M')}")

st.divider()

# Gestionnaire de Mémoire
if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("📝 Ajouter à la mémoire", expanded=True):
    new_note = st.text_input("Saisir la donnée :")
    if st.button("Enregistrer"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
            st.success("Mémorisé.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.write(f"• {n}")

if st.button("🔒 Déconnexion"):
    st.session_state.auth = False
    st.rerun()
