import streamlit as st
from datetime import datetime
import base64
import os
import time
from openai import OpenAI

# --- CONFIGURATION BDD-V10.3-AI ---
# Récupération de la clé API (via Streamlit Secrets ou variable d'env)
# Pour tester localement, vous pouvez remplacer par : client = OpenAI(api_key="VOTRE_CLE_ICI")
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    client = None

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

# --- ARCHITECTURE CSS (CONSOLIDÉE) ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 2rem 1rem 5rem; max-width: 550px; }}
    .stApp {{ background: #ffffff; font-family: 'Inter', sans-serif; }}
    
    .hanna-header {{ text-align: center; margin-bottom: 2rem; width: 100%; display: flex; flex-direction: column; align-items: center; }}
    .hanna-logo {{ width: 140px; margin-bottom: 2.5rem; }}
    
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

    [data-testid="stChatMessageContent"] {{
        background-color: #f8f9fa; border-radius: 15px; padding: 15px !important;
        font-size: 15px; color: #333; border: 1px solid #eee;
    }}
    
    [data-testid="stChatMessage"]:nth-child(even) [data-testid="stChatMessageContent"] {{
        background-color: #ffffff; border: 1px solid #000; color: #000;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- INITIALISATION SESSION ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Tu es HANNA (Hybrid Adaptive Navigator & Network Assistant). Tu es un assistant d'excellence, concis, brillant et dévoué à l'utilisateur qui a délégation totale d'autorité."}
    ]

# --- RENDU HEADER ---
st.markdown(f"""
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">H&nbsp;A&nbsp;N&nbsp;N&nbsp;A</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
    """, unsafe_allow_html=True)

# Affichage des messages (sauf le message système)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- LOGIQUE IA ---
if prompt := st.chat_input("Demander à HANNA"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        if client:
            # Appel réel à l'IA
            response = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=st.session_state.messages,
                stream=True,
            )
            for chunk in response:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
        else:
            # Mode dégradé si pas de clé API
            error_msg = "ERREUR : Clé API non configurée. Veuillez ajouter votre clé OpenAI pour activer l'intelligence de HANNA."
            for word in error_msg.split():
                full_response += word + " "
                time.sleep(0.05)
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
