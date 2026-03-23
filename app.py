import streamlit as st

st.set_page_config(page_title="HANNA", layout="centered")
st.title("🛡️ HANNA Terminal")
st.subheader("Hybrid Adaptive Navigator & Network Assistant")
st.write("Le système est opérationnel. Prêt pour les instructions.")

user_input = st.text_input("Commande :")
if user_input:
    st.info(f"HANNA exécute : {user_input}")
  
