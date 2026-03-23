import streamlit as st
from datetime import datetime
import os
import base64

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"
PROJECT_NAME = "Projet HANNA"

st.set_page_config(page_title="HANNA", layout="centered")

# --- FONCTION POUR LE LOGO (FORCE LE CENTRAGE) ---
def display_logo(file_path, width_percent=50):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; width: 100%; margin-bottom: 10px;">
                <img src="data:image/png;base64,{data}" style="width: {width_percent}%; height: auto;">
            </div>
            """,
            unsafe_allow_html=True
        )

# --- STYLE DESIGN BLANC & COMPACT ---
st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    .stApp { background-color: #ffffff; color: #1e1e1e; font-family: 'Inter', sans-serif; }
    
    .hanna-main-title { 
        font-weight: 200; 
        letter-spacing: 10px; 
        text-transform: uppercase; 
        font-size: 28px; 
        text-align: center; 
        color: #000000;
        margin-top: 10px;
        margin-bottom: 2px;
    }
    
    .hanna-sub-title {
        font-weight: 300;
        font-size: 10px;
        text-align: center;
        color: #999999;
        letter-spacing: 1.5px;
        margin-bottom: 25px;
        text-transform: uppercase;
    }

    div.stTextInput > div > div > input {
        text-align: center;
        background-color: #fcfcfc !important;
        border: 1px solid #f0f0f0 !important;
        border-radius: 4px !important;
        height: 40px !important;
    }
    
    .stButton > button {
        width: 100% !important;
        background-color: #000000 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 400 !important;
        letter-spacing: 2px !important;
        height: 40px !important;
        border-radius: 4px !important;
        text-transform: uppercase !important;
        font-size: 12px !important;
    }
    .stButton > button:hover { background-color: #333333 !important; }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.write("")
    # Appel de la fonction de centrage forcé
    display_logo(LOGO_FILE, 50)

    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hanna-sub-title">{PROJECT_NAME} | ACCÈS SÉCURISÉ</div>', unsafe_allow_html=True)
    
    pwd = st.text_input("Code", type="password", label_visibility="collapsed", placeholder="CODE D'ACCÈS")
    
    if st.button("ENTRER"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Accès refusé.")
    st.stop()

# --- INTERFACE PRINCIPALE ---
display_logo(LOGO_FILE, 50)

st.markdown(f'<div class="hanna-main-title" style="font-size:22px; letter-spacing:4px; margin-top:0px;">{PROJECT_NAME}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="hanna-sub-title" style="margin-bottom:10px;">SYSTÈME OPÉRATIONNEL | {datetime.now().strftime("%H:%M")}</div>', unsafe_allow_html=True)

st.divider()

if 'notes' not in st.session_state:
    st.session_state.notes = []

new_note = st.text_input("CAPTURE :", label_visibility="collapsed", placeholder="Saisir une information...")
if st.button("SYNCHRONISER"):
    if new_note:
        st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
        st.rerun()

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

st.write("")
if st.button("QUITTER LA SESSION"):
    st.session_state.auth = False
    st.rerun()
