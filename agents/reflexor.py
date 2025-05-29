# agents/reflexor.py

def avaliar_resposta(texto):
    """
    Avalia a resposta gerada e retorna uma nota e justificativa.
    Essa é uma versão simplificada para testes.
    """
    nota = 10 if len(texto) > 50 else 7
    justificativa = (
        "Texto longo, claro e persuasivo." if nota == 10
        else "Texto muito curto para avaliação robusta."
    )
    return {
        "nota": nota,
        "justificativa": justificativa
    }
