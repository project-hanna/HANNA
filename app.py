import streamlit as st
from datetime import datetime
import base64
import os

# --- CONFIGURATION ---
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

# --- ARCHITECTURE CSS (NETTOYÉE DU DÉCALAGE) ---
st.markdown(f"""
    <style>
    .block-container {{ padding: 1rem 1rem 0; max-width: 500px; }}
    .stApp {{ background: #fff; font-family: 'Inter', sans-serif; }}
    
    .hanna-header {{ 
        text-align: center; 
        margin-bottom: 2rem; 
        width: 100%;
    }}
    
    .hanna-logo {{ 
        width: 140px; 
        margin-bottom: 3rem; 
        display: block;
        margin-left: auto;
        margin-right: auto;
    }}
    
    /* Plus de letter-spacing ici pour éviter le décalage mobile */
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

    div.stTextInput > div > div > input {{ 
        text-align: center; 
        border-radius: 8px; 
        height: 45px; 
        border: 1px solid #eee; 
        background: #fafafa; 
        font-size: 16px;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- RENDU AVEC ESPACEMENT MANUEL ---
# On simule le letter-spacing avec &nbsp; pour un centrage parfait sur tous les supports
st.markdown(f"""
    <div class="hanna-header">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
        <h1 class="hanna-title">H&nbsp;A&nbsp;N&nbsp;N&nbsp;A</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
    """, unsafe_allow_html=True)

user_input = st.text_input("", placeholder="Demander à HANNA", label_visibility="collapsed")
