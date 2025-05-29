
# agents/copybooster.py

from datetime import datetime
import uuid

PROMPT_COPYBOOSTER = """
====== AGENTE: CopyBooster ======
Versão: v2.2
Função Principal:
Subagente estratégico de copywriting ultra-avançado do GPT Mestre...
[Prompt completo aqui — omitido para brevidade]
"""

class CopyBooster:
    def __init__(self, llm):
        self.llm = llm

    def gerar_copy(self, texto_base, contexto, parametros=None):
        """
        Gera uma copy estratégica baseada em contexto, emoção e parâmetros táticos.
        """
        parametros = parametros or {}
        entrada = f"TEXTO BASE:\n{texto_base}\n\nCONTEXTO:\n{contexto}\n\nPARÂMETROS:\n{parametros}"
        prompt = PROMPT_COPYBOOSTER + "\n\nINSTRUÇÃO: Gere uma copy pronta para Shopee com foco direto na conversão. Não use introduções, nem diga que é um assistente. Use formato modular e sensorial.\n\n" + "\n\nInstrução: Responda diretamente com a copy final, sem introduções, sem se identificar como assistente.\n\n" + "\n\n" + entrada

        resposta_bruta = self.llm.predict(prompt)

        resultado = {
            "id_execucao": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "entrada": entrada,
            "resposta": resposta_bruta,
            "copy_dna": {
                "emoção": parametros.get("emoção"),
                "formato": parametros.get("formato"),
                "tipo": parametros.get("tipo"),
                "tom": parametros.get("tom"),
                "objetivo": parametros.get("objetivo"),
                "modo": parametros.get("modo")
            }
        }

        return resultado
