import os
import requests

api_key = os.getenv("OPENROUTER_API_KEY").strip()

print("API key loaded:", api_key is not None)

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
    "messages": [
        {
            "role": "user",
            "content": "Reply with exactly: OpenRouter works"
        }
    ]
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=data
)

print(response.status_code)
print(response.text)