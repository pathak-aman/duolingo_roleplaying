import os
import json
import random

from duolingo_roleplaying.constants import K_SITUATIONS

# Create dynamic filepath to situations.json
SITUATIONS_PATH = os.path.join(os.path.dirname(__file__), "situations.json")
# print(SITUATIONS_PATH)

def load_situation_json():
    """
    Load and return the situations data from the JSON file.
    """
    try:
        with open(SITUATIONS_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find {SITUATIONS_PATH}")
    except json.JSONDecodeError:
        raise ValueError(f"Malformed JSON in {SITUATIONS_PATH}")
    
def get_situation_by_id(situation_id):
    try:
        situations = load_situation_json()
        return next((s for s in situations if s["id"] == situation_id), None)
    except Exception as e:
        print(str(e))


def get_K_random_situation():
    """
    Returns K random situations from the JSON file
    """
    try:
        situations = load_situation_json()
        return random.sample(situations,K_SITUATIONS)
    except Exception as e:
        print(str(e))
