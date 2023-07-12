import os
import requests
from dotenv import load_dotenv


def get_random_word() -> dict:
    """
    Get random word with pronunciation from RapidApi

    API Response:
    {
        "definition": "Plain glossy silk ",
        "pronunciation":"Lutestrink",
        "word": :"Lutestring",
    }
    """

    load_dotenv()

    url = os.getenv("API_URL")
    headers = {
        "X-RapidAPI-Key": os.getenv("X_RAPIDAPI_KEY"),
        "X-RapidAPI-Host": os.getenv("X_RAPIDAPI_HOST"),
    }

    response = requests.get(url, headers=headers)

    word_obj = response.json()[0]

    return word_obj
