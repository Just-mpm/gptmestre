# agents/copybooster.py

def melhorar_copy(texto_base, emocao='confiança', tipo='descricao'):
    """
    Gera uma versão reescrita do texto com base na emoção desejada.
    """
    explicacao = f"Aplicando tom emocional de '{emocao}' para tipo '{tipo}'."
    nova_versao = f"[{emocao.upper()} - {tipo}] {texto_base}"
    return nova_versao, explicacao
