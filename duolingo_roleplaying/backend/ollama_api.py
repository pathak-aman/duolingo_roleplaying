from duolingo_roleplaying.situations_module.situation_handler import load_situation_json, get_K_random_situation, get_situation_by_id
from duolingo_roleplaying.constants import USER_CHOICE, C1_CEFR_LEVEL, A1_CEFR_LEVEL, DESC_GENERATING_MODEL,DESC_GENERATING_SYSTEM_PROMPT
from duolingo_roleplaying.utils.llm_utils import LLMInteraction

# print(load_situation_json())
# print(get_situation_by_id("daily_life_07"))

# Later would be replaced by Streamlit
situation = get_K_random_situation()[USER_CHOICE]

# Get description from LLM:

llm_interaction = LLMInteraction(model=DESC_GENERATING_MODEL, )
cerf_level = C1_CEFR_LEVEL
user_prompt = llm_interaction.create_user_prompt_for_description(cerf_level, situation)
system_prompt = DESC_GENERATING_SYSTEM_PROMPT
response_description = llm_interaction.generate_response(system_prompt, user_prompt)

print(response_description)