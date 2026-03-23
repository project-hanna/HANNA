import streamlit as st
from datetime import datetime
import base64
import os

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="HANNA", layout="centered", initial_sidebar_state="collapsed")

# --- 2. GESTION DU LOGO ---
LOGO_FILE = "logo1.png"
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

LOGO_B64 = get_base64_logo(LOGO_FILE)

# --- 3. ARCHITECTURE CSS BDD8.8 (CURSEUR À GAUCHE) ---
st.markdown(f"""
    <style>
    /* 1. Force le conteneur global à tout centrer */
    .main .block-container {{
        max-width: 550px !important;
        padding: 4rem 1rem !important;
        margin: 0 auto !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }}

    /* 2. Écrase les conteneurs verticaux pour le milieu */
    [data-testid="stVerticalBlock"], 
    [data-testid="stVerticalBlock"] > div,
    [data-testid="stVerticalBlock"] > div > div {{
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }}

    /* 3. Header HANNA */
    .hanna-header {{
        width: 100% !important;
        text-align: center !important;
        margin-bottom: 3.5rem !important;
    }}

    .hanna-logo {{
        width: 120px !important;
        height: auto !important;
        margin-bottom: 25px !important;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        font-size: 52px;
        color: #000;
        text-transform: uppercase;
        margin: 0 !important;
        letter-spacing: 14px; 
        margin-right: -14px !important; 
        line-height: 1;
    }}

    .hanna-sub {{
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        font-size: 9px;
        color: #999;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-top: 15px !important;
        margin-right: -2.5px !important;
    }}

    /* 4. CHAMP DE SAISIE : Boîte centrée, texte/curseur à GAUCHE */
    div.stTextInput {{
        width: 100% !important;
        max-width: 480px !important;
        margin: 0 auto !important;
    }}
    
    div.stTextInput input {{ 
        text-align: left !important; /* CURSEUR À GAUCHE */
        padding-left: 20px !important; /* Marge pour l'esthétique */
        border-radius: 12px !important; 
        border: 1px solid #EEE
