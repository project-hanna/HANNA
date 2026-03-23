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

# --- 3. ARCHITECTURE CSS BDD8.5 + CORRECTIF CIBLÉ PLACEHOLDER ---
st.markdown(f"""
    <style>
    /* Structure de base BDD8.5 */
    .main .block-container {{
        max-width: 550px !important;
        padding: 4rem 1rem !important;
        margin: 0 auto !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: flex-start !important;
    }}

    [data-testid="stVerticalBlock"] {{
        align-items: center !important;
        width: 100% !important;
    }}

    .hanna-header {{
        width: 100% !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        margin-bottom: 3.5rem !important;
    }}

    .hanna-logo {{
        width: 120px !important;
        height: auto !important;
        margin-bottom: 25px !important;
        display: block !important;
    }}

    .hanna-title {{
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        font-size: 52px;
        color: #000;
        text-transform: uppercase;
        margin: 0 !important;
        line-height: 1;
        letter-spacing: 14px; 
        margin-right: -14px !important; 
        display: block !important;
        width: 100% !important;
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

    /* --- SEULE MODIFICATION : CENTRAGE FORCÉ DU PLACEHOLDER --- */
    div.stTextInput {{ width: 100% !important; max-width: 480px !important; }}
    
    div.stTextInput input {{ 
        text-align: center !important; /* Centre le texte saisi */
        border-radius: 12px !important; 
        border: 1px solid #EEE !important;
        height: 50px !important;
        background: #FDFDFD !important;
    }}

    /* Force le centrage du texte 'Demander à HANNA' pour tous les navigateurs */
    div.stTextInput input::placeholder {{
        text-align: center !important;
        width: 100%;
    }}
    div.stTextInput input::-webkit-input-placeholder {{
        text-align: center !important;
    }}
    div.stTextInput input::-moz-placeholder {{
        text-align: center !important;
    }}
    div.stTextInput input:-ms-input-
