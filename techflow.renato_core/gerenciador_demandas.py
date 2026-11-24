
# TECHFLOW CORE - GERENCIADOR DE DEMANDAS

demandas = []


def cadastrar_demanda():
    """Cadastra uma nova demanda no sistema."""

    print("\n=== CADASTRAR DEMANDA ===")

    identificador = input("ID da demanda: ").strip()

    if not identificador:
        print("Erro: o ID não pode ficar vazio!")
        return

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Erro: este ID já está cadastrado!")
            return

    titulo = input("Título: ").strip()
    solicitante = input("Solicitante: ").strip()
    prioridade = input("Prioridade (Alta, Media, Baixa): ").strip().capitalize()
    cep = input("CEP: ").strip()
    cidade = input("Cidade: ").strip()

    campos = [titulo, solicitante, prioridade, cep, cidade]

    if any(not campo for campo in campos):
        print("Erro: todos os campos são obrigatórios!")
        return

    if prioridade not in ["Alta", "Media", "Baixa"]:
        print("Erro: prioridade inválida!")
        return

    nova_demanda = {
        "id": identificador,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "cidade": cidade,
        "status": "Pendente"
    }

    demandas.append(nova_demanda)

    print("Demanda cadastrada com sucesso!")


def listar_demandas():
    """Exibe todas as demandas cadastradas."""

    print("\n=== LISTA DE DEMANDAS ===")

    if not demandas:
        print("Nenhuma demanda cadastrada.")
        return

    for demanda in demandas:
        print("-" * 35)

        for campo, valor in demanda.items():
            print(f"{campo.capitalize()}: {valor}")


def buscar_demanda():
    """Busca uma demanda pelo seu identificador."""

    print("\n=== BUSCAR DEMANDA ===")

    identificador = input("Digite o ID: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Demanda encontrada:")
            for campo, valor in demanda.items():
                print(f"{campo.capitalize()}: {valor}")
            return

    print("Demanda não encontrada!")


def atualizar_status():
    """Atualiza o status de uma demanda."""

    print("\n=== ATUALIZAR STATUS ===")

    identificador = input("Digite o ID da demanda: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Status disponíveis:")
            print("1 - Pendente")
            print("2 - Em andamento")
            print("3 - Concluída")

            opcao = input("Escolha o novo status: ").strip()

            status = {
                "1": "Pendente",
                "2": "Em andamento",
                "3": "Concluída"
            }

            if opcao not in status:
                print("Opção inválida!")
                return

            demanda["status"] = status[opcao]

            print("Status atualizado com sucesso!")
            return

    print("Demanda não encontrada!")


def excluir_demanda():
    """Exclui uma demanda pelo seu identificador."""

    print("\n=== EXCLUIR DEMANDA ===")

    identificador = input("Digite o ID da demanda: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            demandas.remove(demanda)
            print("Demanda excluída com sucesso!")
            return

    print("Demanda não encontrada!")


def menu():
    """Apresenta o menu principal do sistema."""

    while True:
        print("\n" + "=" * 35)
        print("       TECHFLOW CORE")
        print("   GERENCIADOR DE DEMANDAS")
        print("=" * 35)

        print("1 - Cadastrar demanda")
        print("2 - Listar demandas")
        print("3 - Buscar demanda")
        print("4 - Atualizar status")
        print("5 - Excluir demanda")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_demanda()

        elif opcao == "2":
            listar_demandas()

        elif opcao == "3":
            buscar_demanda()

        elif opcao == "4":
            atualizar_status()

        elif opcao == "5":
            excluir_demanda()

        elif opcao == "0":
            print("Encerrando o TechFlow Core. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
