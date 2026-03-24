import streamlit as st
import google.generativeai as genai
import base64
import os

# --- CONFIGURATION HANNA BDD11 ---
LOGO_FILE = "logo1.png"
APP_NAME = "HANNA"
APP_SUB = "Hybrid Adaptive Navigator & Network Assistant"

st.set_page_config(page_title=APP_NAME, layout="centered")

# --- INITIALISATION ÉTAT DE SESSION (MÉMOIRE) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- INITIALISATION IA ---
model = None
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if available_models:
            model = genai.GenerativeModel(
                model_name=available_models[0],
                system_instruction=f"Tu es {APP_NAME}. Ton ton est professionnel, concis et tu as de la mémoire sur la conversation actuelle."
            )
    except Exception as e:
        st.error(f"Initialisation impossible : {e}")

# --- LOGO ---
@st.cache_data
def get_ui_elements(file_path):
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS BDD11 + BOUTON RESET ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 500px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    /* Suppression radicale des textes d'aide Streamlit */
    div[data-testid="stInstructions"], 
    div[data-testid="stTextInput"] small,
    div[data-testid="InputInstructions"],
    .st-emotion-cache-16idsys p {{ display: none !important; }}

    .hanna-header {{ text-align: center; margin-bottom: 2rem; display: flex; flex-direction: column; align-items: center; width: 100%; }}
    .hanna-logo-wrapper {{ display: flex; justify-content: center; width: 100%; margin-bottom: 3.5rem; }}
    .hanna-logo {{ width: 120px; }}
    .hanna-title {{ font-weight: 200; letter-spacing: 14px; font-size: 52px; color: #000; text-transform: uppercase; margin: 0; line-height: 1.1; padding-left: 14px; text-align: center; }}
    .hanna-sub {{ font-weight: 300; font-size: 8px; color: #999; letter-spacing: 2px; text-transform: uppercase; margin-top: 5px; text-align: center; }}

    /* Input & Bouton */
    div.stTextInput > div > div > input {{ border-radius: 8px; height: 40px; border: 1px solid #eee; background: #fafafa; }}
    .stButton > button {{ border-radius: 8px; height: 40px; width: 40px !important; background-color: #000; color: white; border: none; }}
    .stButton > button:hover {{ background-color: #333; color: white; }}

    /* Bouton Reset Discret (Bas de page) */
    div[data-testid="column"]:last-child button {{
        background: transparent !important; color: #ccc !important; border: none !important; font-size: 10px !important; width: auto !important;
    }}

    .hanna-response {{ margin-top: 2rem; padding: 1.5rem; border-radius: 12px; background-color: #ffffff; border: 1px solid #f2f2f2; font-size: 15px; }}

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

# --- BARRE DE SAISIE ---
col1, col2 = st.columns([10, 1.2])
with col1:
    user_input = st.text_input("", placeholder="Demander à HANNA", label_visibility="collapsed")
with col2:
    submit_clicked = st.button("→")

# --- LOGIQUE IA AVEC MÉMOIRE ---
if (user_input and user_input.strip() != "") or submit_clicked:
    if user_input and model:
        try:
            with st.spinner(""):
                # Construction du contexte (3 derniers échanges)
                history_context = "\n".join([f"Q: {m['q']}\nA: {m['a']}" for m in st.session_state.messages[-3:]])
                prompt = f"{history_context}\nQ: {user_input}\nA:" if history_context else user_input
                
                response = model.generate_content(prompt)
                
                if response and response.text:
                    # Stockage
                    st.session_state.messages.append({"q": user_input, "a": response.text})
                    # Affichage
                    st.markdown(f'<div class="hanna-response">{response.text}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erreur : {e}")

# --- PIED DE PAGE & RESET ---
st.write("---")
c1, c2 = st.columns([8, 2])
with c2:
    if st.button("Effacer la mémoire"):
        st.session_state.messages = []
        st.rerun()
