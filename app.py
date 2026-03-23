import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION & SÉCURITÉ ---
PASSWORD_SYSTEM = st.secrets.get("PASSWORD", "mtt.mallee@gmail.C94")
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

@st.cache_data(show_spinner=False)
def get_base64_logo(file_path):
    """Mise en cache optimisée du logo."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- CSS ARCHITECTURE BDD7.2 (COULEUR & DYNAMISME) ---
# Optimisation : Logo en couleur, accents interactifs
st.markdown(f"""
    <style>
    /* Reset & Container */
    .block-container {{ padding-top: 2rem; max-width: 500px; }}
    .stApp {{ background-color: #FFFFFF; }}
    
    /* Typography Premium */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400&display=swap');
    
    .hanna-header {{ text-align: center; margin-bottom: 2rem; pointer-events: none; }}
    
    /* --- MODIFICATION LOGO : EN COULEUR --- */
    .hanna-logo {{ 
        width: 100px; 
        /* Suppression de grayscale(100%) et opacity */
        filter: none; 
        opacity: 1; 
        transition: transform 0.3s ease-out; 
    }}
    /* Petit effet au survol, subtil mais moderne */
    .hanna-header:hover .hanna-logo {{
        transform: scale(1.05);
    }}
    
    .hanna-title {{ 
        font-family: 'Inter', sans-serif;
        font-weight: 200; 
        letter-spacing: 12px; 
        font-size: clamp(30px, 10vw, 52px); 
        color: #1A1A1A; /* Un noir moins agressif */
        margin: 10px 0 0 0;
        line-height: 1;
    }}
    
    .hanna-sub {{ 
        font-family: 'Inter', sans-serif;
        font-weight: 300; 
        font-size: 9px; 
        color: #999; 
        letter-spacing: 1.5px; 
        text-transform: uppercase;
        margin-top: 8px;
    }}

    /* Inputs & UI Components - Ajout d'une ombre douce */
    div[data-baseweb="input"] {{ 
        border-radius: 12px !important; 
        background: #FFFFFF !important; 
        border: 1px solid #EAEAEA !important; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        transition: box-shadow 0.2s;
    }}
    div[data-baseweb="input"]:focus-within {{
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-color: #DDD !important;
    }}
    input {{ text-align: center !important; font-family: 'Inter', sans-serif !important; color: #333; }}
    
    /* Bouton Quitter : Plus coloré au survol */
    .stButton > button {{ 
        width: 100%; border-radius: 8px; border: 1px solid #EEE; 
        background: white; color: #AAA; font-size: 11px; transition: all 0.2s;
    }}
    .stButton > button:hover {{ 
        color: #FF4B4B; /* Couleur d'accentuation pour l'action de quitter */
        border-color: #FF4B4B; 
        background: #FFF5F5; 
    }}

    /* Masquage des éléments natifs Streamlit */
    #MainMenu, footer, header {{ visibility: hidden; height: 0; }}
    </style>
    
    <div class="hanna-header">
        {"<img src='data:image/png;base64," + LOGO_B64 + "' class='hanna-logo'>" if LOGO_B64 else ""}
        <h1
