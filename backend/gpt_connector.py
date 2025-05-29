# backend/gpt_connector.py

import requests

def ask_carlos(prompt: str) -> str:
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        }

        body = {
            "model": "mistralai/mistral-7b-instruct",  # Pode trocar por 'anthropic/claude-instant-v1' ou outro suportado
            "messages": [
                {"role": "system", "content": "Você é Carlos, o agente executor do GPT Mestre. Sempre responda com clareza, estratégia e lógica, como um assistente autônomo profissional."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Erro ao se comunicar com Carlos via OpenRouter: {str(e)}"
