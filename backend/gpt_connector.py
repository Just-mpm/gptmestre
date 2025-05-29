
# backend/gpt_connector.py

import os
import requests
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

# Carrega variáveis de ambiente
load_dotenv()

# Chave OpenRouter fixa para ambiente controlado (segura em ambiente local)
OPENROUTER_API_KEY = "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"

def get_llm():
    return ChatOpenAI(
        model_name="mistralai/mistral-7b-instruct",
        temperature=0.4,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base="https://openrouter.ai/api/v1"
    )

def ask_carlos(prompt: str) -> str:
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "mistralai/mistral-7b-instruct",
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
