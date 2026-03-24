import streamlit as st
from datetime import datetime
import base64
import os
import time

# --- CONFIGURATION BDD-V10.3 ---
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA", layout="centered")

@st.cache_data
def get_ui_elements(file_path):
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS BDD-V10.3 ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 500px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    .hanna-header {{ text-align: center; margin-bottom: 2rem; width: 100%; }}
    .hanna-logo {{ width: 140px; margin-bottom: 3rem; display: block; margin-left: auto; margin-right: auto; }}
    
    /* Centrage universel (PC & Android) */
    .hanna-title {{ 
        font-weight: 200; font-size: 52px; color: #000; 
        text-transform: uppercase; margin: 0; line-height: 1.1;
        text-align: center; width: 100%;
    }}
    
    .hanna-sub {{ 
        font-weight: 300; font-size: 8px; color: #999; 
        text-transform: uppercase; margin-top: 10px;
        text-align: center; width: 100%;
    }}

    /* Input Design */
    div.stTextInput > div > div > input {{ 
        text-align: center; border-radius: 8px; height: 45px; 
        border: 1px solid #eee; background: #fafafa; font-size: 16px;
    }}

    /* Style de réponse HANNA */
    .hanna-response {{
        margin-top: 2rem; padding: 1.5rem; border-radius: 12px;
        background-color: #fcfcfc; border: 1px solid #f0f0f0;
        color: #333; font-size: 15px; line-height: 1.6;
        animation: fadeIn 0.5s ease-in-out;
    }}

    @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- RENDU HEADER ---
st.markdown(f"""
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">H&nbsp;A&nbsp;N&nbsp;N&nbsp;A</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
    """, unsafe_allow_html=True)

# --- LOGIQUE DE TRAITEMENT ---
def process_hanna_logic(query):
    """Simule la réflexion de HANNA avant réponse."""
    # Ici, nous connecterons ton API ou ton moteur de règles plus tard
    if "bonjour" in query.lower():
        return "Bonjour. Système HANNA opérationnel. En quoi puis-je vous assister aujourd'hui ?"
    elif "heure" in query.lower():
        return f"Il est actuellement {datetime.now().strftime('%H:%M')}."
    else:
        return f"Analyse de la requête : '{query}'. En attente d'instructions complémentaires sur le protocole BDD-V10.3."

# --- ZONE DE SAISIE ---
user_input = st.text_input("", placeholder="Demander à HANNA", label_visibility="collapsed")

if user_input:
    with st.spinner(''):
        # On simule un léger délai pour l'aspect "Adaptive Assistant"
        time.sleep(0.5)
        response = process_hanna_logic(user_input)
        
    st.markdown(f"""
        <div class="hanna-response">
            {response}
        </div>
        """, unsafe_allow_html=True)

# Optionnel : Affichage du status BDD discret en bas
st.markdown("<br><br><p style='text-align:center; color:#eee; font-size:9px;'>BDD-V10.3 ACTIVE</p>", unsafe_allow_html=True)
