
import streamlit as st
from fba_assistant.utils.memory import get_last_interactions
from fba_assistant.utils.multiagent_backend import run_fba_crew

from fba_assistant.utils.memory import get_last_interactions, init_memory
init_memory()


st.set_page_config(page_title="FBA Crew Assistant")
st.title("🧠 Amazon FBA Multi-Agent Orchestrateur (AutoGen)")

user_input = st.text_area("💬 Décris ton idée de produit ou ton besoin :", "")

if st.button("Lancer l’analyse IA"):
    with st.spinner("Analyse complète par les agents..."):
        result = run_fba_crew(user_input)
        st.text_area("📋 Résultat combiné des agents :", value=result, height=400)

st.subheader("🕑 Historique des interactions")
for question, response in get_last_interactions():
    st.markdown(f"**🗨️ {question}**")
    st.markdown(f"```{response}```")
