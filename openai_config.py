import os
import json

# Define the path for the config file in the user's home directory
CONFIG_FILE = os.path.expanduser("~/.text_expander_config.json")

def load_api_key():
    """Loads OpenAI API Key from the config file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            try:
                config = json.load(f)
                return config.get("OPENAI_API_KEY")
            except json.JSONDecodeError:
                print("⚠️ Error decoding JSON from config file.")
                return None
    else:
        return None

def save_api_key(api_key):
    """Saves OpenAI API Key to the config file."""
    config = {"OPENAI_API_KEY": api_key}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)
    print(f"✅ API Key saved to {CONFIG_FILE}")

def delete_api_key():
    """Deletes the OpenAI API Key from the config file."""
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)
        print(f"🗑️ API Key deleted from {CONFIG_FILE}")
    else:
        print("⚠️ No API Key found to delete.")
