import streamlit as st
import google.generativeai as genai
import base64
import os

# --- CONFIGURATION HANNA ---
LOGO_FILE = "logo1.png"
APP_NAME = "HANNA"
APP_SUB = "Hybrid Adaptive Navigator & Network Assistant"

st.set_page_config(page_title=APP_NAME, layout="centered")

# --- INITIALISATION IA (AVEC GESTION QUOTA) ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    try:
        # On tente d'abord le modèle flash qui est le plus rapide
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=f"Tu es {APP_NAME}. Ton ton est professionnel et concis."
        )
    except:
        # Fallback si flash n'est pas dispo
        model = genai.GenerativeModel('gemini-pro')
else:
    st.error("Clé API manquante.")

# --- LOGO ---
@st.cache_data
def get_ui_elements(file_path):
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS (BOUTON COMPACT) ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 500px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    /* Suppression des textes parasites */
    div[data-testid="stInstructions"], 
    div[data-testid="stTextInput"] small,
    .st-emotion-cache-16idsys p {{ display: none !important; }}

    .hanna-header {{ text-align: center; margin-bottom: 2rem; display: flex; flex-direction: column; align-items: center; width: 100%; }}
    .hanna-logo-wrapper {{ display: flex; justify-content: center; width: 100%; margin-bottom: 3.5rem; }}
    .hanna-logo {{ width: 120px; }}
    .hanna-title {{ font-weight: 200; letter-spacing: 14px; font-size: 52px; color: #000; text-transform: uppercase; margin: 0; line-height: 1.1; padding-left: 14px; text-align: center; }}
    .hanna-sub {{ font-weight: 300; font-size: 8px; color: #999; letter-spacing: 2px; text-transform: uppercase; margin-top: 5px; text-align: center; }}

    /* Input Design */
    div.stTextInput > div > div > input {{ 
        border-radius: 8px; height: 40px; border: 1px solid #eee; background: #fafafa; font-size: 15px;
    }}
    
    /* BOUTON COMPACT ET CARRÉ */
    .stButton > button {{
        border-radius: 8px; 
        height: 40px; 
        width: 40px !important; 
        min-width: 40px !important;
        padding: 0 !important;
        background-color: #000; 
        color: white; 
        border: none; 
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 1px;
    }}
    .stButton > button:hover {{ background-color: #333; color: white; }}

    .hanna-response {{
        margin-top: 2rem; padding: 1.5rem; border-radius: 12px; background-color: #ffffff; border: 1px solid #f2f2f2; color: #333; font-size: 15px; line-height: 1.6;
    }}

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

# --- BARRE DE SAISIE OPTIMISÉE ---
# On utilise un ratio 10 pour 1 pour que la colonne du bouton soit très petite
col1, col2 = st.columns([10, 1.2])

with col1:
    user_input = st.text_input("", placeholder="Demander à HANNA", label_visibility="collapsed")

with col2:
    submit_clicked = st.button("→")

# --- LOGIQUE DE RÉPONSE ---
if (user_input and user_input.strip() != "") or submit_clicked:
    if user_input:
        try:
            with st.spinner(""):
                response = model.generate_content(user_input)
                if response.text:
                    st.markdown(f'<div class="hanna-response">{response.text}</div>', unsafe_allow_html=True)
        except Exception as e:
            if "429" in str(e):
                st.error("Quota atteint. Attends quelques secondes ou change de clé API.")
            else:
                st.error(f"Erreur : {e}")
