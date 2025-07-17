import json
import os

def load_all_users():
    path = os.path.join(os.path.dirname(__file__), "../data/credentials.json")
    with open(path) as f:
        return json.load(f)
