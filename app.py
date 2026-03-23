import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo.png"

# Configuration de la page
st.set_page_config(page_title="HANNA Terminal", layout="wide", initial_sidebar_state="collapsed")

# 🎨 STYLE CSS POUR LA TRANSPARENCE ET LE LOOK TERMINAL 🎨
# Ce bloc force le fond sombre et stylise les éléments
st.markdown("""
    <style>
    /* Force le fond sombre pour le projet HANNA */
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    
    /* Supprime les marges inutiles */
    .block-container { padding-top: 1rem; padding-bottom: 1rem; }
    
    /* Centre le logo et le formulaire de connexion */
    .login-box { text-align: center; max-width: 400px; margin: auto; padding: 20px; }
    
    /* Style du titre en vert terminal */
    h1, h2, h3 { color: #00ff41 !important; text-align: center; }
    
    /* Style du champ de saisie */
    .stTextInput>div>div>input { background-color: #1a1c24; color: #00ff41; border: 1px solid #333; }
    
    /* Style du bouton d'authentification */
    .stButton>button { width: 100%; background-color: #00ff41; color: #0e1117; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #00cc33; color: white; }
    </style>
    """, unsafe_allow_index=True)

# --- VÉRIFICATION D'ACCÈS (ÉCRAN DE VERROUILLAGE) ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.write("") # Espacement haut
    st.write("")
    
    # Structure centrée pour l'authentification
    col1, col_center, col3 = st.columns([1, 1.5, 1])
    
    with col_center:
        st.write("")
        
        # Tentative d'affichage de VOTRE LOGO TRANSPARENT
        if os.path.exists(LOGO_FILE):
            try:
                # L'image est affichée ici sur le fond sombre
                st.image(LOGO_FILE, width=180, use_container_width=False)
            except:
                st.title("🛡️ [HANNA]")
        else:
            st.title("🛡️ [HANNA]") # Titre de secours si logo.png absent
            st.warning("⚠️ Fichier logo.png introuvable à la racine de GitHub.")

        # Titre et formulaire
        st.subheader("Authentification Requise")
        st.caption("Hybrid Adaptive Navigator Security Module")
        
        st.write("")
        
        pwd = st.text_input("Code d'autorisation :", type="password", placeholder="Votre code...")
        
        if st.button("S'authentifier"):
            if pwd == PASSWORD_SYSTEM:
                st.session_state.auth = True
                st.success("✅ Code validé. Accès autorisé.")
                # Petite pause pour l'effet de succès
                import time
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("❌ Code incorrect. Tentative échouée.")
    st.stop()

# --- INTERFACE PRINCIPALE (DÉVERROUILLÉE) ---
st.divider()

# Header avec logo plus petit
col_logo, col_title = st.columns([0.1, 0.9])
with col_logo:
    if os.path.exists(LOGO_FILE):
        try:
            st.image(LOGO_FILE, width=60)
        except:
            pass
with col_title:
    st.title("🛡️ HANNA Terminal - Opérationnel")
    st.caption(f"Système Sécurisé | Utilisateur : mtt.mallee | {datetime.now().strftime('%H:%M')}")

st.divider()

# Gestionnaire de Notes
if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("📝 Ajouter à la mémoire", expanded=True):
    new_note = st.text_input("Saisir la donnée à mémoriser :")
    if st.button("Mémoriser"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%d/%m %H:%M')}] {new_note}")
            st.success("Donnée mémorisée.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.write(f"• {n}")

if st.button("🔒 Déconnexion Sécurisée"):
    st.session_state.auth = False
    st.rerun()
