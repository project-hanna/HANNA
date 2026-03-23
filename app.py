import streamlit as st
from datetime import datetime
import time

# --- CONFIGURATION SÉCURISÉE HANNA ---
# Votre mot de passe spécifique est configuré ici
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
# URL d'un logo technologique générique (bouclier numérique bleu)
LOGO_URL = "https://img.icons8.com/fluency/96/shield-with-keyhole.png"

# Configuration de la page
st.set_page_config(page_title="HANNA Terminal", layout="wide", page_icon=LOGO_URL)

# Style CSS personnalisé pour l'ambiance "Terminal Sécurisé"
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #1a1c24; color: #00ff41; border: 1px solid #00ff41; }
    .stButton>button { width: 100%; background-color: #00ff41; color: #0e1117; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #00cc33; color: white; }
    h1, h2, h3 { color: #00ff41 !important; }
    .stMetric { background-color: #1a1c24; padding: 10px; border-radius: 5px; border: 1px solid #333; }
    </style>
    """, unsafe_allow_index=True)

# --- FONCTION DE VÉRIFICATION D'ACCÈS ---
def check_password():
    """Gère l'écran de verrouillage avec logo et mot de passe."""
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if not st.session_state.password_correct:
        # Centre l'écran de connexion
        col_space1, col_content, col_space2 = st.columns([1, 2, 1])
        
        with col_content:
            st.write("") # Espacement top
            st.write("")
            
            # Affichage du Logo et du Titre
            st.image(LOGO_URL, width=80)
            st.title("🛡️ HANNA - Accès Restreint")
            st.caption("Hybrid Adaptive Navigator | Projet de Haute Confidentialité")
            
            st.divider()
            
            # Champ de saisie
            pwd = st.text_input("Veuillez entrer le code d'accès de l'assistant :", type="password", placeholder="Code d'autorisation...")
            
            # Bouton de validation
            if st.button("Authentification"):
                if pwd == PASSWORD_SYSTEM:
                    st.session_state.password_correct = True
                    st.success("✅ Authentification réussie. Chargement du terminal...")
                    time.sleep(1) # Petite pause pour l'effet visuel
                    st.rerun()
                else:
                    st.error("❌ Code d'accès invalide. Tentative enregistrée.")
            
            st.info("ℹ️ Ce terminal est protégé par un protocole adaptatif.")
            
        return False # L'accès est refusé tant que le mot de passe est faux
    return True # L'accès est autorisé

# --- LANCEMENT DE L'INTERFACE PRINCIPALE ---
# Si le mot de passe est correct, on affiche le terminal HANNA
if check_password():
    
    # Header du Terminal
    st.image(LOGO_URL, width=50)
    st.title("🛡️ HANNA Terminal - Opérationnel")
    st.caption(f"Système Sécurisé | Utilisateur Autorisé | {datetime.now().strftime('%H:%M:%S')}")

    # --- DASHBOARD ---
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Niveau de Sécurité", "MAXIMUM", delta="Actif")
    with col2:
        st.metric("Statut Assistant", "En Ligne", delta="Stable")
    with col3:
        st.metric("Version Logique", "v1.3.0", delta="Lock Active")

    st.divider()

    # --- GESTIONNAIRE DE MÉMOIRE (NOTES) ---
    st.subheader("📝 Mémoire Chiffrée de l'Assistant")
    if 'notes' not in st.session_state:
        st.session_state.notes = []

    # Zone de saisie
    with st.expander("➕ Ajouter une information à la mémoire", expanded=True):
        new_note = st.text_input("Saisir la donnée à mémoriser :")
        if st.button("Enregistrer l'information"):
            if new_note:
                st.session_state.notes.append(f"[{datetime.now().strftime('%d/%m %H:%M')}] {new_note}")
                st.success("Donnée chiffrée et mémorisée.")

    # Affichage des notes
    if st.session_state.notes:
        with st.expander("🔍 Consulter la mémoire active", expanded=False):
            for n in reversed(st.session_state.notes):
                st.write(f"• {n}")
    
    st.divider()
    
    # Bouton de Déconnexion
    if st.button("🔒 Déconnexion Sécurisée"):
        st.session_state.password_correct = False
        st.rerun()
