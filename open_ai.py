# import openai_secret_manager
# import openai
import requests

API_KEY = "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"
ORGANIZATION_ID = "org-C2kvhijI4C3q2iOFpfdQxan9"

# Get API key
# secrets = openai.get_secrets("openai")
# api_key = secrets["api_key"]

# Ask user for input
question = input("What is your question? ")

# Send request to API
response = requests.post(
    "https://api.openai.com/v1/engines/davinci-codex/completions",
    headers={"Content-Type": "application/json",

             "Authorization": f"Bearer {API_KEY}"},
    json={
        "prompt": question,
        "temperature": 0.5,
    },
)

# Print response
z = response.json()
print(response.json()["choices"][0]["text"])
