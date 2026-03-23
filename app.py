# --- ARCHITECTURE CSS BDD7.2 (CENTRAGE ABSOLU) ---
st.markdown("""
    <style>
    /* On force le conteneur principal à être centré */
    .block-container { 
        padding-top: 2rem; 
        max-width: 500px; 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
    }
    
    .hanna-header { 
        width: 100%;
        display: flex; 
        flex-direction: column; 
        align-items: center; /* Centrage horizontal de tous les enfants */
        justify-content: center;
        text-align: center; 
        margin-bottom: 2rem; 
    }
    
    .hanna-logo-wrapper {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 15px;
    }

    .hanna-logo { 
        width: 110px; 
        height: auto;
        display: block; /* Évite les espacements résiduels en ligne */
    }
    
    .hanna-title { 
        font-family: 'Inter', sans-serif;
        font-weight: 200; 
        letter-spacing: 12px; 
        font-size: 42px; 
        color: #1A1A1A; 
        margin: 0;
        line-height: 1.1;
        /* Correction optique : le letter-spacing ajoute de l'espace à droite de la dernière lettre. 
           On ajoute un padding-left pour rééquilibrer le titre au centre exact. */
        padding-left: 12px; 
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

    /* Masquage des éléments natifs */
    #MainMenu, footer, header { visibility: hidden; height: 0; }
    </style>
""", unsafe_allow_html=True)

# --- RENDU DU HEADER ---
# Utilisation d'une structure de div imbriquées pour verrouiller le centrage
logo_html = f"""
    <div class="hanna-logo-wrapper">
        <img src="data:image/png;base64,{LOGO_B64}" class="hanna-logo">
    </div>
""" if LOGO_B64 else ""

st.markdown(f"""
    <div class="hanna-header">
        {logo_html}
        <h1 class="hanna-title">HANNA</h1>
        <p class="hanna-sub">Hybrid Adaptive Navigator & Network Assistant</p>
    </div>
""", unsafe_allow_html=True)
