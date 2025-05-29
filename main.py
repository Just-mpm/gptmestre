# main.py

import streamlit as st
from backend.gpt_connector import ask_carlos
from agents.reflexor import audit_response

st.set_page_config(page_title="GPT Mestre Autônomo", layout="centered")

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

    # Chama o agente Carlos
    with st.chat_message("assistant"):
        response = ask_carlos(user_input)
        st.markdown(response)

        # Chama o Reflexor para avaliar a resposta
        reflexor_output = audit_response(user_input, response)
        st.markdown(f"🧠 **Reflexor:** {reflexor_output}")

    # Salva a resposta do Carlos
    st.session_state.messages.append({"role": "assistant", "content": response})
