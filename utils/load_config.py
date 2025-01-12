import json
from models.config import Config


def load_config() -> Config:
    with open("config.json", "r") as file:
        return Config.from_dict(json.load(file))


config = load_config()
