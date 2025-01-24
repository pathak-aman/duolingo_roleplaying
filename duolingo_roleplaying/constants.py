K_SITUATIONS = 3
A1_CEFR_LEVEL = "A1"
C1_CEFR_LEVEL = "C1"

USER_CHOICE = 1

DESC_MAX_OUTPUT_TOKEN = 100
DESC_GENERATING_MODEL = "llama3.2:1b"
DESC_GENERATING_TEMP = 0.8
DESC_GENERATING_SYSTEM_PROMPT ='''"You are an AI tutor generating creative CEFR-aligned scenarios for language learners."
"Always return your output as a JSON object with these fields: "
"- 'description': A detailed 2-3 sentence scenario description in ENGLISH."
"- 'first_dialog': A small opening question (max 8 words) engaging interaction in the scenario in SPANISH."
"The language should be appropriate for the CEFR level)"
"Follow the format exactly and do not include additional text or explanations.'''
