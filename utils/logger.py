# utils/logger.py

import json
import os
from datetime import datetime

LOG_PATH = "logs/execucoes.json"

def registrar_execucao(id_copy, texto, tipo, emocao, nota, justificativa):
    nova_entrada = {
        "id": id_copy,
        "texto": texto,
        "tipo": tipo,
        "emocao": emocao,
        "nota": nota,
        "justificativa": justificativa,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(nova_entrada)

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
