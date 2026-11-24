
from utils import (
    validar_texto,
    validar_prioridade,
    formatar_cep,
    exibir_cabecalho
)

exibir_cabecalho("TESTE DO MÓDULO UTILS")

print("Texto válido:", validar_texto("TechFlow"))
print("Texto vazio:", validar_texto("   "))
print("Prioridade válida:", validar_prioridade("Alta"))
print("Prioridade inválida:", validar_prioridade("Urgente"))
print("CEP formatado:", formatar_cep("55150000"))
print("CEP inválido:", formatar_cep("123"))
