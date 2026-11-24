
import os


def limpar_tela():
    """Limpa o terminal conforme o sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")


def exibir_cabecalho(titulo):
    """Exibe um cabeçalho padronizado no terminal."""
    print("=" * 45)
    print(titulo.center(45))
    print("=" * 45)


def validar_texto(texto):
    """Verifica se um texto foi preenchido."""
    return bool(texto and texto.strip())


def validar_prioridade(prioridade):
    """Verifica se a prioridade informada é válida."""
    prioridades_validas = ["Alta", "Media", "Baixa"]

    return prioridade.capitalize() in prioridades_validas


def formatar_cep(cep):
    """Remove caracteres não numéricos e formata o CEP."""
    cep_limpo = "".join(caractere for caractere in cep if caractere.isdigit())

    if len(cep_limpo) != 8:
        return None

    return f"{cep_limpo[:5]}-{cep_limpo[5:]}"
