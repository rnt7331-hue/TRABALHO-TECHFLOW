
from gerenciador_demandas import (
    cadastrar_demanda,
    listar_demandas,
    buscar_demanda,
    atualizar_status,
    excluir_demanda,
    filtrar_por_prioridade,
    STATUS_VALIDOS,
    PRIORIDADES_VALIDAS
)

from integracoes_api import (
    consultar_cep,
    consultar_cotacao_dolar,
    converter_brl_para_usd
)

from utils import (
    limpar_tela,
    exibir_cabecalho,
    formatar_cep,
    formatar_moeda
)


def pausar():
    input("\nPressione ENTER para continuar...")


def ler_valor_monetario():
    """Solicita um valor monetário válido."""

    while True:
        entrada = input("Valor estimado em reais (R$): ").strip()
        entrada = entrada.replace(".", "").replace(",", ".")

        try:
            valor = float(entrada)

            if valor < 0:
                print("O valor não pode ser negativo.")
                continue

            return valor

        except ValueError:
            print("Digite um valor numérico válido. Exemplo: 1500,50")


def exibir_demanda(demanda):
    """Exibe os dados completos de uma demanda."""

    print("\n" + "-" * 50)
    print(f"ID: {demanda['id']}")
    print(f"Título: {demanda['titulo']}")
    print(f"Solicitante: {demanda['solicitante']}")
    print(f"Prioridade: {demanda['prioridade']}")
    print(f"CEP: {demanda['cep']}")
    print(f"Cidade: {demanda['cidade']}")
    print(f"Status: {demanda['status']}")
    print(
        "Valor estimado em reais: "
        + formatar_moeda(demanda["valor_estimado_brl"], "R$")
    )
    print(
        "Valor estimado em dólares: "
        + formatar_moeda(demanda["valor_estimado_usd"], "US$")
    )
    print("-" * 50)


def cadastrar():
    """Fluxo de cadastro de uma nova demanda."""

    limpar_tela()
    exibir_cabecalho("CADASTRAR DEMANDA")

    titulo = input("Título da demanda: ").strip()

    if not titulo:
        print("O título é obrigatório.")
        return

    solicitante = input("Nome do solicitante: ").strip()

    if not solicitante:
        print("O solicitante é obrigatório.")
        return

    print("\nPrioridades disponíveis:")
    for prioridade in PRIORIDADES_VALIDAS:
        print(f"- {prioridade}")

    prioridade = input("Escolha a prioridade: ").strip().capitalize()

    if prioridade not in PRIORIDADES_VALIDAS:
        print("Prioridade inválida.")
        return

    while True:
        cep_digitado = input("\nCEP: ").strip()
        cep = formatar_cep(cep_digitado)

        if cep is None:
            print("CEP inválido. Digite os oito números.")
            continue

        break

    print("\nConsultando endereço...")
    endereco = consultar_cep(cep)

    if endereco:
        cidade = endereco["cidade"]
        print(f"Endereço localizado: {cidade}/{endereco['uf']}")
    else:
        cidade = input("Informe a cidade manualmente: ").strip()

        if not cidade:
            print("A cidade é obrigatória.")
            return

    valor_brl = ler_valor_monetario()

    print("\nConsultando cotação do dólar...")
    cotacao = consultar_cotacao_dolar()

    if cotacao is not None:
        valor_usd = converter_brl_para_usd(valor_brl, cotacao)
        print(f"Cotação utilizada: {formatar_moeda(cotacao, 'R$')}")
        print(f"Conversão: {formatar_moeda(valor_usd, 'US$')}")
    else:
        valor_usd = None
        print("Cotação indisponível. O cadastro continuará sem conversão.")

    dados = {
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "cidade": cidade,
        "valor_estimado_brl": valor_brl,
        "valor_estimado_usd": valor_usd
    }

    sucesso, mensagem, demanda = cadastrar_demanda(dados)

    print(f"\n{mensagem}")

    if sucesso:
        print(f"Demanda cadastrada com ID: {demanda['id']}")


def listar():
    """Exibe todas as demandas cadastradas."""

    limpar_tela()
    exibir_cabecalho("LISTAGEM DE DEMANDAS")

    demandas = listar_demandas()

    if not demandas:
        print("Nenhuma demanda cadastrada.")
        return

    for demanda in demandas:
        exibir_demanda(demanda)


def buscar():
    """Busca e exibe uma demanda pelo ID."""

    limpar_tela()
    exibir_cabecalho("BUSCAR DEMANDA")

    try:
        id_demanda = int(input("Informe o ID da demanda: "))
    except ValueError:
        print("ID inválido.")
        return

    demanda = buscar_demanda(id_demanda)

    if demanda:
        exibir_demanda(demanda)
    else:
        print("Demanda não encontrada.")


def atualizar():
    """Atualiza o status de uma demanda."""

    limpar_tela()
    exibir_cabecalho("ATUALIZAR STATUS")

    try:
        id_demanda = int(input("ID da demanda: "))
    except ValueError:
        print("ID inválido.")
        return

    print("\nStatus disponíveis:")
    for status in STATUS_VALIDOS:
        print(f"- {status}")

    novo_status = input("\nNovo status: ").strip()

    sucesso, mensagem = atualizar_status(id_demanda, novo_status)

    print(f"\n{mensagem}")


def excluir():
    """Exclui uma demanda."""

    limpar_tela()
    exibir_cabecalho("EXCLUIR DEMANDA")

    try:
        id_demanda = int(input("ID da demanda que deseja excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    demanda = buscar_demanda(id_demanda)

    if demanda is None:
        print("Demanda não encontrada.")
        return

    exibir_demanda(demanda)

    confirmacao = input(
        "\nTem certeza que deseja excluir esta demanda? (S/N): "
    ).strip().upper()

    if confirmacao == "S":
        sucesso, mensagem = excluir_demanda(id_demanda)
        print(mensagem)
    else:
        print("Exclusão cancelada.")


def filtrar():
    """Filtra as demandas pela prioridade."""

    limpar_tela()
    exibir_cabecalho("FILTRAR POR PRIORIDADE")

    print("Prioridades disponíveis:")
    for prioridade in PRIORIDADES_VALIDAS:
        print(f"- {prioridade}")

    prioridade = input("\nEscolha a prioridade: ").strip().capitalize()

    if prioridade not in PRIORIDADES_VALIDAS:
        print("Prioridade inválida.")
        return

    resultado = filtrar_por_prioridade(prioridade)

    if not resultado:
        print(f"Nenhuma demanda com prioridade {prioridade}.")
        return

    print(f"\nDemandas com prioridade {prioridade}:")

    for demanda in resultado:
        exibir_demanda(demanda)


def consultar_dolar():
    """Consulta e apresenta a cotação atual do dólar."""

    limpar_tela()
    exibir_cabecalho("COTAÇÃO DO DÓLAR")

    cotacao = consultar_cotacao_dolar()

    if cotacao is not None:
        print(f"\nCotação atual: {formatar_moeda(cotacao, 'R$')}")
        print("Referência: dólar comercial (USD/BRL).")
    else:
        print("\nNão foi possível consultar a cotação neste momento.")


def exibir_menu():
    """Apresenta o menu principal do sistema."""

    print("\n1 - Cadastrar demanda")
    print("2 - Listar demandas")
    print("3 - Buscar demanda")
    print("4 - Atualizar status")
    print("5 - Excluir demanda")
    print("6 - Filtrar por prioridade")
    print("7 - Consultar cotação do dólar")
    print("0 - Sair")

    return input("\nEscolha uma opção: ").strip()


def main():
    """Executa o sistema TechFlow Core."""

    while True:
        limpar_tela()
        exibir_cabecalho("SISTEMA DE GESTÃO TECHFLOW CORE")

        opcao = exibir_menu()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            atualizar()
        elif opcao == "5":
            excluir()
        elif opcao == "6":
            filtrar()
        elif opcao == "7":
            consultar_dolar()
        elif opcao == "0":
            print("\nEncerrando o TechFlow Core. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

        if opcao != "0":
            pausar()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nExecução interrompida pelo usuário.")
