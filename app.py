import streamlit as st
import google.generativeai as genai
import base64
import os

# --- CONFIGURATION HANNA ---
LOGO_FILE = "logo1.png"
APP_NAME = "HANNA"
APP_SUB = "Hybrid Adaptive Navigator & Network Assistant"

st.set_page_config(page_title=APP_NAME, layout="centered")

# --- INITIALISATION IA ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if available_models:
            model = genai.GenerativeModel(
                model_name=available_models[0],
                system_instruction=f"Tu es {APP_NAME} ({APP_SUB}). Ton ton est professionnel et concis."
            )
    except Exception as e:
        st.error(f"Erreur d'initialisation : {e}")

# --- LOGO ---
@st.cache_data
def get_ui_elements(file_path):
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS (NETTOYAGE COMPLET) ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 500px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    /* SUPPRESSION DU TEXTE "PRESS ENTER TO APPLY" */
    div.stTextInput small {{
        display: none !important;
    }}

    .hanna-header {{ text-align: center; margin-bottom: 2rem; display: flex; flex-direction: column; align-items: center; width: 100%; }}
    .hanna-logo-wrapper {{ display: flex; justify-content: center; width: 100%; margin-bottom: 3.5rem; }}
    .hanna-logo {{ width: 120px; }}
    .hanna-title {{ font-weight: 200; letter-spacing: 14px; font-size: 52px; color: #000; text-transform: uppercase; margin: 0; line-height: 1.1; padding-left: 14px; text-align: center; }}
    .hanna-sub {{ font-weight: 300; font-size: 8px; color: #999; letter-spacing: 2px; text-transform: uppercase; margin-top: 5px; text-align: center; }}

    div.stTextInput > div > div > input {{ 
        text-align: center; border-radius: 8px; height: 45px; border: 1px solid #eee; background: #fafafa; font-size: 16px;
    }}
    
    div.stTextInput > div > div > input:focus {{ border-color: #000; box-shadow: none; }}

    .hanna-response {{
        margin-top: 2rem; padding: 1.5rem; border-radius: 12px; background-color: #ffffff; border: 1px solid #f2f2f2; color: #333; font-size: 15px; line-height: 1.6;
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
        <h1 class="hanna-title">{APP_NAME}</h1>
        <p class="hanna-sub">{APP_SUB}</p>
    </div>
    """, unsafe_allow_html=True)

user_input = st.text_input("", placeholder="Demander à HANNA", label_visibility="collapsed")

if user_input:
    try:
        with st.spinner(""):
            response = model.generate_content(user_input)
            if response.text:
                st.markdown(f'<div class="hanna-response">{response.text}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Erreur technique : {e}")
