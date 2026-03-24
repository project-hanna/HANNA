import streamlit as st
import google.generativeai as genai
import base64
import os

# --- CONFIGURATION HANNA ---
LOGO_FILE = "logo1.png"
APP_NAME = "HANNA"
APP_SUB = "Hybrid Adaptive Navigator & Network Assistant"

st.set_page_config(page_title=APP_NAME, layout="centered")

# --- INITIALISATION MOTEUR IA ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    try:
        # Détection automatique du meilleur modèle disponible
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if available_models:
            # Sélection du modèle le plus performant disponible
            selected_model = available_models[0]
            
            # Définition de la personnalité de HANNA
            model = genai.GenerativeModel(
                model_name=selected_model,
                system_instruction=f"Tu es {APP_NAME} ({APP_SUB}). Ton ton est professionnel, concis et analytique. Tu es l'assistant personnel de l'utilisateur pour ses projets et son architecture réseau."
            )
        else:
            st.error("Aucun modèle compatible trouvé sur votre compte Google AI.")
    except Exception as e:
        st.error(f"Erreur d'initialisation : {e}")
else:
    st.error("Clé GOOGLE_API_KEY manquante dans les Secrets Streamlit.")

# --- CHARGEMENT DU LOGO ---
@st.cache_data
def get_ui_elements(file_path):
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS (DESIGN v10.10) ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 500px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    /* Header Centré */
    .hanna-header {{ 
        text-align: center; 
        margin-bottom: 2rem; 
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }}
    
    .hanna-logo-wrapper {{
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 3.5rem;
    }}
    
    .hanna-logo {{ width: 120px; }}
    
    .hanna-title {{ 
        font-weight: 200; 
        letter-spacing: 14px; 
        font-size: 52px; 
        color: #000; 
        text-transform: uppercase; 
        margin: 0; 
        line-height: 1.1;
        padding-left: 14px; 
        text-align: center;
    }}
    
    .hanna-sub {{ 
        font-weight: 300; 
        font-size: 8px; 
        color: #999; 
        letter-spacing: 2px; 
        text-transform: uppercase; 
        margin-top: 5px;
        text-align: center;
    }}

    /* Input Design */
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

    /* Zone de réponse */
    .hanna-response {{
        margin-top: 2rem;
        padding: 1.5rem;
        border-radius: 12px;
        background-color: #ffffff;
        border: 1px solid #f2f2f2;
        color: #333;
        font-size: 15px;
        line-height: 1.6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02);
    }}

    /* Masquer les éléments Streamlit superflus */
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- RENDU INTERFACE ---
st.markdown(f"""
    <div class="hanna-header">
        <div class="hanna-logo-wrapper">
            <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        </div>
        <h1 class="hanna-title">{APP_NAME}</h1>
        <p class="hanna-sub">{APP_SUB}</p>
    </div>
    """, unsafe_allow_html=True)

# Champ de saisie
user_input = st.text_input("", placeholder="Demander à HANNA", label_visibility="collapsed")

# --- LOGIQUE DE RÉPONSE ---
if user_input:
    try:
        with st.spinner(""):
            # Génération de la réponse
            response = model.generate_content(user_input)
            
            if response.text:
                st.markdown(f'<div class="hanna-response">{response.text}</div>', unsafe_allow_html=True)
            else:
                st.warning("Réponse vide générée.")
    except Exception as e:
        st.error(f"Erreur technique : {e}")
