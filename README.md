# GPT Mestre Autônomo — Base com Integração Telegram

Projeto completo de IA autônoma com execução local e agentes inteligentes inspirados em DeepAgent e Manus, utilizando GPT-4.

## 🔧 Principais recursos
- Integração com Telegram Bot
- Execução de agentes reais (CopyBooster, Reflexor, DeepAgent)
- Memória vetorial (ChromaDB)
- Painel local com Streamlit
- Suporte a comandos inteligentes no chat

## 📁 Estrutura
```
gpt_mestre_autonomo_base/
├── agents/
├── backend/
├── integrations/
├── memory/
├── logs/
├── main.py
├── requirements.txt
```

## 🚀 Como rodar
```bash
pip install -r requirements.txt
python main.py
```

## 📬 Comandos do Telegram
- `/copy` → Executa CopyBooster
- `/reflexor` → Audita resposta
- `/deep` → Ativa DeepAgent

---

Projeto criado por Matheus Pimenta.