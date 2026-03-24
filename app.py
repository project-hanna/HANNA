import streamlit as st
from datetime import datetime
import base64
import os
import time

# --- CONFIGURATION BDD-V10.3 ---
LOGO_FILE = "logo1.png"

st.set_page_config(
    page_title="HANNA", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

@st.cache_data
def get_ui_elements(file_path):
    """Mise en cache du logo pour une vitesse d'exécution maximale."""
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS (CENTRAGE UNIVERSEL & CHAT PREMIUM) ---
st.markdown(f"""
    <style>
    /* Configuration Container */
    .block-container {{ padding: 2rem 1rem 5rem; max-width: 550px; }}
    .stApp {{ background: #ffffff; font-family: 'Inter', sans-serif; }}
    
    /* Header & Centrage Logo */
    .hanna-header {{ 
        text-align: center; 
        margin-bottom: 2rem; 
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}
    
    .hanna-logo {{ 
        width: 140px; 
        margin-bottom: 2.5rem; 
        display: block;
    }}
    
    /* Titre HANNA (Méthode espaces insécables pour Android/PC) */
    .hanna-title {{ 
        font-weight: 200; 
        font-size: 52px; 
        color: #000; 
        text-transform: uppercase; 
        margin: 0; 
        line-height: 1.1;
        text-align: center; 
        width: 100%;
    }}
    
    .hanna-sub {{ 
        font-weight: 300; 
        font-size: 8px; 
        color: #999; 
        text-transform: uppercase; 
        margin-top: 10px;
        text-align: center; 
        width: 100%;
    }}

    /* Personnalisation des bulles de Chat native Streamlit */
    [data-testid="stChatMessage"] {{
        background-color: transparent !important;
        padding: 10px 0;
    }}
    
    [data-testid="stChatMessageContent"] {{
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 15px !important;
        font-size: 15px;
        color: #333;
        border: 1px solid #eee;
    }}

    /* Inversion de style pour HANNA (bulles blanches bordées noir) */
    [data-testid="stChatMessage"]:nth-child(even) [data-testid="stChatMessageContent"] {{
        background-color: #ffffff;
        border: 1px solid #000;
        color: #000;
    }}

    /* Masquer les éléments Streamlit superflus */
    #MainMenu, footer, header {{visibility: hidden;}}
    .stChatFloatingInputContainer {{bottom: 20px;}}
    </style>
    """, unsafe_allow_html=True)

# --- INITIALISATION SESSION (HISTORIQUE) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- RENDU INTERFACE ---
st.markdown(f"""
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">H&nbsp;A&nbsp;N&nbsp;N&nbsp;A</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
    """, unsafe_allow_html=True)

# Affichage des messages passés
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- LOGIQUE DE RÉPONSE ---
def hanna_brain(prompt):
    """Moteur de logique pour HANNA BDD-V10.3"""
    query = prompt.lower()
    if "bonjour" in query or "salut" in query:
        return "Bonjour. Système HANNA opérationnel. En quoi puis-je vous assister aujourd'hui ?"
    elif "heure" in query:
        return f"Il est actuellement {datetime.now().strftime('%H:%M')}."
    elif "statut" in query or "version" in query:
        return "Statut : Nominal. Architecture : BDD-V10.3 active. Protocoles de centrage universels déployés."
    else:
        return f"Analyse effectuée : '{prompt}'. Je suis prêt pour la prochaine phase de programmation."

# --- ZONE DE SAISIE ---
if prompt := st.chat_input("Demander à HANNA"):
    # Ajout message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Réponse HANNA avec effet de frappe
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        reply = hanna_brain(prompt)
        
        for chunk in reply.split():
            full_response += chunk + " "
            time.sleep(0.06)
            response_placeholder.markdown(full_response + "▌")
        response_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": reply})
