
# main.py

import streamlit as st
from backend.gpt_connector import ask_carlos, get_llm
from agents.reflexor import Reflexor
from agents.copybooster import CopyBooster
from agents.deepagent import DeepAgent

st.set_page_config(page_title="GPT Mestre Autônomo", layout="centered")

# Inicialização dos agentes com o LLM
llm = get_llm()
reflexor = Reflexor(llm)
copybooster = CopyBooster(llm)
deepagent = DeepAgent(llm)

# Interface visual
st.title("🤖 Carlos Executor — GPT Mestre Autônomo")

# Histórico de mensagens (memória temporária)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens antigas
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Campo de entrada do usuário
user_input = st.chat_input("Fale com o Carlos...")

if user_input:
    # Salva entrada do usuário
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Exibe a mensagem do usuário
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        # Chama o Carlos
        response = ask_carlos(user_input)
        st.markdown(response)

        # Auditoria com Reflexor
        audit = reflexor.avaliar_resposta(response)
        st.markdown(f"🧠 **Reflexor:** Nota {audit['nota']}/10 — {audit['diagnostico']}")

        # CopyBooster (simulação com parâmetros)
        copy = copybooster.gerar_copy(
            texto_base=user_input,
            contexto="Conversão para Shopee",
            parametros={"emoção": "confiança", "formato": "shopee", "tipo": "modular"}
        )
        st.markdown("✍️ **CopyBooster (simulação):**")
        st.markdown(copy["resposta"])

        # DeepAgent (simulação rápida)
        insight = deepagent.investigar(user_input, tipo="produto", objetivo="concorrência", modo="rápido")
        st.markdown("🌐 **DeepAgent (simulação):**")
        st.markdown(insight["resposta"])

    # Salva a resposta do Carlos
    st.session_state.messages.append({"role": "assistant", "content": response})
