
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from utils.memory import save_interaction

product_hunter = AssistantAgent(
    name="ProductHunterAgent",
    llm_config={"model": "gpt-4", "api_key": "sk-REPLACE_ME"},
    system_message="""Tu es un expert en recherche de produits Amazon FBA..."""
)

sourcing_agent = AssistantAgent(
    name="SourcingAgent",
    llm_config={"model": "gpt-4", "api_key": "sk-REPLACE_ME"},
    system_message="Tu es un expert en sourcing Alibaba..."
)

listing_agent = AssistantAgent(
    name="ListingAgent",
    llm_config={"model": "gpt-4", "api_key": "sk-REPLACE_ME"},
    system_message="Tu es un expert en création de fiches produit Amazon..."
)

launch_agent = AssistantAgent(
    name="LaunchPlannerAgent",
    llm_config={"model": "gpt-4", "api_key": "sk-REPLACE_ME"},
    system_message="Tu es un expert en lancement de produits Amazon..."
)

user = UserProxyAgent(name="Utilisateur", human_input_mode="NEVER")

def run_fba_crew(user_input):
    groupchat = GroupChat(
        agents=[user, product_hunter, sourcing_agent, listing_agent, launch_agent],
        messages=[], max_round=4
    )
    manager = GroupChatManager(groupchat=groupchat, llm_config={"model": "gpt-4", "api_key": "sk-REPLACE_ME"})
    result = user.initiate_chat(manager, message=user_input)
    save_interaction(user_input, result)
    return result
