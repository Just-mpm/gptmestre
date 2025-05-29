# test_streamlit_reflexor.py

import streamlit as st
from agents.copybooster import melhorar_copy
from memory.vetorial import salvar_copy
from agents.reflexor import avaliar_resposta
from utils.logger import registrar_execucao
from datetime import datetime

st.set_page_config(page_title="CopyBooster + Reflexor", layout="centered")
st.title("CopyBooster v1.0 + Reflexor — Teste de Copy Emocional")

texto_base = st.text_area("Texto base", height=150)
emocao = st.selectbox("Emoção desejada", ["confiança", "surpresa", "urgência", "segurança", "alegria"])
tipo = st.selectbox("Tipo de saída", ["descricao", "titulo", "carrossel"])

if st.button("Gerar Copy"):
    if not texto_base.strip():
        st.warning("Por favor, preencha o texto base.")
    else:
        nova_copy, explicacao = melhorar_copy(texto_base, emocao=emocao, tipo=tipo)
        st.subheader("Resultado Gerado")
        st.code(nova_copy, language='markdown')
        st.caption(f"ℹ️ {explicacao}")

        avaliacao = avaliar_resposta(nova_copy)
        nota = avaliacao.get("nota", 0)
        justificativa = avaliacao.get("justificativa", "Sem justificativa.")

        st.markdown(f"**Reflexor:** Nota {nota}/10")
        st.caption(f"🧠 {justificativa}")

        if nota >= 8:
            id_copy = "copy_" + datetime.now().strftime("%Y%m%d%H%M%S")
            salvar_copy(id_copy, nova_copy)
            registrar_execucao(id_copy, nova_copy, tipo, emocao, nota, justificativa)
            st.success("✅ Copy salva na memória vetorial e log de execuções.")
        else:
            st.warning("⚠️ Copy não salva: nota inferior a 8.")
