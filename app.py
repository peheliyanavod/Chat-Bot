import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("API_KEY")
email = os.getenv("EMAIL")

while True:
    question = input("You : ")

    if question.lower() in ["exit", "quit"]:
        break

    url = "https://apiswitch.leapcell.app/chat"
    params = {
        "question": question,
        "model": "gpt-4.1-nano",
        "stream": "false",
        "apikey": api_key,
        "email": email
    }
    
    response = requests.get(url, params=params)
    print(response.json().get("answer"))