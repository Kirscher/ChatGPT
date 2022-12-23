import requests

url = "https://api.openai.com/v1/models/chatbot"

payload = {
    "prompt": "Bonjour, comment ça va?",
    "model": "chatbot",
    "max_tokens": 64,
}

headers = {
    "Authorization": "Bearer API-KEY",
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())