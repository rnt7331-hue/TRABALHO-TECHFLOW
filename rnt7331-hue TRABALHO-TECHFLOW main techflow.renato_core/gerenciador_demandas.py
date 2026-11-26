
from utils import validar_texto, validar_prioridade


demandas = []

PRIORIDADES_VALIDAS = ["Alta", "Média", "Baixa"]

STATUS_VALIDOS = [
    "Pendente",
    "Em andamento",
    "Concluída"
]


def cadastrar_demanda(dados):
    """Valida e cadastra uma nova demanda."""

    campos_obrigatorios = [
        "titulo",
        "solicitante",
        "prioridade",
        "cep",
        "cidade"
    ]

    for campo in campos_obrigatorios:
        if not validar_texto(str(dados.get(campo, ""))):
            return False, f"O campo {campo} é obrigatório.", None

    prioridade = dados["prioridade"].strip().capitalize()

    if not validar_prioridade(prioridade):
        return False, "Prioridade inválida.", None

    try:
        valor_brl = float(dados["valor_estimado_brl"])
        if valor_brl < 0:
            return False, "O valor não pode ser negativo.", None
    except (ValueError, TypeError, KeyError):
        return False, "Valor estimado inválido.", None

    novo_id = max(
        (demanda["id"] for demanda in demandas),
        default=0
    ) + 1

    nova_demanda = {
        "id": novo_id,
        "titulo": dados["titulo"].strip(),
        "solicitante": dados["solicitante"].strip(),
        "prioridade": prioridade,
        "cep": dados["cep"].strip(),
        "cidade": dados["cidade"].strip(),
        "status": "Pendente",
        "valor_estimado_brl": valor_brl,
        "valor_estimado_usd": dados.get("valor_estimado_usd")
    }

    demandas.append(nova_demanda)

    return True, "Demanda cadastrada com sucesso!", nova_demanda


def listar_demandas():
    """Retorna todas as demandas cadastradas."""
    return demandas


def buscar_demanda(id_demanda):
    """Busca uma demanda pelo identificador."""

    try:
        id_demanda = int(id_demanda)
    except (ValueError, TypeError):
        return None

    for demanda in demandas:
        if demanda["id"] == id_demanda:
            return demanda

    return None


def atualizar_status(id_demanda, novo_status):
    """Atualiza o status de uma demanda."""

    demanda = buscar_demanda(id_demanda)

    if demanda is None:
        return False, "Demanda não encontrada."

    novo_status = novo_status.strip().capitalize()

    if novo_status not in STATUS_VALIDOS:
        return False, "Status inválido."

    demanda["status"] = novo_status

    return True, "Status atualizado com sucesso!"


def excluir_demanda(id_demanda):
    """Exclui uma demanda pelo identificador."""

    demanda = buscar_demanda(id_demanda)

    if demanda is None:
        return False, "Demanda não encontrada."

    demandas.remove(demanda)

    return True, "Demanda excluída com sucesso!"


def filtrar_por_prioridade(prioridade):
    """Retorna somente as demandas da prioridade escolhida."""

    prioridade = prioridade.strip().capitalize()

    if prioridade not in PRIORIDADES_VALIDAS:
        return []

    return [
        demanda for demanda in demandas
        if demanda["prioridade"] == prioridade
    ]
