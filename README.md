# Duolingo Clone - GenAI Language Learning Tutor 

A project in development. This project is a personal initiative to build a GenAI-powered language learning application inspired by Duolingo Max. The app uses Generative AI to provide roleplaying scenarios and detailed feedback for language learners. The backend leverages the LLAMA3 model via the Ollama API, while the frontend is built with Streamlit for simplicity and ease of use. The project is modular to allow incremental development and testing.

### Features:
1. Roleplaying Scenarios: Engage in realistic conversational scenarios to practice language skills.
2. Feedback and Analysis: Understand why your answers were incorrect and get constructive feedback.
3. Vocabulary Support: Suggestions for words and phrases tailored to the user's CEFR level.
4. Flashcards: Generate flashcards from conversations for better retention.

### Development Plan

1. Backend Setup:
    1. Set up Ollama: Install and configure the Ollama API locally or on a server.
    2. Install LLAMA3 Model: Ensure the LLAMA3 model is operational.
    3. Test API Integration: Create a script to test LLAMA3 via the Ollama API. Verify functionality by sending basic prompts and checking responses.


2. Logic Design
    1. User Input and Customization: Prompt users for their CEFR level (e.g., A1, B2) to set difficulty.
    2. Suggest 3 scenarios to choose from (e.g., ordering food, introducing oneself).
    3. Conversation Flow: Provide vocabulary and phrase suggestions before starting the conversation.
    4. Store user responses and maintain a dialogue history.
    5. Feedback and Flashcards: Analyze the user's responses to generate constructive feedback.
    6. Create flashcards for key takeaways and areas of improvement.

3. Frontend Skeleton
    1. Streamlit Integration: Build a basic Streamlit app to serve as the frontend.
    2. UI Components: Design placeholders for user input, scenario selection, and feedback display.

4. Incremental Integration - Step-by-Step Integration:

1. Connect the frontend with the backend.
2. Test individual modules (e.g., Ollama API, CEFR prompts, dialogue handling).
3. Full Workflow Testing: Validate the app's workflow end-to-end.

Refinement: Optimize prompts, UI, and feedback generation based on testing.

### Project Structure
```bash
language_learning_app/
├── backend/
│   ├── ollama_api.py      # Ollama API interaction functions
│   ├── language_model.py  # Logic for interacting with the language model
│   ├── scenarios.py       # Scenario definitions and data
│   ├── analysis.py        # Answer analysis and feedback generation
│   └── utils.py           # Utility functions (e.g., data loading, CEFR mapping)
├── frontend/
│   └── app.py             # Streamlit UI code
├── data/
│   └── scenarios.json     # Scenario data (or use a database)
└── tests/
    └── test_ollama_api.py # Test script for Ollama API integration
```
###  Setup Instructions

#### Prerequisites

1. Python 3.8+
2. Ollama API: Follow the Ollama Installation Guide to install and configure the API.
3. Streamlit: Install Streamlit via pip.

### Installation Steps

1. Clone the Repository: 
```bash
git clone https://github.com/your-username/genai-language-tutor.git
cd genai-language-tutor
```

2. Set Up Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies:
```bash
pip install -r requirements.txt
```

Run the Test Script:
1. On linux: 
```bash
sudo systemctl stop ollama
ollama serve
```
2. Test the Ollama API setup using:
```bash
python tests/test_ollama_api.py
```
Example Output from Test Script

Successful API Call:

Testing Ollama API...
✅ API call successful!
Response: {
  "choices": [
    { "text": "The capital of Spain is Madrid." }
  ]
}

Failed API Call:

Testing Ollama API...
❌ API call failed with status code: 404
Response content: {"error": "Model not found"}