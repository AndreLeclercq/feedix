from mistralai import Mistral
import os
from dotenv import load_dotenv

load_dotenv()

def generate_summary(value):
    api_key = os.getenv("MISTRAL_API_KEY")
    model = "mistral-small-latest"
    client = Mistral(api_key=api_key)

    response = client.chat.complete(
        model = model,
        messages = [{
            "role": "user",
            "content": value,
        },]
    )

    return response.choices[0].message.content
