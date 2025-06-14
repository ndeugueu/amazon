
import os
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from utils.memory import save_interaction

# Récupération de la clé API via variable d'environnement
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm_conf = {
    "model": "gpt-4",
    "api_key": OPENAI_API_KEY
}

product_hunter = AssistantAgent(
    name="ProductHunterAgent",
    llm_config=llm_conf,
    system_message="""Tu es un expert en recherche de produits Amazon FBA. Ta tâche est d’identifier des produits rentables avec ces critères : 
- Prix de vente entre 20€ et 70€
- Poids < 1kg
- Moins de 1000 avis
- Forte demande (500+ ventes/mois)
- Produit améliorable (design, packaging...)
- Pas de marque dominante

Donne des suggestions concrètes et argumentées."""
)

sourcing_agent = AssistantAgent(
    name="SourcingAgent",
    llm_config=llm_conf,
    system_message="Tu es un expert en sourcing de produits Alibaba. Fournis des recommandations de fournisseurs et de coûts estimés selon les idées du ProductHunter."
)

listing_agent = AssistantAgent(
    name="ListingAgent",
    llm_config=llm_conf,
    system_message="Tu es expert Amazon SEO. Rédige des titres, puces et descriptions optimisés pour le référencement."
)

launch_agent = AssistantAgent(
    name="LaunchPlannerAgent",
    llm_config=llm_conf,
    system_message="Tu es un spécialiste du lancement de produits sur Amazon. Tu proposes une stratégie incluant : offre de lancement, récolte d’avis, campagne PPC, visuels."
)

user = UserProxyAgent(
    name="Utilisateur",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False}
)

def run_fba_crew(user_input):
    groupchat = GroupChat(
        agents=[user, product_hunter, sourcing_agent, listing_agent, launch_agent],
        messages=[],
        max_round=4
    )
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_conf)
    result = user.initiate_chat(manager, message=user_input)
    save_interaction(user_input, str(result))
    return result
