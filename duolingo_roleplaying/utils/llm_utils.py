from ollama import chat
from duolingo_roleplaying.utils.sceanrio import Sceanrio_Desc

class LLMInteraction:
    def __init__(self, model="some-light-model", max_tokens=75):
        self.model = model
        self.max_tokens = max_tokens
        self.conversation_history = []  # Store LLM and user exchanges

    def generate_response(self, system_prompt, user_prompt, stream=False):
        """
        Generates a response from the LLM given the system and user prompts.
        Automatically adds the exchange to the conversation history.
        """
        # Format the input
        self._build_prompt(system_prompt, user_prompt)
        
        # Call the LLM API
        response = chat(
            model=self.model,
            messages=self.conversation_history,
            stream=stream,
            format = Sceanrio_Desc.model_json_schema()
        )

        try:
            scenario  = Sceanrio_Desc.model_validate_json(response.message.content)
            parsed_json = scenario.model_dump()
            
            # Log the exchange in the history
            assistant_message = {"role": "assistant", "content": parsed_json}
            self.conversation_history.append(assistant_message)

            # for _ in self.conversation_history:
            #     print("\n\n")
            #     print(_)

            return parsed_json 

        except Exception as e:
            assistant_message = {"role": "assistant", "content": {"error": str(e)}}
            self.conversation_history.append(assistant_message)
            return f"Error parsing scenario: {e}"
    

    def _build_prompt(self, system_prompt, user_prompt):
        """
        Builds the full prompt, incorporating conversation history.
        """
        # Add the system prompt to the history if it's the first message
        if not any(msg['role'] == 'system' for msg in self.conversation_history):
            self.conversation_history.append({"role": "system", "content": system_prompt})

        # Add the user's message to the conversation history
        self.conversation_history.append({"role": "user", "content": user_prompt})
        # print(self.conversation_history)

    def reset_conversation(self):
        """Resets the conversation history."""
        self.conversation_history = []

    def create_user_prompt_for_description(self, cefr_level, situation):
        id = situation["id"]
        category = situation["category"]
        description = situation["description"]
        return f'''Generate a scenario description (in ENGLISH) and opening dialog (in Spanish) for the following situation: "{description}" for a Spanish learner at CEFR level "{cefr_level}". Ensure the vocabulary and sentence structure match the CEFR level and the category of the situation: "{category}".'''