import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

# Configuration de base
st.set_page_config(page_title="HANNA Terminal", layout="centered")

# --- STYLE LIGHT MODE CORRIGÉ ---
st.markdown("""
    <style>
    /* Fond blanc pour l'application */
    .stApp { background-color: #ffffff; color: #1e1e1e; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Titres en noir pour lisibilité sur blanc */
    h1, h2, h3 { color: #1e1e1e !important; text-align: center; font-weight: 600; }
    
    /* Champs de saisie adaptés au fond blanc */
    input { background-color: #f0f2f6 !important; color: #1e1e1e !important; border: 1px solid #dcdfe6 !important; }
    
    /* Bouton d'action */
    .stButton>button { width: 100%; background-color: #1e1e1e; color: #ffffff; border-radius: 8px; border: none; font-weight: bold; height: 3em; }
    .stButton>button:hover { background-color: #333333; color: #ffffff; }
    
    /* Centrage du logo */
    .stImage { display: flex; justify-content: center; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.write("")
    st.write("")
    
    # Affichage sécurisé du logo2.png
    if os.path.exists(LOGO_FILE):
        try:
            st.image(LOGO_FILE, width=180)
        except:
            st.markdown("<h1 style='font-size: 60px;'>🛡️</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='font-size: 60px;'>🛡️</h1>", unsafe_allow_html=True)
        st.caption("<p style='text-align: center; color: #666;'>Logo2.png introuvable</p>", unsafe_allow_html=True)

    st.title("HANNA")
    st.subheader("Authentification Requise")
    
    pwd = st.text_input("Code d'accès :", type="password")
    
    if st.button("Se connecter"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Code invalide.")
    st.stop()

# --- INTERFACE PRINCIPALE (DÉVERROUILLÉE) ---
col_l, col_r = st.columns([0.2, 0.8])
with col_l:
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=60)
with col_r:
    st.title("HANNA TERMINAL")
    st.caption(f"Connecté | {datetime.now().strftime('%H:%M')}")

st.divider()

# Gestionnaire de Mémoire
if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("📝 Enregistrer une nouvelle donnée", expanded=True):
    new_note = st.text_input("Information :", key="main_input")
    if st.button("Enregistrer dans la mémoire"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
            st.success("Donnée mémorisée.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

st.write("")
if st.button("🔒 Déconnexion"):
    st.session_state.auth = False
    st.rerun()
