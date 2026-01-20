import os
import requests
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "x-ai/grok-code-fast-1"
def call_model(prompt: str):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ],
        },
    )
    return response.json()
if __name__ == "__main__":
    result = call_model("Provide a bullet-point summary of cloud-native systems.")
    response_text = result["choices"][0]["message"]["content"]
    print(response_text)
    print(f"Response length: {len(response_text)}")
