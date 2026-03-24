import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION ---
LOGO_FILE = "logo1.png"

st.set_config(page_title="HANNA", layout="centered")

@st.cache_data
def get_ui_elements(file_path):
    """Mise en cache du logo pour une vitesse d'exécution maximale."""
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 500px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    /* Centrage Global du Header */
    .hanna-header {{ 
        text-align: center; 
        margin-bottom: 2rem; 
        display: flex;
        flex-direction: column;
        align-items: center;
    }}
    
    /* Centrage du Logo */
    .hanna-logo-wrapper {{
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 3rem;
    }}
    
    .hanna-logo {{ 
        width: 120px; 
    }}
    
    /* Centrage Parfait de HANNA (Compensation du letter-spacing) */
    .hanna-title {{ 
        font-weight: 200; 
        letter-spacing: 14px; 
        font-size: 52px; 
        color: #000; 
        text-transform: uppercase; 
        margin: 0; 
        line-height: 1.1;
        padding-left: 14px; /* Force le centrage réel en compensant l'espace à droite */
        width: 100%;
        text-align: center;
    }}
    
    .hanna-sub {{ 
        font-weight: 300; 
        font-size: 8px; 
        color: #999; 
        letter-spacing: 2px; 
        text-transform: uppercase; 
        margin-top: 5px;
        padding-left: 2px; /* Compensation du letter-spacing du sous-titre */
        width: 100%;
        text-align: center;
    }}

    /* Inputs Design */
    div.stTextInput > div > div > input {{ 
        text-align: center; 
        border-radius: 8px; 
        height: 45px; 
        border: 1px solid #eee; 
        background: #fafafa; 
        font-size: 16px;
    }}
    
    div.stTextInput > div > div > input:focus {{
        border-color: #000;
        box-shadow: none;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- RENDU ---
st.markdown(f"""
    <div class="hanna-header">
        <div class="hanna-logo-wrapper">
            <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        </div>
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
    """, unsafe_allow_html=True)

user_input = st.text_input("", placeholder="Demander à HANNA", label_visibility="collapsed")

if user_input:
    # Logique de traitement
    pass
