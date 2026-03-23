import streamlit as st
from datetime import datetime

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"

# Configuration ultra-simple
st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE MINIMALISTE ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; font-family: monospace; }
    h1 { color: #00ff41 !important; text-align: center; }
    .stTextInput>div>div>input { background-color: #1a1c24; color: #00ff41; border: 1px solid #00ff41; }
    .stButton>button { width: 100%; background-color: #00ff41; color: #0e1117; font-weight: bold; }
    </style>
    """, unsafe_allow_index=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.write("# 🛡️")
    st.title("HANNA - ACCÈS RESTREINT")
    
    pwd = st.text_input("Veuillez entrer le code d'accès :", type="password")
    
    if st.button("Authentification"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Code invalide.")
    st.stop()

# --- INTERFACE OPÉRATIONNELLE ---
st.title("🛡️ HANNA TERMINAL")
st.write("Système Opérationnel")

st.divider()

# Mémoire simple
if 'notes' not in st.session_state:
    st.session_state.notes = []

new_note = st.text_input("Mémoriser une information :")
if st.button("Enregistrer"):
    if new_note:
        st.session_state.notes.append(new_note)
        st.success("Enregistré.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.write(f"• {n}")

if st.button("Déconnexion"):
    st.session_state.auth = False
    st.rerun()
