# --- CSS ARCHITECTURE BDD7.2 (CENTRAGE OPTIMISÉ) ---
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; max-width: 500px; }
    .stApp { background-color: #FFFFFF; }
    
    /* Conteneur Flexbox pour centrer verticalement et horizontalement */
    .hanna-header { 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center;
        text-align: center; 
        margin-bottom: 2rem; 
    }
    
    .hanna-logo-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 10px;
    }

    .hanna-logo { 
        width: 100px; 
        height: auto;
        display: block;
    }
    
    .hanna-title { 
        font-family: 'Inter', sans-serif;
        font-weight: 200; 
        letter-spacing: 12px; 
        font-size: 42px; 
        color: #1A1A1A; 
        margin: 0;
        line-height: 1.1;
        padding-left: 12px; /* Pour compenser le letter-spacing à droite et centrer optiquement */
    }
    
    .hanna-sub { 
        font-family: 'Inter', sans-serif;
        font-weight: 300; 
        font-size: 9px; 
        color: #999; 
        letter-spacing: 1.5px; 
        text-transform: uppercase;
        margin-top: 8px;
    }

    /* Reste du CSS... */
    #MainMenu, footer, header { visibility: hidden; height: 0; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER HTML ---
# On s'assure que le logo est bien dans sa div de centrage
logo_html = f"<div class='hanna-logo-container'><img src='data:image/png;base64,{LOGO_B64}' class='hanna-logo'></div>" if LOGO_B64 else ""

st.markdown(f"""
    <div class="hanna-header">
        {logo_html}
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)
