import streamlit as st
from datetime import datetime

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"

st.set_page_config(page_title="HANNA Terminal", layout="wide")

# Style CSS pour un logo textuel "Cyber"
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; font-family: 'Courier New', monospace; }
    .cyber-logo { 
        font-size: 50px; 
        font-weight: bold; 
        text-align: center; 
        text-shadow: 2px 2px #ff0000, -2px -2px #0000ff;
        margin-bottom: 10px;
    }
    .stTextInput>div>div>input { background-color: #1a1c24; color: #00ff41; border: 1px solid #00ff41; }
    .stButton>button { width: 100%; background-color: #00ff41; color: #0e1117; border: none; font-weight: bold; }
    h1, h2, h3 { color: #00ff41 !important; text-align: center; }
    </style>
    """, unsafe_allow_index=True)

# --- VÉRIFICATION D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    col1, col_center, col3 = st.columns([1, 1.5, 1])
    with col_center:
        st.write("")
        st.write("")
        # LOGO TEXTUEL (Remplace l'image qui pose problème)
        st.markdown('<div class="cyber-logo">🛡️ HANNA</div>', unsafe_allow_index=True)
        st.caption("<p style='text-align: center;'>Hybrid Adaptive Navigator & Network Assistant</p>", unsafe_allow_index=True)
        
        st.divider()
        
        pwd = st.text_input("Code d'autorisation :", type="password", key="login_pass")
        
        if st.button("Authentification"):
            if pwd == PASSWORD_SYSTEM:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("❌ Code invalide.")
    st.stop()

# --- INTERFACE PRINCIPALE (DÉVERROUILLÉE) ---
st.markdown('<div style="color: #00ff41; font-size: 24px; font-weight: bold;">🛡️ HANNA Terminal</div>', unsafe_allow_index=True)
st.caption(f"Système Opérationnel | {datetime.now().strftime('%H:%M')}")
st.divider()

# Gestionnaire de Notes
if 'notes' not in st.session_state:
    st.session_state.notes = []

new_note = st.text_input("Mémoriser une donnée :", key="note_input")
if st.button("Enregistrer"):
    if new_note:
        st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
        st.success("Donnée mémorisée.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.write(f"• {n}")

if st.button("🔒 Déconnexion Sécurisée"):
    st.session_state.auth = False
    st.rerun()
