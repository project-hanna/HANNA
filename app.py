import streamlit as st
from datetime import datetime

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"

# Configuration de base
st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE CORRIGÉ (unsafe_allow_html=True) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; font-family: monospace; }
    h1 { color: #00ff41 !important; text-align: center; }
    input { background-color: #1a1c24 !important; color: #00ff41 !important; border: 1px solid #00ff41 !important; }
    .stButton>button { width: 100%; background-color: #00ff41; color: #0e1117; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True) # <-- CORRECTION ICI

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
st.write(f"Système Opérationnel | {datetime.now().strftime('%H:%M')}")

st.divider()

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
