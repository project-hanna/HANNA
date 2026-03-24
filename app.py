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

# --- ARCHITECTURE CSS (CHAT CLASSIQUE) ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 550px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    .hanna-header {{ text-align: center; margin-bottom: 2rem; width: 100%; }}
    .hanna-logo {{ width: 140px; margin-bottom: 2.5rem; display: block; margin-left: auto; margin-right: auto; }}
    
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

    /* Styles des bulles de Chat */
    .chat-container {{ margin-top: 2rem; display: flex; flex-direction: column; gap: 1rem; }}
    
    .bubble {{ 
        padding: 12px 18px; border-radius: 18px; font-size: 15px; 
        max-width: 85%; line-height: 1.4; animation: fadeIn 0.3s ease;
    }}
    
    .user-bubble {{ 
        align-self: flex-end; background-color: #f0f0f0; color: #333; 
        border-bottom-right-radius: 4px; 
    }}
    
    .hanna-bubble {{ 
        align-self: flex-start; background-color: #ffffff; color: #000; 
        border: 1px solid #eee; border-bottom-left-radius: 4px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }}

    /* Fixation de l'input en bas de page (optionnel) */
    div.stChatInput {{ margin-top: 2rem; }}
    
    @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- INITIALISATION DE L'HISTORIQUE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- RENDU HEADER ---
st.markdown(f"""
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">H&nbsp;A&nbsp;N&nbsp;N&nbsp;A</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
    """, unsafe_allow_html=True)

# --- AFFICHAGE DE LA CONVERSATION ---
for message in st.session_state.messages:
    role_class = "user-bubble" if message["role"] == "user" else "hanna-bubble"
    st.markdown(f"""<div class="bubble {role_class}">{message["content"]}</div>""", unsafe_allow_html=True)

# --- ZONE DE SAISIE (STREAMLIT CHAT INPUT) ---
if prompt := st.chat_input("Demander à HANNA"):
    # Ajout du message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Génération de la réponse HANNA (Logique BDD-V10.3)
    with st.spinner(''):
        time.sleep(0.4)
        # Logique de réponse temporaire
        response = f"Système HANNA v10.3 en ligne. Analyse de : '{prompt}'..."
        
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
