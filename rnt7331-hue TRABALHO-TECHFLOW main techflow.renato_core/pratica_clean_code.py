
# TECHFLOW CORE - PRATICA CLEAN CODE

PONTOS_PRAZO_URGENTE = 2
PONTOS_PRAZO_PROXIMO = 1
LIMITE_URGENTE = 4
LIMITE_NORMAL = 2

PONTOS_PRIORIDADE = {
    "Alta": 3,
    "Media": 2,
    "Baixa": 1
}


def calcular_prioridade(prioridade, prazo_dias):
    """Calcula a classificação de prioridade de um chamado."""

    pontuacao = PONTOS_PRIORIDADE[prioridade]

    if prazo_dias <= 1:
        pontuacao += PONTOS_PRAZO_URGENTE
    elif prazo_dias <= 3:
        pontuacao += PONTOS_PRAZO_PROXIMO

    if pontuacao >= LIMITE_URGENTE:
        classificacao = "URGENTE"
    elif pontuacao >= LIMITE_NORMAL:
        classificacao = "NORMAL"
    else:
        classificacao = "BAIXA"

    return classificacao, pontuacao


def main():
    """Executa o programa de cálculo de prioridades."""

    for numero in range(3):
        print(f"\n--- CHAMADO {numero + 1} ---")

        prioridade = input(
            "Prioridade (Alta, Media, Baixa): "
        ).capitalize()

        if prioridade not in PONTOS_PRIORIDADE:
            print("Prioridade inválida!")
            continue

        try:
            prazo_dias = int(input("Prazo em dias: "))

            if prazo_dias < 0:
                print("O prazo não pode ser negativo!")
                continue

        except ValueError:
            print("Digite um número inteiro válido!")
            continue

        classificacao, pontuacao = calcular_prioridade(
            prioridade, prazo_dias
        )

        print(f"Prioridade: {classificacao}")
        print(f"Pontuação: {pontuacao}")


if __name__ == "__main__":
    main()
