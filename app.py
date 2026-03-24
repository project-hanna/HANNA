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

# --- ARCHITECTURE CSS (CHAT PREMIUM) ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 5rem; max-width: 550px; }}
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

    /* Bulles de Chat Style Minimaliste */
    .stChatMessage {{ background-color: transparent !important; border: none !important; }}
    .stChatMessage [data-testid="stChatMessageContent"] {{
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 15px;
        font-size: 15px;
        color: #333;
        border: 1px solid #eee;
    }}
    
    /* Différenciation User / Assistant */
    [data-testid="stChatMessage"]:nth-child(even) [data-testid="stChatMessageContent"] {{
        background-color: #ffffff;
        border: 1px solid #000;
        color: #000;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- INITIALISATION DU CERVEAU (SESSION STATE) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- RENDU HEADER ---
st.markdown(f"""
    <div class="hanna-header">
        <div style="display: flex; justify-content: center; width: 100%;">
            <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        </div>
        <h1 class="hanna-title">H&nbsp;A&nbsp;N&nbsp;N&nbsp;A</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
    """, unsafe_allow_html=True)

# --- AFFICHAGE DE LA CONVERSATION ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- LOGIQUE DE RÉPONSE INTELLIGENTE ---
def generate_hanna_response(prompt):
    """
    Ici s'exécute l'intelligence de HANNA.
    Pour l'instant, elle simule une réflexion adaptative.
    """
    prompt_l = prompt.lower()
    if "bonjour" in prompt_l or "salut" in prompt_l:
        return "Bonjour. Je suis HANNA, votre assistant adaptatif. Comment puis-je vous aider aujourd'hui ?"
    elif "qui es-tu" in prompt_l:
        return "Je suis le Hybrid Adaptive Navigator & Network Assistant (HANNA), opérant sous le protocole BDD-V10.3."
    elif "statut" in prompt_l:
        return f"Systèmes nominaux. Architecture V10.3 active. Temps de réponse actuel : {time.process_time():.4f}s."
    else:
        # Ici, nous pourrions appeler openai.ChatCompletion.create(...)
        return f"Analyse en cours pour : '{prompt}'. Ma base de connaissances s'affine pour répondre précisément à cette requête."

# --- ZONE DE SAISIE ---
if prompt := st.chat_input("Demander à HANNA"):
    # Ajout du message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Génération de la réponse
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        hanna_reply = generate_hanna_response(prompt)
        
        # Effet de frappe progressive (Streaming effect)
        for chunk in hanna_reply.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": hanna_reply})
