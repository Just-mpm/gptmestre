# painel_execucao.py

import streamlit as st
import json
import os
from datetime import datetime

LOG_PATH = "logs/execucoes.json"

st.set_page_config(page_title="Painel de Execuções", layout="wide")
st.title("📊 Painel de Execuções — Copy + Reflexor")

# Função para carregar logs
def carregar_logs():
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

# Carregar execuções
execucoes = carregar_logs()

if not execucoes:
    st.info("Nenhuma execução registrada ainda.")
else:
    filtro_emocao = st.selectbox("Filtrar por emoção", [""] + sorted(list(set(e['emocao'] for e in execucoes))))
    exec_filtradas = [e for e in execucoes if e['emocao'] == filtro_emocao] if filtro_emocao else execucoes

    st.markdown(f"Total: **{len(exec_filtradas)}** execuções mostradas")

    for e in reversed(exec_filtradas):
        st.markdown(f"**🆔 {e['id']}** — {e['data']}")
        st.code(e['texto'], language='markdown')
        st.markdown(f"📌 Tipo: `{e['tipo']}` — Emoção: `{e['emocao']}`")
        st.markdown(f"🧠 Nota: **{e['nota']}** — {e['justificativa']}")
        st.markdown("---")
