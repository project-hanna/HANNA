import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA", layout="centered")

@st.cache_data
def get_ui_elements(file_path):
    """Mise en cache du logo pour une vitesse d'exécution maximale."""
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS BDD7 (OPTIMISÉE & XXL) ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 500px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    /* Header Premium */
    .hanna-header {{ text-align: center; margin-bottom: 1.5rem; }}
    .hanna-logo {{ width: 120px; margin-bottom: 5px; }}
    
    .hanna-title {{ 
        font-weight: 200; 
        letter-spacing: 14px; 
        font-size: 52px; 
        color: #000; 
        text-transform: uppercase; 
        margin: 0; 
        line-height: 1.1;
    }}
    
    .hanna-sub {{ 
        font-weight: 300; 
        font-size: 8px; 
        color: #999; 
        letter-spacing: 2px; 
        text-transform: uppercase; 
        margin-top: 5px;
    }}

    /* Inputs Design - Validation Clavier */
    div.stTextInput > div > div > input {{ text-align: center; border-radius: 8px; height: 45px; border: 1px solid #eee; background: #fafafa; }}
    
    /* Bouton Show Password à Gauche */
    div[data-baseweb="input"] > div {{
        flex-direction: row-reverse !important;
    }}
    div[data-baseweb="input"] button {{
        margin-left: 10px !important;
        margin-right: 0 !important;
    }}

    /* UI Clean & Bouton Quitter */
    .stButton > button {{ width: 100%; background: transparent; color: #ccc; border: 1px solid #eee; font-size: 10px; letter-spacing: 1px; height: 35px; transition: 0.3s; }}
    .stButton > button:hover {{ color: #000; border-color: #000; }}

    #MainMenu, footer, header {{ visibility: hidden; }}
    </style>
    
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <p class="hanna-title">HANNA</p>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# --- ÉTAT DE LA SESSION ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'notes' not in st.session_state: st.session_state.notes = []

# --- MOTEUR DE CAPTURE (ENTRÉE CLAVIER) ---
def process_entry():
    if st.session_state.get('entry'):
        ts = datetime.now().strftime("%H:%M")
        st.session_state.notes.append(f"[{ts}] {st.session_state.entry}")
        st.session_state.entry = "" 

# --- ROUTAGE ---
if not st.session_state.auth:
    # Page Connexion
    pwd = st.text_input("CODE", type="password", label_visibility="collapsed", placeholder="CODE D'ACCÈS")
    if pwd:
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Accès refusé.")
    st.stop()
else:
    # Page Principale
    st.divider()
    st.text_input("CAPTURE", label_visibility="collapsed", placeholder="Demandez à HANNA", 
                  key="entry", on_change=process_entry)

    # Affichage des notes
    if st.session_state.notes:
        for note in reversed(st.session_state.notes):
            st.info(note)

    st.write("---")
    if st.button("QUITTER LA SESSION"):
        st.session_state.clear()
        st.rerun()
