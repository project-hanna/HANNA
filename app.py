import streamlit as st
from datetime import datetime
import os

# --- CONFIGURATION SÉCURISÉE ---
PASSWORD_SYSTEM = "mtt.mallee@gmail.C94"
LOGO_FILE = "logo2.png"

st.set_page_config(page_title="HANNA Terminal", layout="centered")

# --- STYLE ÉLÉGANT (LIGHT & REFINED) ---
st.markdown("""
    <style>
    /* Fond blanc pur */
    .stApp { background-color: #ffffff; color: #333333; font-family: 'Inter', 'Segoe UI', Helvetica, sans-serif; }
    
    /* Centrage global du logo */
    .stImage { display: flex; justify-content: center; padding-bottom: 10px; }
    
    /* Typographie HANNA : Fine et élégante */
    .hanna-title { 
        font-weight: 200; 
        letter-spacing: 4px; 
        text-transform: uppercase; 
        font-size: 28px; 
        text-align: center; 
        color: #1a1a1a;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    
    .hanna-subtitle {
        font-weight: 300;
        font-size: 12px;
        text-align: center;
        color: #888888;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }

    /* Champs de saisie discrets */
    input { 
        background-color: #fcfcfc !important; 
        color: #333 !important; 
        border: 1px solid #eeeeee !important; 
        border-radius: 4px !important;
        text-align: center;
    }
    
    /* Bouton minimaliste noir */
    .stButton>button { 
        width: 100%; 
        background-color: #000000; 
        color: #ffffff; 
        border: none; 
        font-weight: 300; 
        letter-spacing: 1px;
        height: 45px;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #333333; color: #ffffff; }

    /* Suppression des éléments Streamlit parasites */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'ACCÈS ---
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.write("")
    st.write("")
    
    # Logo au centre
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=140)
    else:
        st.markdown("<h1 style='text-align:center;'>🛡️</h1>", unsafe_allow_html=True)

    # Titre élégant
    st.markdown('<div class="hanna-title">HANNA TERMINAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="hanna-subtitle">HYBRID ADAPTIVE NAVIGATOR</div>', unsafe_allow_html=True)
    
    pwd = st.text_input("AUTHORIZATION CODE", type="password", label_visibility="collapsed", placeholder="Enter Code")
    
    if st.button("UNLOCK SYSTEM"):
        if pwd == PASSWORD_SYSTEM:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Access Denied.")
    st.stop()

# --- INTERFACE PRINCIPALE (DÉVERROUILLÉE) ---
st.markdown('<div class="hanna-title" style="text-align:left; font-size:20px;">HANNA TERMINAL</div>', unsafe_allow_html=True)
st.caption(f"Status: Operational | {datetime.now().strftime('%H:%M')}")

st.divider()

if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.expander("NEW ENTRY", expanded=True):
    new_note = st.text_input("Data:", key="main_input", placeholder="..." )
    if st.button("COMMIT TO MEMORY"):
        if new_note:
            st.session_state.notes.append(f"[{datetime.now().strftime('%H:%M')}] {new_note}")
            st.success("Synchronized.")

if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)

if st.button("LOCK SYSTEM"):
    st.session_state.auth = False
    st.rerun()
