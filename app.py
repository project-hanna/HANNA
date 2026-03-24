import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION ---
LOGO_FILE = "logo1.png"

st.set_page_config(page_title="HANNA", layout="centered")

@st.cache_data
def get_ui_elements(file_path):
    """Mise en cache du logo pour une vitesse d'exécution maximale."""
    logo_b64 = ""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    return logo_b64

LOGO_B64 = get_ui_elements(LOGO_FILE)

# --- ARCHITECTURE CSS BDD9.5 (XXL & ESPACEMENT OPTIMISÉ) ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 500px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    /* Header Premium */
    .hanna-header {{ text-align: center; margin-bottom: 2rem; }}
    
    /* Espacement de 2 lignes (3rem) entre logo et titre */
    .hanna-logo {{ 
        width: 120px; 
        margin-bottom: 3rem; 
    }}
    
    .hanna-title {{ 
        font-weight: 200; 
        letter-spacing: 14px; 
        font-size: 52px; 
        color: #000; 
        text-transform: uppercase; 
        margin: 0; 
        line-height: 1.1;
    }}
    
    .hanna-sub {{ 
        font-weight: 300; 
        font-size: 8px; 
        color: #999; 
        letter-spacing: 2px; 
        text-transform: uppercase; 
        margin-top: 5px;
    }}

    /* Inputs Design - Focus XXL */
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

    /* Style des Notes */
    .stInfo {{
        background-color: #fcfcfc;
        border: 1px solid #f0f0f0;
        color: #333;
        font-size: 14px;
        border-radius: 6px;
    }}

    /* Masquer les éléments Streamlit natifs */
    #MainMenu, footer, header {{ visibility: hidden; }}
    </style>
    
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <p class="hanna-title">HANNA</p>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)

# --- ÉTAT DE LA SESSION ---
if 'notes' not in st.session_state: 
    st.session_state.notes = []

# --- MOTEUR DE CAPTURE ---
def process_entry():
    if st.session_state.get('entry'):
        ts = datetime.now().strftime("%H:%M")
        # Ajout en tête de liste pour l'affichage inversé
        st.session_state.notes.insert(0, f"[{ts}] {st.session_state.entry}")
        st.session_state.entry = "" 

# --- INTERFACE DE SAISIE ---
st.text_input(
    "CAPTURE", 
    label_visibility="collapsed", 
    placeholder="Demandez à HANNA", 
    key="entry", 
    on_change=process_entry
)

# --- AFFICHAGE DES FLUX ---
if st.session_state.notes:
    for note in st.session_state.notes:
        st.info(note)
