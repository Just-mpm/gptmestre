# agents/deepagent.py

from datetime import datetime

def investigar(texto, tipo='produto'):
    """
    Versão inicial do DeepAgent. Apenas simula uma análise estratégica.
    """
    data_execucao = datetime.now().strftime("%Y-%m-%d %H:%M")
    if tipo == 'produto':
        return f"[{data_execucao}] Análise Estratégica de Produto: {texto}"
    else:
        return f"[{data_execucao}] Investigação Geral: {texto}"
