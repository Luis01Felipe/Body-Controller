import mediapipe as mp


def capturar_movimentos():
    # Inicializar Mediapipe
    movimentos = {
        "cabeca": "neutra",  # esquerda, direita, cima, baixo
        "mao_direita": "neutra",  # esquerda, direita, cima, baixo
        "queixo": "neutra",  # rápido para cima, neutra
    }

    # Simulação de movimentos (substituir com código real de detecção)
    # Aqui você deve capturar o movimento da cabeça, mão e gestos
    movimentos["cabeca"] = "cima"
    movimentos["mao_direita"] = "direita"
    movimentos["queixo"] = "rápido para cima"

    return movimentos
