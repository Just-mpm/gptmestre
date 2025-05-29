
# agents/reflexor.py

from datetime import datetime
import uuid

PROMPT_REFLEXOR = """
Nome do Agente: Reflexor
Versão: v1.5
Função Principal:
Auditor lógico e estratégico das respostas geradas em qualquer tarefa crítica do GPT Mestre...
[Prompt completo aqui — omitido para brevidade]
"""

class Reflexor:
    def __init__(self, llm):
        self.llm = llm
        self.memoria = {
            "ultima_nota": None,
            "ultimo_setor": None,
            "ultimo_erro": None
        }

    def avaliar_resposta(self, entrada):
        prompt = PROMPT_REFLEXOR + "\n\nINSTRUÇÃO: Responda com um JSON contendo os campos solicitados. Não inclua texto explicativo.\n\nENTRADA:\n" + entrada
        resposta_bruta = self.llm.predict(prompt)

        # Aqui simulamos um parse da resposta — o ideal é que o output seja um JSON formatado
        resultado = {
            "id_execucao": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "entrada": entrada,
            "resposta_bruta": resposta_bruta,
            "nota": None,
            "justificativa": None,
            "fator_decisivo": None,
            "fator_incerteza": None,
            "erro_classificacao": None,
            "severidade": None,
            "acao_recomendada": None,
            "diagnostico": None,
            "aprendizado": None,
            "sugestao_prompt": None,
            "red_flag": False
        }

        
        # Parsing simples da resposta para capturar nota e diagnóstico
        for line in resposta_bruta.split("\n"):
            if "Nota de Confiança" in line:
                try:
                    resultado["nota"] = float(line.split(":")[1].split("/")[0].strip())
                except: pass
            elif "Diagnóstico" in line:
                resultado["diagnostico"] = line.split(":")[1].strip()

        # Armazenar memória básica temporária
        self.memoria["ultima_nota"] = resultado["nota"]
        self.memoria["ultimo_erro"] = resultado["erro_classificacao"]

        return resultado
