import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def test_ollama_api():
    prompt = "Tell me the captial of India?"
    payload = {
        "model" : MODEL_NAME,
        "prompt" : prompt,
        "stream" : False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        if response.status_code == 200:
            print("API call successful!")
            data = response.json()["response"]
            print("Response:", json.dumps(data, indent=2))
        else:
            print("API call failed with status code:", response.status_code)
            print("Response content:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error connecting to Ollama API:", str(e), print(response.text))
    
if __name__ == "__main__":
    print("Testing Ollama API...")
    test_ollama_api()