
import os
import re


def limpar_tela():
    """Limpa o terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def exibir_cabecalho(titulo="TECHFLOW CORE"):
    """Exibe o cabeçalho padrão do sistema."""
    print("=" * 55)
    print(f"{titulo:^55}")
    print("=" * 55)


def validar_texto(texto):
    """Verifica se o texto contém algum conteúdo."""
    return bool(texto and texto.strip())


def validar_prioridade(prioridade):
    """Verifica se a prioridade é válida."""
    prioridades_validas = ["Alta", "Média", "Baixa"]
    return prioridade.strip().capitalize() in prioridades_validas


def formatar_cep(cep):
    """Remove caracteres não numéricos e formata o CEP."""
    numeros = re.sub(r"\D", "", str(cep))

    if len(numeros) != 8:
        return None

    return f"{numeros[:5]}-{numeros[5:]}"


def formatar_moeda(valor, moeda="R$"):
    """Formata um valor monetário."""
    if valor is None:
        return "Não disponível"

    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X")
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace("X", ".")

    return f"{moeda} {valor_formatado}"
