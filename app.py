import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

st.set_page_config(page_title="HANNA", layout="centered")

# --- STYLE ÉLÉGANT & CENTRAGE ABSOLU ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #333333; font-family: 'Inter', sans-serif; }
    
    .stImage {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }
    .stImage > div {
        display: flex !important;
        justify-content: center !important;
    }
    
    .hanna-main-title { 
        font-weight: 200; 
        letter-spacing: 12px; 
        text-transform: uppercase; 
        font-size: clamp(24px, 5vw, 32px); 
        text-align: center; 
        color: #000000;
        margin-top: 20px;
        margin-bottom: 5px;
        width: 100%;
    }
    
    .hanna-sub-title {
        font-weight: 300;
        font-size: clamp(10px, 3vw, 11px);
        text-align: center;
        color: #999999;
        letter-spacing: 1.5px;
        margin-bottom: 40px;
        text-transform: uppercase;
        width: 100%;
    }

    div.stTextInput > div > div > input {
        text-align: center;
        border: 1px solid #eeeeee !important;
        border-radius: 4px !important;
        height: 45px;
    }
    
    .stButton > button {
        width: 100%;
        background-color: #000000;
        color: #ffffff;
        border: none;
        font-weight: 300;
        letter-spacing: 2px;
        height: 45px;
        border-radius: 4px;
    }
    .stButton > button:hover { background-color: #222222; }

    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.write("")
    st.write("")
    
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=160)
    else:
        st.markdown("<h1 style='text-align:center;'>🛡️</h1>", unsafe_allow_html=True)

    st.markdown('<div class="hanna-main-title">HANNA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-sub-title">Hybrid Adaptive Navigator & Network Assistant</div>', unsafe_allow_html=True)
    
    pwd = st.text_input("ACCESS CODE", type="password", label_visibility="collapsed", placeholder="ENTER ACCESS CODE")
    
    if st.button("AUTHORIZE"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Invalid credentials.")
    st.stop()

# --- INTERFACE PRINCIPALE ---
st.markdown('<div style="font-weight:200; letter-spacing:5px; font-size:20px;">HANNA</div>', unsafe_allow_html=True)
st.caption(f"Network Assistant | System Ready | {datetime.now().strftime('%H:%M')}")
st.divider()

if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("NEW DATA ENTRY", expanded=True):
    new_note = st.text_input("Capture:", key="main_input", placeholder="...")
    if st.button("SYNCHRONIZE"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
            st.success("Entry recorded.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

if st.button("TERMINATE SESSION"):
    st.session_state.auth = False
    st.rerun()
