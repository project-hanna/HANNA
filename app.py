import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION HANNA V10.00 ---
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA V10", layout="centered")

@st.cache_data
def get_ui_elements(file_path):
    """Mise en cache des ressources graphiques."""
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS BDD 10.00 (ULTRA-MINIMALISTE) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    .block-container {{ padding: 2rem 1rem 0; max-width: 550px; }}
    .stApp {{ background: #ffffff; font-family: 'Inter', sans-serif; }}
    
    /* Header Architecture V10 */
    .hanna-header {{ text-align: center; margin-bottom: 4rem; }}
    
    .hanna-logo-container {{ 
        display: flex; 
        justify-content: center; 
        margin-bottom: 3.5rem; 
    }}
    
    .hanna-logo {{ 
        width: 100px; 
        filter: grayscale(100%);
        transition: 0.3s ease;
    }}

    .hanna-title {{ 
        font-weight: 100; 
        letter-spacing: 18px; 
        font-size: 58px; 
        color: #000; 
        text-transform: uppercase; 
        margin: 0; 
        line-height: 1;
        padding-left: 18px; /* Compensation pour le letter-spacing */
    }}
    
    .hanna-sub {{ 
        font-weight: 300; 
        font-size: 9px; 
        color: #aaaaaa; 
        letter-spacing: 4px; 
        text-transform: uppercase; 
        margin-top: 15px;
    }}

    /* Input Design V10 - Focus Minimal */
    div.stTextInput > div > div > input {{ 
        text-align: center; 
        border-radius: 0px; 
        height: 50px; 
        border: none;
        border-bottom: 1px solid #eeeeee;
        background: transparent; 
        font-size: 18px;
        font-weight: 200;
        transition: border-color 0.4s;
    }}
    
    div.stTextInput > div > div > input:focus {{
        border-bottom: 1px solid #000;
        box-shadow: none;
        outline: none;
    }}

    /* Masquer les éléments Streamlit par défaut */
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- RENDU UI ---
st.markdown(f"""
    <div class="hanna-header">
        <div class="hanna-logo-container">
            <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        </div>
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant • V10.00</p>
    </div>
    """, unsafe_allow_html=True)

user_input = st.text_input("", placeholder="Entrez une commande ou un texte...", label_visibility="collapsed")

if user_input:
    # Logique de traitement ici
    st.write(f"Exécution BDD 10.00 : {user_input}")
