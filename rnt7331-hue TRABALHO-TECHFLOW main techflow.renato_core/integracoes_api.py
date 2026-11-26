
import json
import urllib.request
import urllib.error
from utils import formatar_cep


def consultar_cep(cep):
    """Consulta um CEP na API ViaCEP."""

    cep_formatado = formatar_cep(cep)

    if cep_formatado is None:
        print("CEP inválido. Informe oito números.")
        return None

    cep_numeros = cep_formatado.replace("-", "")
    url = f"https://viacep.com.br/ws/{cep_numeros}/json/"

    try:
        requisicao = urllib.request.Request(
            url,
            headers={"User-Agent": "TechFlowCore/1.0"}
        )

        with urllib.request.urlopen(requisicao, timeout=10) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))

        if dados.get("erro"):
            print("CEP não encontrado.")
            return None

        return {
            "cep": cep_formatado,
            "logradouro": dados.get("logradouro", ""),
            "bairro": dados.get("bairro", ""),
            "cidade": dados.get("localidade", ""),
            "uf": dados.get("uf", "")
        }

    except urllib.error.HTTPError as erro:
        print(f"Erro HTTP ao consultar CEP: {erro.code}")
    except urllib.error.URLError:
        print("Não foi possível conectar à API ViaCEP.")
    except TimeoutError:
        print("Tempo limite excedido na consulta do CEP.")
    except (json.JSONDecodeError, UnicodeDecodeError):
        print("A API ViaCEP retornou uma resposta inválida.")
    except OSError as erro:
        print(f"Erro de conexão ao consultar CEP: {erro}")

    return None


def consultar_cotacao_dolar():
    """Consulta a cotação atual do dólar comercial."""

    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    try:
        requisicao = urllib.request.Request(
            url,
            headers={"User-Agent": "TechFlowCore/1.0"}
        )

        with urllib.request.urlopen(requisicao, timeout=10) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))

        cotacao = float(dados["USDBRL"]["bid"])

        if cotacao <= 0:
            raise ValueError("Cotação inválida.")

        return cotacao

    except urllib.error.HTTPError as erro:
        print(f"Erro HTTP ao consultar dólar: {erro.code}")
    except urllib.error.URLError:
        print("Não foi possível conectar à API de cotação.")
    except TimeoutError:
        print("Tempo limite excedido na consulta do dólar.")
    except (KeyError, ValueError, TypeError, json.JSONDecodeError,
            UnicodeDecodeError):
        print("Não foi possível interpretar a cotação recebida.")
    except OSError as erro:
        print(f"Erro de conexão ao consultar dólar: {erro}")

    return None


def converter_brl_para_usd(valor_brl, cotacao=None):
    """Converte reais para dólares utilizando a cotação informada."""

    try:
        valor_brl = float(valor_brl)

        if valor_brl < 0:
            return None

        if cotacao is None:
            cotacao = consultar_cotacao_dolar()

        if cotacao is None or float(cotacao) <= 0:
            return None

        return valor_brl / float(cotacao)

    except (ValueError, TypeError, ZeroDivisionError):
        return None
