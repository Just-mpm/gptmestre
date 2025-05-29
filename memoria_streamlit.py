# memoria_streamlit_reflexor.py

import streamlit as st
from memory.vetorial import buscar_copies, salvar_copy
from agents.copybooster import melhorar_copy
from agents.reflexor import avaliar_resposta
from utils.logger import registrar_execucao
from datetime import datetime

st.set_page_config(page_title="Memória Vetorial — CopyBooster + Reflexor", layout="centered")
st.title("📦 Memória de Copys — Reutilização com Avaliação Inteligente")

query = st.text_input("🔍 Buscar por palavra-chave")
emocao_nova = st.selectbox("🎯 Aplicar nova emoção (opcional)", ["", "confiança", "surpresa", "urgência", "segurança", "alegria"])
tipo_saida = st.selectbox("Tipo de saída (para regenerar)", ["descricao", "titulo", "carrossel"])

if st.button("Buscar na Memória"):
    if not query.strip():
        st.warning("Digite um termo para buscar.")
    else:
        resultados = buscar_copies(query)
        docs = resultados.get("documents", [[]])[0]
        ids = resultados.get("ids", [[]])[0]

        if not docs:
            st.info("Nenhum resultado encontrado.")
        else:
            st.success(f"{len(docs)} resultado(s) encontrado(s).")

            for doc, id_ in zip(docs, ids):
                st.markdown(f"**📄 ID:** `{id_}`")
                st.code(doc, language='markdown')

                if emocao_nova:
                    nova, explicacao = melhorar_copy(doc, emocao_nova, tipo_saida)
                    st.markdown("**🔁 Variação com nova emoção:**")
                    st.code(nova, language='markdown')
                    st.caption(f"ℹ️ {explicacao}")

                    avaliacao = avaliar_resposta(nova)
                    nota = avaliacao.get("nota", 0)
                    justificativa = avaliacao.get("justificativa", "")

                    st.markdown(f"**🧠 Reflexor:** Nota {nota}/10")
                    st.caption(f"💬 {justificativa}")

                    if nota >= 8:
                        id_novo = f"{id_}_nova_{emocao_nova}_{datetime.now().strftime('%H%M%S')}"
                        salvar_copy(id_novo, nova)
                        registrar_execucao(id_novo, nova, tipo_saida, emocao_nova, nota, justificativa)
                        st.success("✅ Nova versão salva na memória e log de execuções.")

                st.markdown("---")
