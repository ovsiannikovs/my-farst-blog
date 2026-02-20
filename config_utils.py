import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
CONFIG_ENCODING = "utf8"

def get_config():
    with open(CONFIG_PATH, "rt", encoding=CONFIG_ENCODING) as f:
        text = f.read()
        return json.loads(text)